import os

from epm.paths import normalize_path

class Location(object):

  PROJECT = 'Project'
  CONAN = 'CONAN_STORAGE_PATH' # conan storage path

  def __init__(self, path, root=Location.PROJECT, mapper=None):
    assert(root in [Location.PROJECT, Location.CONAN])
    self.path_ = normalize_path(path)
    self.root_ = root
    self.mapper_ = mapper_

  @property
  def abspath(self):
    root = self.mapper.get(self.root_) if self.mapper else None
    if root is None:
      return os.path.abspath(self.path_)
    assert(not os.path.isabs(self.path_))
    return  normalize_path('%s/%s' % (root, self.path_))

  @property
  def path(self):
    return self.path_

  @property
  def mapper(self):
    return {
      Location.PROJECT: normalize_path(os.path.abspath('.')),
      Location.CONAN: normalize_path(os.)
    }

