#!/usr/bin/env python
from iCR import iCR
bigip = iCR("172.24.9.132","admin","admin")
nodes = bigip.get("ltm/node",select='name')

for node in nodes['items']:
  print node['name']