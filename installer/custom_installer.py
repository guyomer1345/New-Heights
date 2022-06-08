from installer import install_program
from constants import Apps


def install_miniconda():
    return install_program(Apps.MiniConda.value.APP_NAME, Apps.MiniConda.value.INSTALLATION_FOLDER,
                           Apps.MiniConda.value.URL, Apps.MiniConda.value.INSTALL_COMMAND, 'Miniconda3-latest-Windows-x86_64.exe') # Change to get from response


def install_7zip():
    return install_program(Apps.SevenZip.value.APP_NAME, Apps.SevenZip.value.INSTALLATION_FOLDER,
                           Apps.SevenZip.value.URL, Apps.SevenZip.value.INSTALL_COMMAND, '7z2107-x64.exe') # Change to get from response
