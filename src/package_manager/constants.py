import os
from enum import Enum, EnumMeta

WORK_DIR = os.path.dirname(os.path.realpath(__file__))
DOWNLOADS_DIR = os.path.join(WORK_DIR, "../../downloads") + os.path.sep
INSTALLATIONS_DIR = os.path.join(WORK_DIR, "system",
                                 "installations") + os.path.sep
JSON_CONTENT_TYPE = {'ContentType': 'application/json'}
SUCCESS = 'success'
MSG = 'msg'
HTTP_CODE = 'http_code'
FILE_EXISTS = ' Already Exists'
INSTALL_SUCCESS = 'Installed %s successfully'
ACCESS_DENIED = 'Access is denied.'

# TODO: make ProgramDetails class, containing url, folder, command and name
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

class StatusCodes(Enum):
    OK = 200
    INTERNAL_SERVER_ERROR = 500