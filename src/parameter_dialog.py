from src.ui import widgets
from src.parameter_item import ParameterItem


class ParameterDialog(widgets.QDialog):
    def __init__(self, parameters: dict):
        super().__init__()
        self.setWindowTitle("Edit Parameters")
        self.item_list = []
        for name, (low, high, step, default) in parameters.items():
            self.item_list.append(ParameterItem(name, low, high, step, default))
        btn_box = widgets.QDialogButtonBox(
            widgets.QDialogButtonBox.Ok | widgets.QDialogButtonBox.Cancel
        )
        btn_box.accepted.connect(self.accept)
        btn_box.rejected.connect(self.reject)

        layout = widgets.QVBoxLayout()
        for item in self.item_list:
            layout.addWidget(item)
        layout.addWidget(btn_box)
        self.setLayout(layout)

        self.values = self.collect_values()

    def change_value(self, value):
        self.label.setText(str(value))

    def collect_values(self):
        return [item.current_value for item in self.item_list]

    def accept(self):
        self.values = self.collect_values()
        super().accept()

    def reject(self):
        for i, item in enumerate(self.item_list):
            item.set_value(self.values[i])
        super().reject()
