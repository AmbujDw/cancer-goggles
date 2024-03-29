from pathlib import Path

from src.meta_dialog import MetaDialog
from src.parameter_dialog import ParameterDialog
from src.parameters import parameters
from src.ui import widgets
from src.video_panel import VideoPanel

milliseconds_per_seconds = 1000


class StartWindow(widgets.QMainWindow):
    def __init__(self, camera=(None, None)):
        super().__init__()
        self.setWindowTitle("Cancer Vision")
        self.resize(1280, 720)

        self.root_path = Path(__file__).parent.parent
        self.parameters = parameters
        self.parameters_value = [value for _, _, _, value in parameters.values()]

        self.central_widget = widgets.QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = widgets.QGridLayout(self.central_widget)

        self.btn_meta_info = widgets.QPushButton(
            "Edit Surgery Info", self.central_widget
        )
        self.btn_meta_info.clicked.connect(self.enter_meta_info)
        self.layout.addWidget(self.btn_meta_info, 0, 0)

        self.btn_directory = widgets.QPushButton(
            "Select Main Directory", self.central_widget
        )
        self.btn_directory.clicked.connect(self.select_directory)
        self.layout.addWidget(self.btn_directory, 0, 1)

        self.btn_parameters = widgets.QPushButton("Set Parameters", self.central_widget)
        self.btn_parameters.clicked.connect(self.set_parameters)
        self.layout.addWidget(self.btn_parameters, 0, 2)

        self.panel = VideoPanel(*camera)
        self.layout.addWidget(self.panel, 2, 0, 1, 3)

        self._create_status_bar()

    def _create_status_bar(self):
        self.statusbar = self.statusBar()
        self.statusbar.setContentsMargins(10, 0, 10, 0)

        self.user_name_label = widgets.QLabel("User Name: test_user")
        self.user_name_label.setContentsMargins(5, 0, 5, 0)
        self.statusbar.addPermanentWidget(self.user_name_label)

        self.patient_name_label = widgets.QLabel("Patient ID: test_patient")
        self.patient_name_label.setContentsMargins(5, 0, 5, 0)
        self.statusbar.addPermanentWidget(self.patient_name_label)

        self.surgery_type_label = widgets.QLabel("Surgery Type: test_surgery")
        self.surgery_type_label.setContentsMargins(5, 0, 5, 0)
        self.statusbar.addPermanentWidget(self.surgery_type_label)

        self.path_label = widgets.QLabel(f"Main Directory: {self.root_path}")
        self.path_label.setContentsMargins(5, 0, 5, 0)
        self.statusbar.addPermanentWidget(self.path_label)

    def enter_meta_info(self):
        meta_info_dialog = MetaDialog()
        if meta_info_dialog.exec_():
            self.user_name_label.setText(f"User Name: {meta_info_dialog.user_name}")
            self.patient_name_label.setText(
                f"Patient ID: {meta_info_dialog.patient_id}"
            )
            self.surgery_type_label.setText(
                f"Surgery Type: {meta_info_dialog.surgery_type.name}"
            )

    def select_directory(self):
        directory_dialog = widgets.QFileDialog()
        directory_dialog.setFileMode(widgets.QFileDialog.Directory)
        if directory_dialog.exec_():
            directory = directory_dialog.selectedFiles()[0]
            self.path_label.setText(f"Main Directory: {directory}")
            self.root_path = Path(directory)

    def set_parameters(self):
        param = ParameterDialog(parameters)
        if param.exec_():
            self.parameters_value = param.values

    def closeEvent(self, event):
        msg = "Close the app?"
        reply = widgets.QMessageBox.question(
            self, "Message", msg, widgets.QMessageBox.Yes, widgets.QMessageBox.No
        )

        if reply == widgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
