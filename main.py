"""
Author: ZyMa-1
"""

import importlib
import os
import pathlib
import sys

from PySide6.QtCore import QTranslator, QLocale
from PySide6.QtWidgets import QApplication

from src.backend.PathManager import PathManager
from src.backend.SettingsManager import SettingsManager


# FOR DEBUGGING (to receive dumpObjectInfo output)
# def message_handler(mode, context, message):
#     print(message)
#
#
# qInstallMessageHandler(message_handler)


def ensure_if_ok_to_run():
    pass
    # Make any necessary directories here #


if __name__ == '__main__':
    ensure_if_ok_to_run()

    # Change to your MainWindow if necessary
    MainWindow = getattr(importlib.import_module('src.widgets.MainWindow'), 'MainWindow')

    app = QApplication(sys.argv)

    app.setOrganizationName("Set you name here")
    app.setApplicationName("Set you app name here")
    app.setApplicationVersion("Set app ver here")

    PathManager.set_project_root(pathlib.Path(__file__).absolute().parent)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
