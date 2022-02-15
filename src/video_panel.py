from src.ui import widgets
from src.video_player import VideoPlayer


class VideoPanel(widgets.QWidget):
    def __init__(self, camera_0=None, camera_1=None):
        super().__init__()
        layout = widgets.QGridLayout()
        self.player_0 = VideoPlayer(camera_0)
        layout.addWidget(self.player_0, 0, 0)
        self.player_1 = VideoPlayer(camera_1)
        layout.addWidget(self.player_1, 0, 1)
        self.setLayout(layout)
