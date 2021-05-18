import urllib.request as urlreq

def install(*s):
  '''
  Installs different uri shemes
  *s must be derived from urllib.request.BaseHandler
  '''
  for i in s:
    if not isinstance(i,type(urlreq.BaseHandler)):
      raise TypeError('"s" must be of type "urllib.request.BaseHandler"')
    else:
      opener = urlreq.build_opener(i())
      urlreq.install_opener(opener)
