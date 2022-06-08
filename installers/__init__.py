from installers.installer_manager import InstallerManager


programs = [
    seven_zip_installer,
    python_zip_installer
]

manager = InstallerManager(
    # Programs
)

__all__ = [
    programs,
    manager,
    InstallerManager
]