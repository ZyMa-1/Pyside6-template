"""
Author: ZyMa-1
"""

from PySide6.QtCore import Slot, QSettings
from PySide6.QtWidgets import QMainWindow
from src.backend.SettingsManager import SettingsManager
from src.ui.Ui_MainWindow import Ui_MainWindow
from src.widgets.AboutDialog import AboutDialog


class MainWindow(QMainWindow):
    """
    Main window of an application
    """

    def __init__(self):
        super().__init__()

        # Setup UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Create expected attributes
        self.settings: QSettings | None = None

        # Init UI
        self.create_helper_classes()
        self.init_ui()

        self.connect_signals_to_slots()

    def init_ui(self):
        pass

    @Slot()
    def handle_action_about_triggered(self):
        dialog = AboutDialog(self)
        dialog.setModal(True)
        dialog.show()

    # Init functions

    def create_helper_classes(self):
        # Create settings
        self.settings = SettingsManager().settings_instance()

    def connect_signals_to_slots(self):
        self.ui.action_about.triggered.connect(self.handle_action_about_triggered)
