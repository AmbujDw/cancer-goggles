from importlib import import_module
from importlib.util import find_spec

if find_spec("PySide6") is not None:
    target = "PySide6"
elif find_spec("PyQt5") is not None:
    target = "PyQt5"
else:
    raise RuntimeError("Cannot find PySide6 or PyQt5")
qt = import_module(target)
core = import_module(".QtCore", target)
widgets = import_module(".QtWidgets", target)
gui = import_module(".QtGui", target)
