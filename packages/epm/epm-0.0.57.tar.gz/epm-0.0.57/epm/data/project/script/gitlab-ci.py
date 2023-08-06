import os
import re
import yaml
import collections
from jinja2 import PackageLoader, Environment, FileSystemLoader

__dir__ = os.path.abspath(os.path.dirname(__file__))
template = '''

'''
from string import Template
from epm.worker.api import WorkerAPI
from conans.client.profile_loader import read_profile


_VisualStudio = '''
${build}:
  stage: build
  tags:  
    - Windows
    - EPM
    - VS2019
  artifacts:
    paths:
      - .epm
      - .conan
${test}:
  stage: test
  tags:
    - Windows
    - runner
    
  dependencies:
    - ${build}
    
${deploy}:
  stage: deploy
  tags:
    - Windows
    - EPM
    - deployer  
  dependencies:
    - ${build}
'''

_GCC = '''
${build}:
  stage: build
  image: ${docker_builder}
  tags:  
    - Linux
    - docker-executor
    - builder
  
  artifacts:
    paths:
      - .epm
      - .conan  
${test}:
  stage: test  
  image: ${docker_runner}
  tags:
    - Linux
    - docker-executor
    - runner
    
  dependencies:
    - ${build}
    
${deploy}:
  stage: deploy  
  image: ${docker_builder}
  tags:
    - Linux
    - docker-executor
    - deployer
  
  dependencies:
    - ${build}
'''


_HISI = '''
${build}:
  stage: build
  image: ${docker_builder}
  tags:  
    - Linux
    - docker-executor
    - builder
  
  artifacts:
    paths:
      - .epm
      - .conan

${test}:
  stage: test
  tags:
    - Linux
    - docker-executor
    - device-agent
    
  dependencies:
    - ${build}
   
${deploy}:
  stage: deploy  
  image: ${docker_builder}
  tags:
    - Linux
    - docker-executor
    - deployer
  
  dependencies:
    - ${build}
'''

_BUILD = 'epm -c {} create --clear --cache --runner shell'
_UPLOAD = 'epm -c {} upload'

{% if type == 'app' %}
_TEST = [
    'epm -c {} run test'
]
_WinTest = _TEST
_HiSiTest = _TEST

{% else %}

_TEST = [
    './.epm/{}/sandbox/test_package'
]

_WinTest = [
    '.epm/{}/sandbox/test_package'
]

_HiSiTest = [
    'epm -c {} sandbox test_package'
]
{% endif %}

_PROFILESPLIT='''
#=================================================
#      {}
#=================================================
'''
_SCRIPT='''#
#  This GitLab CI script was generate by {0}
#  Please do not change this file directly, 
#  edit {0} if you want do some changes. 
#
stages:
  - build
  - test
  - deploy
'''.format(os.path.relpath(__file__, os.path.dirname('.')).replace('\\', '/'))


def get_profiles(name, profiles, all=False):
    result = []
    for key, value in profiles.items():
        if not key.startswith(name):
            continue
        if all or not value.get('hiden'):
            result.append(key)
    return result


def main():
    api = WorkerAPI()
    api.create_app()
    profiles = api.worker.profiles
    script = _SCRIPT

    with open('package.yml') as f:
        manifest = yaml.safe_load(f)

    schemes = list(manifest.get('configuration', {}).get('scheme', {}).keys())
    if 'default' not in schemes:
        schemes = ['default'] + schemes

    for name in manifest.get('configuration', {}).get('profile', {}):
        profile = profiles.get(name, None)
        if profile is None:
            raise Exception('package.yml configuration.profile {} not installed.'.format(name))

        docker = profile[name].get('docker', {})

        docker_builder = docker.get('builder', {}).get('image')
        docker_runner = docker.get('runner', {}).get('image')
        {% if type == 'app' %}
        docker_runner = docker_builder
        {% endif %}

        d = os.path.dirname(profile['__file__'])
        pr, _ = read_profile(name, d, d)

        tests = _TEST
        stage = None
        if pr.settings['compiler'] == 'Visual Studio':
            stage = _VisualStudio
            tests = _WinTest
        elif pr.settings['compiler'] == 'gcc' and pr.settings['arch'] in ['x86', 'x86_64']:
            stage = _GCC
        elif pr.settings['compiler'] == 'gcc' and pr.settings['arch'] in ['armv7']:
            stage = _HISI
            tests = _HiSiTest
        else:
            print(pr.settings['compiler'], pr.settings['arch'])
            raise Exception('Not find tempalte')

        #
        # generate all scheme jobs
        #
        script += _PROFILESPLIT.format(name)
        for scheme in schemes:

            configuration = "{}" if scheme == 'default' else ("{}@%s" % scheme)

            c = configuration.format(name)
            build = "build:{}".format(c)
            test = "test:{}".format(c)
            deploy = "deploy:{}".format(c)

            templ = Template(stage)
            text = templ.substitute(build=build, test=test, deploy=deploy,
                                    docker_builder=docker_builder,
                                    docker_runner=docker_runner,
                                    configuration=c)

            section = yaml.safe_load(text)
            section[build]['script'] = []
            section[test]['script'] = []
            section[deploy]['script'] = []
            for p in get_profiles(name, profile):
                c = configuration.format(p)
                section[build]['script'].append(_BUILD.format(c))
                section[deploy]['script'].append(_UPLOAD.format(c))
                for cmd in tests:
                    section[test]['script'].append(cmd.format(c))

            script += yaml.safe_dump(section, default_flow_style=False) + "\n"

    with open('.gitlab-ci.yml', 'w') as f:
        f.write(script)
    return script


if __name__ == '__main__':
    main()