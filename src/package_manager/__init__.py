from src.package_manager.installer_manager import InstallerManager
from src.package_manager.exe_installers import seven_zip_installer, miniconda_installer
from src.package_manager.constants import INSTALLATIONS_DIR

programs = [
    seven_zip_installer,
    miniconda_installer
]

manager = InstallerManager(
    programs,
    INSTALLATIONS_DIR
)

__all__ = [
    programs,
    manager,
    InstallerManager
]
