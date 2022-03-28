from platform import machine
from importlib import import_module

is_rpi = machine() == "armv7l"

gui_framework = "PyQt5" if is_rpi else "PySide6"

qt = import_module(gui_framework)
core = import_module(".QtCore", gui_framework)
widgets = import_module(".QtWidgets", gui_framework)
gui = import_module(".QtGui", gui_framework)
