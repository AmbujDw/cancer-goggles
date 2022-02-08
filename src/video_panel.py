from PySide6.QtWidgets import QGridLayout, QWidget

from src.video_player import VideoPlayer


class VideoPanel(QWidget):
    def __init__(self, camera_0=None, camera_1=None):
        super().__init__()
        layout = QGridLayout()
        self.player_0 = VideoPlayer(camera_0)
        layout.addWidget(self.player_0, 0, 0)

        if camera_1 is not None:
            self.player_1 = VideoPlayer(camera_1)
            layout.addWidget(self.player_1, 0, 1)

        self.setLayout(layout)
