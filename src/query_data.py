import meraki
import os
from commons import API_KEY, ORG_ID
import requests
import json
import time
from datetime import datetime


meraki_client = meraki.DashboardAPI(API_KEY)

response = meraki_client.organizations.getOrganizations()
org_id = response[0]['id']


# Get the networks 
networks = meraki_client.organizations.getOrganizationNetworks(organizationId=org_id)
camera_networks = [n for n in networks if 'camera' in n['productTypes']]


print("Organization ID: ", org_id)
print("Organization name: ", response[0]['name'])
# Print the network ID(s) of the camera network(s)
for network in camera_networks:
    print('Network ID for camera network:', network['id'])
    print('Network name: ', network['name'])


# inventory = meraki_client.organizations.getOrganizationInventoryDevices(ORG_ID)
# print(inventory)

