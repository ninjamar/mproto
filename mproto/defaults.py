import urllib.request as urlreq

class TestProto(urlreq.BaseHandler):

  def python_open(self,req):
    print(dir(req))
    return req.get_full_url()
