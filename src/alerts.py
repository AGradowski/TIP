import meraki
from commons import API_KEY, CAMERA_1_SID, ORG_ID, NETWORK_ID
import requests
import json
import time

NETWORK_ID='L_595038100766333474'

meraki_client = meraki.DashboardAPI(API_KEY)

# Define a function to monitor camera events
def monitor_cameras_events(cameras):
    while True:
        for camera in cameras:
            events = meraki_client.camera.getDeviceCameraAnalyticsLive(camera['serial'])
            print(events)
        time.sleep(100)

# Get the cameras for the specified network
print(f"Network ID: {NETWORK_ID}")
all_devices = meraki_client.networks.getNetworkDevices(NETWORK_ID)
cameras = [n for n in all_devices if n['model'] == "MV93X"]
print(f"Cameras: {cameras}")

monitor_cameras_events(cameras)