## Description
mproto is a python package for making custom protocols
## Installation
### pip
```bash
pip install mproto
```
## Usage
```python
import mproto
import urllib.request as urlreq

class MyCustomProtocol(mproto.BaseProtoHandler)
  def protocolname_open(self,req): #name must be protocol name + _open
    # do stuff with req
    return req.get_full_url()

mproto.install(MyCustomProtocol)
print(urlreq.urlopen('protocolname://abc')) #should print "protocolname://abc"
```

## Other
[docs](https://ninjamar.repl.co/mproto/docs)
[usefull stuff](https://scratch.mit.edu/discuss/topic/515027/)
