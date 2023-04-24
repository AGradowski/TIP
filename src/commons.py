import os

CAMERA_1_SID = "Q2LV-KGF5-GDKS"
CAMERA_2_SID = "Q2LV-5CU2-FJ6R"

API_KEY = os.getenv('MERAKI_DASHBOARD_API_KEY')
assert API_KEY is not None, "API Key must not be None"
