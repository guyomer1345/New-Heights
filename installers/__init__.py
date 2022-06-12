from installers.installer_manager import InstallerManager
from installers.exe_installers import seven_zip_installer, miniconda_installer
from constants import DOWNLOADS_DIR

programs = [
    seven_zip_installer,
    miniconda_installer
]

manager = InstallerManager(
    programs,
    DOWNLOADS_DIR
)

__all__ = [
    programs,
    manager,
    InstallerManager
]
