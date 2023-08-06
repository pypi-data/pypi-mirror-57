#!/usr/bin/env python
from iCR import iCR
bigip = iCR("172.24.9.132","admin","admin")
bigip.debug = True
bigip.get_token()
bigip.password = "wrongpassword"
print ("Token: " + str(bigip.token))
nodes = bigip.get("ltm/node",select='name')
print ("---------------------------")
print ("Nodes:" + str(len(nodes['items'])))
bigip.delete_token()
