from pathlib import Path
from queue import Queue
from threading import Thread
from time import time

import cv2

from src.utils import to_timestamped_frame


def format_gst_str(resolution, fps: int):
    width, height = resolution
    return f"libcamerasrc ! video/x-raw, width={width}, height={height}, framerate={fps}/1 ! videoconvert ! videoscale ! autovideosink"


class Camera:
    def __init__(self, cam_num, resolution, fourcc, fps, timestamped=False):
        self.cam_num = cam_num
        self.resolution = resolution
        self.fps = fps
        self.timestamped = timestamped

        self.cap = cv2.VideoCapture(self.cam_num)
        self.fourcc = cv2.VideoWriter_fourcc(*fourcc)
        self.video_writer = None
        self.last_frame = None
        self.last_timestamp = None
        self.video_queue = Queue()
        self.video_thread = Thread(target=self._video_writer_worker, daemon=True)
        self.pipeline = None

    def is_opened(self):
        return self.cap.isOpened()

    def open(self):
        cam_id = self.cam_num if self.pipeline is None else self.pipeline
        self.cap.open(cam_id)

    def close(self):
        self.video_queue.join()
        if self.video_writer is not None:
            self.video_writer.release()
        self.cap.release()

    def setup_gst_pipeline(self):
        self.pipeline = format_gst_str(self.resolution, self.fps)
        print(self.pipeline)
        self.cap = cv2.VideoCapture(self.pipeline, cv2.CAP_GSTREAMER)
        print(self.is_opened())

    def get_frame(self):
        if not self.is_opened():
            self.open()
        ret, video_frame = self.cap.read()
        if ret:
            self.last_frame = video_frame
            self.last_timestamp = int(time())
        return self.last_frame

    def initialize_video_writer(self, root_path):
        folder_path = Path(root_path, "video")
        if not folder_path.exists():
            folder_path.mkdir()
        video_path = Path(folder_path, f"record_{self.cam_num}_{int(time())}.avi")
        self.video_writer = cv2.VideoWriter(
            str(video_path), self.fourcc, self.fps, self.resolution
        )
        self.video_thread.start()

    def is_initialized(self):
        return self.video_writer is not None

    def write(self):
        self.video_queue.put(
            to_timestamped_frame(self.last_frame)
            if self.timestamped
            else self.last_frame
        )

    def _video_writer_worker(self):
        while True:
            frame = self.video_queue.get()
            self.video_writer.write(frame)
            self.video_queue.task_done()

    def snapshot(self, root_path):
        snapshot_thread = Thread(
            target=self._snapshot_thread_function,
            args=(root_path, self.cam_num, self.last_frame, self.last_timestamp),
            daemon=True,
        )
        snapshot_thread.run()

    @staticmethod
    def _snapshot_thread_function(root_path, cam_num, frame, timestamp):
        folder_path = Path(root_path, f"image_{cam_num}")
        if not folder_path.exists():
            folder_path.mkdir()
        snapshot_path = Path(folder_path, f"{timestamp}.jpg")
        cv2.imwrite(str(snapshot_path), frame)

    def __del__(self):
        self.close()

    def __str__(self):
        return f"OpenCV Camera {self.cam_num}"
