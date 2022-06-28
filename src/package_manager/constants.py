import os
from enum import Enum, EnumMeta
import sys

WORK_DIR = os.getcwd()
INSTALLATIONS_DIR = os.path.join(WORK_DIR, 
                                 "installations") + os.path.sep

class Apps(Enum):
    class MiniConda(EnumMeta):
        APP_NAME = 'Miniconda'
        INSTALLATION_FOLDER = os.path.join(INSTALLATIONS_DIR, 'Miniconda3')
        URL = "https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe"
        INSTALL_COMMAND = 'start /wait "" "%s" /AddToPath=0 \
        /InstallationType=JustMe /RegisterPython=0 /S /D={installation_folder}' \
            .format(installation_folder=INSTALLATION_FOLDER)
            

    class SevenZip(EnumMeta):
        APP_NAME = '7-Zip'
        URL = "https://d3.7-zip.org/a/7z2107-x64.exe"
        INSTALLATION_FOLDER = os.path.join(INSTALLATIONS_DIR, '7-Zip')
        INSTALL_COMMAND = f'"%s" /S /D="{INSTALLATION_FOLDER}"' 