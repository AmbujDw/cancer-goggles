from __future__ import annotations

from datetime import datetime
from enum import Enum

import cv2

from src.ui import gui


class Surgery(Enum):
    Test = 1
    A = 2
    B = 3
    C = 4


def check_camera(id: int | str):
    cam = cv2.VideoCapture(id)
    cam_on, _ = cam.read()
    cam.release()
    return cam_on


def check_cameras():
    cam_on_0 = check_camera(0)
    cam_on_1 = check_camera(1)
    return cam_on_0, cam_on_1


def ndarray_to_qpixmap(img):
    if img.ndim == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    w, h, _ = img.shape
    qimg = gui.QImage(img.data, h, w, 3 * h, gui.QImage.Format_RGB888)
    return gui.QPixmap(qimg)


def to_timestamped_frame(img):
    now = datetime.now().astimezone().strftime("%A, %d. %B %Y %H:%M:%S %Z")
    img_copy = img.copy()
    cv2.putText(
        img_copy,
        now,
        (10, 30),
        cv2.FONT_HERSHEY_PLAIN,
        1,
        (210, 155, 155),
        1,
        cv2.LINE_4,
    )
    return img_copy
