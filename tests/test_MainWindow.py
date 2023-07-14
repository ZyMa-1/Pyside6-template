import os
import pathlib
import sys
import tempfile
import unittest
from typing import ClassVar

from PySide6.QtCore import QLocale, QTranslator, QSettings
from PySide6.QtWidgets import QApplication

from src.backend.PathManager import PathManager
from src.backend.SettingsManager import SettingsManager
from src.widgets.MainWindow import MainWindow


def create_app():
    app = QApplication(sys.argv)

    app.setOrganizationName("Set you name here")
    app.setApplicationName("Set you app name here")
    app.setApplicationVersion("Set app ver here")

    PathManager.set_project_root(pathlib.Path(__file__).absolute().parent)

    return app


class MainWindowTest(unittest.TestCase):
    """Tests the MainWidget GUI."""
    app: ClassVar[QApplication | None] = None
    settings_temp_file_path: ClassVar[pathlib.Path | None] = None
    temp_dir: ClassVar[tempfile.TemporaryDirectory | None] = None
    settings: ClassVar[QSettings | None] = None

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()

        cls.temp_dir = tempfile.TemporaryDirectory(prefix="specify dir path here")
        cls.settings_temp_file_path = PathManager.PROJECT_ROOT / 'settings.ini'

        cls.settings = SettingsManager(parent=cls.app).settings_instance()
        lang = cls.settings.value("Language", "en", type=str)
        if lang == "ru":
            lang = QLocale.Language.Russian
        elif lang == "en":
            lang = QLocale.Language.English

        # Initialize translations using resource file
        translator = QTranslator(cls.app)
        path = ':/translations'
        if translator.load(lang, 'main_gui', '_', path):
            cls.app.installTranslator(translator)

    def setUp(self):
        self.main_window = MainWindow()

    def tearDown(self):
        del self.main_window

    @classmethod
    def tearDownClass(cls):
        cls.temp_dir.cleanup()
        try:
            os.remove(str(cls.settings_temp_file_path))
        except FileNotFoundError:
            pass

    def test_some_shit(self):
        pass


def suite():
    """Create a test suite."""
    test_suite = unittest.TestSuite()
    test_suite.addTest(MainWindowTest('main_window_test'))
    return test_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
