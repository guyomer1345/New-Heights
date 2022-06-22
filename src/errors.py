class IInstallerErrors(Exception):
    """Base class for all IInstaller errors"""
    pass

class InstallerErrors(IInstallerErrors):
    """Base class for all errors occuring durring installation"""
    pass

class DownloadeErrors(IInstallerErrors):
    """Base class for all errors occuring durring downloading"""
    pass

class CriticalDownloadErrors(DownloadeErrors):
    """Base class for critical download errors """
    pass

class WarningDownloadErros(DownloadeErrors):
    """Base class for warning download errors"""
    pass

class CriticalInstallerErrors(InstallerErrors):
    """Base class for critical installing errors """
    pass

class WarningInstallerErros(InstallerErrors):
    """Base class for warning installing errors"""
    pass

class HTTPError(CriticalDownloadErrors):
    """Raise when there was an error downloading a file"""
    pass

class FileAlreadyDownloaded(WarningDownloadErros):
    """Raise when the file is already downloaded"""

class FileAlreadyInstalled(WarningInstallerErros):
    """Raise when the file is already installed"""
    pass

class ExeInstallerError(CriticalInstallerErrors):
    """Raise when there was an error with the exe installer error """
    pass

class InstallFailed(CriticalDownloadErrors):
    """Raise when the installer didnt show an error but the fill wasn't installed"""
    pass

class InvalidDownloadUrl(CriticalDownloadErrors):
    """Raise when the download url is invalid"""
    pass

class ExeUninstallerError(CriticalInstallerErrors):
    """Raise when the uninstaller failed"""
    pass

