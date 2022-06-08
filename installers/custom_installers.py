from enum import Enum, EnumMeta
from constants import MiniConda, SevenZip
from installers.generic_installer import install_program

def install_miniconda():
    return install_program(MiniConda.NAME.value, MiniConda.INSTALLATION_FOLDER.value,
                           MiniConda.URL.value, MiniConda.INSTALL_COMMAND.value, 'Miniconda3-latest-Windows-x86_64.exe') # Change to get from response


def install_7zip():
    return install_program(SevenZip.NAME.value, SevenZip.INSTALLATION_FOLDER.value,
                           SevenZip.URL.value, SevenZip.INSTALL_COMMAND.value, '7z2107-x64.exe') # Change to get from response


class AppUrls(Enum):
    class Miniconda(EnumMeta):
        app_name = 'Miniconda'
        installer = install_miniconda

    class SevenZip(EnumMeta):
        app_name = '7-Zip'
        installer = install_7zip