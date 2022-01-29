import os
from typing import Tuple, Dict

WORK_DIR = os.path.dirname(os.path.realpath(__file__))
DOWNLOADS_DIR = os.path.join(WORK_DIR, "downloads") + os.path.sep
INSTALLATIONS_DIR = os.path.join(WORK_DIR, "system", "installations") + os.path.sep

SEVEN_ZIP_URL = "https://d3.7-zip.org/a/7z2107-x64.exe"
ANACONDA_URL = "https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe"

SEVEN_ZIP_INSTALLATION_FOLDER = os.path.join(INSTALLATIONS_DIR, '7-Zip')
SEVEN_ZIP_INSTALL_COMMAND = '%s /S /D={installation_folder}'.format(installation_folder=SEVEN_ZIP_INSTALLATION_FOLDER)

JSON_CONTENT_TYPE = {'ContentType':'application/json'}
FILE_EXISTS = ' Already Exists'

