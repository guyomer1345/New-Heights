import os
from typing import Tuple, Dict

WORK_DIR = os.path.dirname(os.path.realpath(__file__))
DOWNLOADS_DIR = os.path.join(WORK_DIR, "downloads") + os.path.sep

SEVEN_ZIP_URL = "https://d3.7-zip.org/a/7z2107-x64.exe"
ANACONDA_URL = "https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe"

SEVEN_ZIP_INSTALL_COMMAND = '%s /S /D=%s'

JSON_CONTENT_TYPE = {'ContentType':'application/json'}
FILE_EXISTS = ' Already Exists'

