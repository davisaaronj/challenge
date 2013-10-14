#!/usr/bin/python
#cloud server information list
#usage listerservers <username> <api key>
#simple python script using kenova and pyrax.

__author__ = 'Aaron Davis aaron.davis@rackspace.com'

import pyrax
import sys
import os

#Pyrax specific
pyrax.set_setting('identity_type', 'rackspace')

# Initially made this prompt but decided to pass arguments
#username = raw_input("Enter username: ")
#apikey = raw_input("Enter API Key: ")

#grabs the Auth args
username = sys.argv[1]
apikey = sys.argv[2]

#Not sure if region= was needed but left it since it's working
pyrax.set_credentials(username, apikey, region='DFW',  authenticate=True)

regions = ['ORD', 'DFW', 'IAD', 'SYD']
#Open Stack servers list
for location in regions:
    cs = pyrax.connect_to_cloudservers(region=location)
    print "Cloud servers in region: ", location
    cslist = cs.servers.list()
    for server in cslist:
        sinfo = cs.servers.get(server)
        print sinfo.human_id, sinfo.id, sinfo.accessIPv4, sinfo.status

#Hacked together Firstgen server information (I don't like this but with kenova it saves quite a few steps)
#will eventually replace this with requests


print "Legacy cloud servers: "
knew = 'bash ~/.kenova new username apikey'
klus = 'bash ~/.kenova lus show'
os.system(knew)
os.system(klus)


