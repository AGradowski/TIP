import typing as tp


class CameraSnapshotResponse(tp.TypedDict):
    url: str
    expiry: str

