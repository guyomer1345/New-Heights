import os
from enum import Enum

WORK_DIR = os.path.dirname(os.path.realpath(__file__))
DOWNLOADS_DIR = os.path.join(WORK_DIR, "downloads") + os.path.sep
INSTALLATIONS_DIR = os.path.join(WORK_DIR, "system",
                                 "installations") + os.path.sep

# TODO: make ProgramDetails class, containing url, folder, command and name
class SevenZip(Enum):
    NAME = '7-Zip'
    URL = "https://d3.7-zip.org/a/7z2107-x64.exe"
    INSTALLATION_FOLDER = os.path.join(INSTALLATIONS_DIR, '7-Zip')
    INSTALL_COMMAND = f'"%s" /S /D={INSTALLATION_FOLDER}' 

class MiniConda(Enum):
    NAME = 'Miniconda'
    URL = "https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe"
    INSTALLATION_FOLDER = os.path.join(INSTALLATIONS_DIR, 'Miniconda3')
    INSTALL_COMMAND = 'start /wait "" "%s" /AddToPath=0 \
    /InstallationType=JustMe /RegisterPython=0 /S /D={installation_folder}' \
        .format(installation_folder=INSTALLATION_FOLDER)

JSON_CONTENT_TYPE = {'ContentType': 'application/json'}
SUCCESS = 'success'
MSG = 'msg'
HTTP_CODE = 'http_code'
FILE_EXISTS = ' Already Exists'
INSTALL_SUCCESS = 'Installed %s successfully'
ACCESS_DENIED = 'Access is denied.'