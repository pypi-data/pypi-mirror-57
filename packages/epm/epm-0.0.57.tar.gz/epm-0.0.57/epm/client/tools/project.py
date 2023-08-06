import os
import yaml
import sys
import shutil

from epm.errors import EException
from epm.client.output import Output
from epm.utils.files import mkdir
from jinja2 import PackageLoader,Environment

_DEP_DEMO='''#
#dependencies:
#  dep-lib-name:
#    version: version_this_module_dep
#    user: user_of_the_dep_module
'''

_DESCRIPTION = '{name} is {type} ....'

_LICENSE = 'MIT'


class Initializer(object):

    def __init__(self, args):
        self._type = args.type
        self._out_dir = os.path.abspath('.')
        self._jinja2_project_env = Environment(loader=PackageLoader('epm', 'data/project'))
        self._manifest = {}
        self.out = Output(sys.stdout, sys.stderr, color=True)

        if os.path.exists('package.yml'):
            with open('package.yml') as f:
                self._manifest = yaml.safe_load(f)

        name = os.path.basename(os.path.abspath('.'))
        name = self._manifest.get('name') or args.name or name
        version = self._manifest.get('version') or args.version or '0.0.1'
        user = self._manifest.get('user') or 'examples'
        self._name = name

        self._manifest['name'] = name
        self._manifest['version'] = version
        self._manifest['user'] = user

    @property
    def name(self):
        return self._manifest['name']

    @property
    def type(self):
        return self._type

    @property
    def user(self):
        return self._manifest['user']

    @property
    def version(self):
        return self._manifest['version']

    def _gitlab_ci(self):
        dst ='script/gitlab-ci.py'
        folder = os.path.dirname(dst)
        if folder:
            mkdir(folder)
        import epm

        filename = os.path.join(os.path.dirname(epm.__file__),
                                'data', 'project', 'script','gitlab-ci2.py')

        with open(filename) as f:
            content = f.read()
        tests = "    ('{}', '')".format('test_package' if self._type =='lib' else self._name)
        content = content.replace('@TESTs@', tests)

        with open(dst, 'w') as f:
            f.write(content)

    def _common(self):
        self._gitlab_ci()

        #self._copy('script/gitlab-ci2.py', 'script/gitlab-ci.py')
        self._out('.gitignore', '.gitignore')
        self._out('conanfile.py', 'conanfile.py')
        self._docs()

    def _docs(self):
        self._out('docs/mkdocs.yml', 'docs/mkdocs.yml')
        self._out('docs/index.md', 'docs/index.md')
        self._out('docs/release-notes.md', 'docs/release-notes.md')
        self._out('docs/user-guide.md', 'docs/user-guide.md')
        if not os.path.exists('README.md'):
            self._out('README.md', 'README.md')

    def _library(self):
        self._common()

        self._out('include/declaration.h', 'include/{0}/declaration.h'.format(self.name))
        self._out('include/lib.h', 'include/{0}/{0}.h'.format(self.name))
        self._out('source/lib.c', 'source/{0}.c'.format(self.name))

        self._out('CMakeLists.txt', 'CMakeLists.txt')
        self._out('cmake/libCMakeLists.txt', 'cmake/CMakeLists.txt')
        self._out('cmake/config.cmake.in', 'cmake/{}-config.cmake.in'.format(self.name))

        self._out('test_package/main.cpp', 'test_package/src/main.cpp')
        self._out('test_package/test.cpp', 'test_package/src/test.cpp')
        self._out('test_package/CMakeLists.txt', 'test_package/CMakeLists.txt')
        self._out('test_package/conanfile.py', 'test_package/conanfile.py')

    def _application(self):
        self._common()

        self._out('source/main.c', 'source/main.c')

        self._out('CMakeLists.txt', 'CMakeLists.txt')
        self._out('cmake/CMakeLists.txt', 'cmake/CMakeLists.txt')

        self._out('test_package/main.py', 'test_package/main.py')
        self._out('test_package/test_version.py', 'test_package/test_{}.py'.format(self.name))
        self._out('test_package/app-conanfile.py', 'test_package/conanfile.py')

    def _out(self, template, filename, **kwargs):
        env = self._jinja2_project_env
        tmpl = env.get_template(template)
        vars = dict({'name': self.name,
                     'version': self.version,
                     'user': self.user,
                     'type': self._type,
                     'manifest': self._manifest},

                    **kwargs)

        content = tmpl.render(vars)

        folder = os.path.dirname(os.path.abspath(filename))
        if not os.path.exists(folder):
            os.makedirs(folder)

        with open(filename, 'w') as f:
            f.write(content)

    def _gen_manifest(self):
        ''' format and update manifest
        '''
        import copy

        manifest = copy.deepcopy(self._manifest)
        license = manifest.get('license', _LICENSE)
        description = manifest.get('description', _DESCRIPTION.format(name=self.name, type=self.type))
        sandbox = manifest.get('sandbox', {})
        dependencies = manifest.get('dependencies', {})

        configuration = manifest.get('configuration', {})
        if not configuration.get('profile'):
            configuration['profile'] = ['vs2019', 'gcc5']
            configuration['scheme'] = {
                'dynamic': {'shared': True}
            }

            deps = {}
            for k, v in dependencies.items():
                deps[k] = 'dynamic'

            if deps:
                configuration['scheme']['dynamic']['.dependencies'] = deps

        script = manifest.get('script', {})

        if not script.get('gitlab-ci'):
            script['gitlab-ci'] = 'python script/gitlab-ci.py'

        if not script.get('build-docs'):
            script['build-docs'] = 'mkdocs build -f docs/mkdocs.yml -d ../.epm'

        if not script.get('docs-server'):
            script['docs-server'] = 'mkdocs serve -f docs\mkdocs.yml'

        if self._type == 'app':
            if not script.get('test', {}):
                script['test'] = 'test_package/main.py ${configuration}'

            if not sandbox.get(self.name, {}):
                sandbox = {self.name: 'package/bin/%s' % self.name}

        else:
            if not sandbox.get('test_package', {}):
                sandbox = {'test_package': 'test_package/%s_test' % self.name}

        for key in ['name', 'version', 'user', 'sandbox', 'configuration', 'script',
                    'dependencies', 'license', 'description']:
            if key in manifest.keys():
                del manifest[key]

        license = yaml.dump({'license': license}, default_flow_style=False)
        description = yaml.dump({'description': description}, default_flow_style=False)

        sandbox = yaml.dump({'sandbox': sandbox},
                            default_flow_style=False)
        configuration = yaml.dump({'configuration': configuration},
                                  default_flow_style=False)
        script = yaml.dump({'script': script},
                           default_flow_style=False)
        dependencies = yaml.dump({'dependencies': dependencies},
                                 default_flow_style=False) if dependencies else _DEP_DEMO
        if os.path.exists('package.yml'):
            filename = 'package.yml.origin'
            i =1
            while True:
                if not os.path.exists(filename):
                    break
                i += 1
                filename = 'package.yml.origin.{}'.format(i)

            os.rename('package.yml', filename)
        self._out('package.yml', 'package.yml',
                  configuration=configuration,
                  sandbox=sandbox,
                  script=script,
                  dependencies=dependencies,
                  license=license,
                  description=description)

    def generate(self):
        if self._type == 'lib':
            self._library()
        if self._type == 'app':
            self._application()

        self._gen_manifest()
        self.out.success('{} package <{}> project created successfully.'.format(
            self.type, self.name))

        self.out.info('To build project, run command:  epm -c {} build'.format(
            self._manifest.get('configuration', {}).get('profile', ['vs2019'])[0]))

