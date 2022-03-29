from __future__ import annotations

from datetime import datetime
from enum import Enum
from platform import machine

import cv2

is_rpi = machine() == "armv7l"


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
