# Cancer-Goggles
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

## Desktop Setup
Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html), and update conda base environment:
```shell
conda update conda
```

Create and activate the development environment:
```shell
conda create -f environment.yml
conda activate goggles-dev
```

See the official [documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) 
for how to manage conda environments. 

Install the App
```shell
python -m pip install -e .
```

## Raspberry Pi Setup (only on Buster for now)

Qt has limited support for Arm devices. The only pre-build Qt library for Python on Pi is available via `apt`. 

The following might not be the optimal solution. But it works for now.

Update firmware
```shell
sudo rpi-update
sudo reboot
```

Setup the Camera Module following the [Offical Guide](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera).

Update packages and install PyQt5
```shell
sudo apt update
sudo apt upgrade
sudo apt install python3-pyqt5
```

Create and activate a virtualenv. See [venv](https://docs.python.org/3/library/venv.html) for details.
Since we installed pyqt5 at the system level, we need the `--system-site-packages` flag to give venv the access.
```shell
python3 -m venv ~/virtualenvs/goggles-dev --system-site-packages
. ~/virtualenvs/goggles-dev/bin/activate
```

Inside the `goggles-dev` environment, install dependencies
```shell
pip install -U pip setuptools wheel
pip install -U numpy opencv-python-headless scikit-image
```

## Start the GUI
With the `goggles-dev` environment activated and inside of the project directory
```shell
python -m src
```
Or if the app is installed in the environment, you can simply do
```shell
goggles
```

## QT Python Bindings
There are two Python bindings for Qt: PyQT and PySide. We currently use PyQt5 on Raspberry Pi since it's available via `apt`. On other platforms, we use PySide6 since it has pre-build wheels available via `pip` for the Apple M1 machine. The app has a compatibility shim that would try to import PySide6 first; if not found, then import PyQt5. The app would work as long as either one of those packages is available in the virtual environment.
