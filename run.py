from mproto.defaults import TestProto
from mproto.installer import install
import urllib.request as urlreq

install(TestProto)

print(urlreq.urlopen('test://abc'))
