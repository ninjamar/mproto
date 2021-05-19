import urllib.request as urlreq


class BaseProtoHandler(urlreq.BaseHandler):
  '''
  Handles installing protocols
  Thanks to @imfh (https://scratch.mit.edu/users/imfh) for making the base code
  '''
  installed = []
  @classmethod
  def install(cls):
    cls.installed.append(cls)
    opener = urlreq.build_opener(*cls.installed)
    urlreq.install_opener(opener)

  @classmethod
  def uninstall(cls):
    cls.installed.remove(cls.installed.index(cls))
    opener = urlreq.build_opener(*cls.installed)
    urlreq.install_opener(opener)
  
  @classmethod
  def is_installed(cls):
    return cls in cls.installed
