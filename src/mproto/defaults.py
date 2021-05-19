from .proto import BaseProtoHandler

class TestProto(BaseProtoHandler):
  def test_open(self,req):
    return req.get_full_url()
