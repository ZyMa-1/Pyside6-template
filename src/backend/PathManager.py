"""
Author: ZyMa-1
"""

import pathlib


class PathManager:
    """Class for storing paths."""
    PROJECT_ROOT = None
    SETTINGS_INI = None

    @classmethod
    def set_project_root(cls, path: pathlib.Path):
        cls.PROJECT_ROOT = path
        cls.SETTINGS_INI = cls.PROJECT_ROOT / "settings.ini"
