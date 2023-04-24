import meraki
import os


# Defining your API key as a variable in source code is not recommended
API_KEY =os.getenv('CAMERA_API_KEY')
#print(API_KEY)
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

serial = 'Q2LV-KGF5-GDKS'

response = dashboard.camera.getDeviceCameraCustomAnalytics(
    serial
)

print(response)