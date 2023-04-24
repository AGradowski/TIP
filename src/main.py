import meraki
import os
from commons import API_KEY, CAMERA_1_SID

meraki_client = meraki.DashboardAPI(API_KEY)
response = meraki_client.camera.getDeviceCameraCustomAnalytics(CAMERA_1_SID)

print(response)

