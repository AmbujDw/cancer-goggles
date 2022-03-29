from time import time

import cv2
import numpy as np

from src.algorithms.threshold import thresholding
from src.models import Camera
from src.ui import core, gui, widgets


def ndarray_to_qpixmap(img: np.ndarray) -> gui.QPixmap:
    if img.ndim == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    w, h, _ = img.shape
    qimg = gui.QImage(img.data, h, w, 3 * h, gui.QImage.Format_RGB888)
    return gui.QPixmap(qimg)


class VideoPlayer(widgets.QWidget):

    milliseconds_per_seconds = 1000

    def __init__(self, source=None):
        super().__init__()
        self.source = source
        self.video_interval = (
            int(self.milliseconds_per_seconds / self.source.fps)
            if self.source is Camera
            else 0
        )
        w, h = (
            self.source.resolution if isinstance(self.source, Camera) else (1280, 720)
        )

        layout = widgets.QVBoxLayout()

        self.image_view = widgets.QLabel()
        self.image_view.setAlignment(core.Qt.AlignVCenter)
        self.image_view.setFixedSize(w, h)
        layout.addWidget(self.image_view)

        self.goggle_view = widgets.QLabel()
        self.goggle_view.setFixedSize(w, h)
        self.goggle_view.hide()
        self.goggle_view.setWindowFlag(core.Qt.CustomizeWindowHint, True)
        self.goggle_view.setWindowFlag(core.Qt.WindowCloseButtonHint, False)

        self.default_fps_label = "0.00 FPS"
        self.fps_label = widgets.QLabel(self.default_fps_label)
        self.fps_label.setContentsMargins(5, 0, 5, 0)
        self.fps_label.setFixedSize(w * 0.1, h * 0.03)
        self.fps_label.setAlignment(core.Qt.AlignVCenter)
        layout.addWidget(self.fps_label)

        disable = True if self.source is None else False
        self.control_panel = VideoControlPanel(disable)
        layout.addWidget(self.control_panel)

        self.setLayout(layout)

        self.timer_video = core.QTimer()
        self.timer_video.timeout.connect(self.update_image)

        self.timer_fps = core.QTimer()
        self.timer_fps.timeout.connect(self.update_fps)

        self.curr_time = 1.0
        self.realtime_fps = 0.0
        self.frame_counter = 0

        self.black_frame = ndarray_to_qpixmap(np.ones((h, w, 3)))
        self.image_view.setPixmap(self.black_frame)

    def start_video(self):
        if not self.source.is_opened():
            return False
        self.timer_video.start(self.video_interval)
        self.timer_fps.start(self.milliseconds_per_seconds)
        return True

    def stop_video(self):
        self.timer_video.stop()
        self.timer_fps.stop()
        self.image_view.setPixmap(self.black_frame)
        self.fps_label.setText(self.default_fps_label)
        self.control_panel.cleanup()
        self.goggle_view.hide()

    def snapshot(self):
        self.source.snapshot(self.parent().parent().parent().root_path)

    def update_image(self):
        frame = self.source.get_frame()

        if self.control_panel.segmentation_on:
            frame = thresholding(frame)

        frame_pixmap = ndarray_to_qpixmap(frame)
        self.image_view.setPixmap(frame_pixmap)

        if self.control_panel.is_recording:
            self.source.write()

        goggle_view_visible = self.goggle_view.isVisible()
        if self.control_panel.project_to_goggle:
            if not goggle_view_visible:
                self.goggle_view.show()
            self.goggle_view.setPixmap(frame_pixmap)
        elif goggle_view_visible:
            self.goggle_view.hide()

        if self.frame_counter == 0:
            self.curr_time = time()

        self.frame_counter += 1

        if self.frame_counter == self.source.fps:
            self.realtime_fps = self.source.fps / (time() - self.curr_time)
            self.frame_counter = 0

    def update_fps(self):
        self.fps_label.setText(f"{self.realtime_fps:.2f} FPS")

    def video_writer_initialized(self):
        return self.source.is_initialized()

    def initialize_video_writer(self):
        self.source.initialize_video_writer(self.parent().parent().parent().root_path)

    def cleanup(self):
        self.stop_video()


class VideoControlPanel(widgets.QWidget):
    def __init__(self, disable=False):
        super().__init__()
        layout = widgets.QGridLayout()
        btn_start = widgets.QPushButton("Start")
        btn_start.clicked.connect(self.start)
        btn_start.setDisabled(disable)
        layout.addWidget(btn_start, 0, 0)

        btn_stop = widgets.QPushButton("Stop")
        btn_stop.clicked.connect(self.stop)
        btn_stop.setDisabled(disable)
        layout.addWidget(btn_stop, 0, 1)

        btn_snap = widgets.QPushButton("Snapshot")
        btn_snap.clicked.connect(self.snapshot)
        btn_snap.setDisabled(disable)
        layout.addWidget(btn_snap, 1, 0, 1, 2)

        self.cbx_record = widgets.QCheckBox("Record")
        self.cbx_record.stateChanged.connect(self.record)
        self.cbx_record.setDisabled(disable)
        layout.addWidget(self.cbx_record, 2, 0)

        self.cbx_goggle = widgets.QCheckBox("To Goggle")
        self.cbx_goggle.stateChanged.connect(self.to_goggle)
        self.cbx_goggle.setDisabled(disable)
        layout.addWidget(self.cbx_goggle, 2, 1)

        self.cbx_segmentation = widgets.QCheckBox("Segmentation")
        self.cbx_segmentation.stateChanged.connect(self.segmentation)
        self.cbx_segmentation.setDisabled(disable)
        layout.addWidget(self.cbx_segmentation, 3, 0)

        self.cbx_superimposed = widgets.QCheckBox("Superimposed")
        self.cbx_superimposed.stateChanged.connect(self.superimposed)
        self.cbx_superimposed.setDisabled(disable)
        layout.addWidget(self.cbx_superimposed, 3, 1)

        self.setLayout(layout)

        self.is_recording = False
        self.project_to_goggle = False
        self.segmentation_on = False
        self.superimposed_on = False

    def start(self):
        self.parent().start_video()

    def stop(self):
        self.parent().stop_video()
        self.cleanup()

    def snapshot(self):
        self.parent().snapshot()

    def record(self, state):
        self.is_recording = True if state == core.Qt.Checked else False
        if self.is_recording and not self.parent().video_writer_initialized():
            self.parent().initialize_video_writer()

    def to_goggle(self, state):
        self.project_to_goggle = True if state == core.Qt.Checked else False

    def segmentation(self, state):
        self.segmentation_on = True if state == core.Qt.Checked else False

    def superimposed(self, state):
        self.superimposed_on = True if state == core.Qt.Checked else False
        if self.superimposed_on and not self.segmentation_on:
            self.cbx_segmentation.click()

    def cleanup(self):
        if self.cbx_record.isChecked():
            self.cbx_record.click()
        if self.cbx_goggle.isChecked():
            self.cbx_goggle.click()
