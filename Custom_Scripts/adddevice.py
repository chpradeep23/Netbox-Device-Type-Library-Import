import pynetbox
import os
import time

NETBOX_URL = 'HTTPS://10.16.32.17'
NETBOX_TOKEN = '62a2ca8ee97b1d72b6b942d22f0ff87472d8e0a7'

netbox = pynetbox.api(NETBOX_URL, token=NETBOX_TOKEN,)
netbox.http_session.verify = False

device = netbox.dcim.devices.create([
                 {
                    "name": "dc4-sf-spine-sec",
                    "device_type": 756,
                    "role": 1,
                    "site": 13,
                    "status": "active",
                 }
])
if device:
    print(f"Device {device} created successfully.")
else:
    print("Failed to create device")