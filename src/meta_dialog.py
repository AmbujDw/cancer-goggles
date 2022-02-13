from src.ui import widgets
from src.utils import Surgery


class MetaDialog(widgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Surgery Information")
        self.form_group_box = widgets.QGroupBox("User Info")
        layout = widgets.QFormLayout()

        self.user_name = "test_user"
        self.patient_id = "test_patient"
        self.surgery_type = Surgery.Test

        self.user_name_line = widgets.QLineEdit()
        layout.addRow(widgets.QLabel("User Name:"), self.user_name_line)

        self.patient_id_line = widgets.QLineEdit()
        layout.addRow(widgets.QLabel("Patient ID:"), self.patient_id_line)

        surgery_types = [name for name, _ in Surgery.__members__.items()]
        self.surgery_types_box = widgets.QComboBox()
        self.surgery_types_box.addItems(surgery_types)
        layout.addRow(widgets.QLabel("Surgery Type:"), self.surgery_types_box)

        self.form_group_box.setLayout(layout)

        btn_box = widgets.QDialogButtonBox(
            widgets.QDialogButtonBox.Ok | widgets.QDialogButtonBox.Cancel
        )
        btn_box.accepted.connect(self.accept)
        btn_box.rejected.connect(self.reject)

        main_layout = widgets.QVBoxLayout()
        main_layout.addWidget(self.form_group_box)
        main_layout.addWidget(btn_box)
        self.setLayout(main_layout)

    def accept(self):
        if self.user_name_line.text() != "":
            self.user_name = self.user_name_line.text()
        if self.patient_id_line.text() != "":
            self.patient_id = self.patient_id_line.text()
        self.surgery_type = Surgery[self.surgery_types_box.currentText()]
        super().accept()
