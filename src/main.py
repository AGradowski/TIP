import meraki
import requests as req
import os
from commons import API_KEY, CAMERA_1_SID
from typedefs.meraki import CameraSnapshotResponse
from PIL import Image


def get_camera_snapshot(client: meraki.DashboardAPI) -> CameraSnapshotResponse:
    # response: CameraSnapshotResponse = client.camera.generateDeviceCameraSnapshot(
    #     CAMERA_1_SID
    # )
    #
    # print("Meraki response", response)

    # url = response['url']
    url = "https://spn3003.meraki.com/stream/jpeg/snapshot/41cbf1d53288a6b0VHYjkxZmQwYmNmZGQ1NTkyYjRiOGY3OWM5YjY0MWNhM2VhYjFiYTE1NzE2YzgyMjAxMWZjY2RlY2Q5ODVhMjRmZPoVYKseR8nJah7SN9CuzGiEe3MaAhvyHD4KXRrJh59jzHx_i8a4g6ngRZ7lNUyJDPZKpB5CDrR090Y4rMyxXj4wIOBBGE25kZp_bLpHVKeYsjAZuUJquyKODpDdoIsnBgZw6hqQaSfVrbNJJbkL4SitJpfaiIkgesErtTglWHivp6DphGFTCTN3HKc4j2mtgto9bA_atTzpXl1YVDpejus"

    assert url is not None, "Url should be present"

    response: req.Response = req.get(url)

    print(type(response))
    # print(response.encoding)
    # print(response.text)
    # print(response.content)
    return response


# meraki_client = meraki.DashboardAPI(API_KEY)

# response = meraki_client.camera.getDeviceCameraCustomAnalytics(CAMERA_1_SID)
# print(response)

# response = get_camera_snapshot(meraki_client)
# print(response.encoding)
# print(response.content)

print(os.getcwd())

im = Image.open("image.png")
im.show()

