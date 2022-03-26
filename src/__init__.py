from src.models import Camera
from src.ui import widgets
from src.utils import check_cameras
from src.views import StartWindow


def start_gui():

    cam_0_on, cam_1_on = check_cameras()

    resolution = (1280, 720)
    fourcc = "XVID"
    fps = 30
    timestamped = True

    camera_0 = (
        Camera(0, resolution, fourcc, fps, timestamped=timestamped)
        if cam_0_on
        else None
    )
    camera_1 = (
        Camera(1, resolution, fourcc, fps, timestamped=timestamped)
        if cam_1_on
        else None
    )

    app = widgets.QApplication([])
    start_window = StartWindow((camera_0, camera_1))
    start_window.show()
    app.exit(app.exec_())
