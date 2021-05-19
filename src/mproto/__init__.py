'''
Python library for managing custom protocols
Let Python make requests to urls such as "python://abc"
'''

from .proto import BaseProtoHandler

def install(*a):
  for i in a:
    getattr(i,'install')()
