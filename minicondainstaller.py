import json
import os
from typing import Tuple,  Dict

from Constants import DOWNLOADS_DIR, MINICONDA_INSTALL_COMMAND, MINICONDA_INSTALLATION_FOLDER, MINICONDA_URL , FILE_EXISTS
from Utils import download_file_with_response


def download_miniconda() -> Tuple[str, int, Dict[str, str]]:
    return download_file_with_response(MINICONDA_URL)


def install_miniconda_from_executable(executable_path) -> bool:
    os.system(MINICONDA_INSTALL_COMMAND % executable_path)

    return os.path.isdir(MINICONDA_INSTALLATION_FOLDER)
    

def install_miniconda():
    # TODO: implement version checking miniconda, existence of folder shouldn't be blocking
    if os.path.isdir(MINICONDA_INSTALLATION_FOLDER):
        return print('7-Zip already installed')

    response = download_miniconda()

    if response[1] == 200:
        json_object = json.loads(response[0])
        file_path = json_object['msg']

        if FILE_EXISTS in file_path:
            print('File already exists, using local')
            file_path = file_path.replace(FILE_EXISTS, '')

        install_miniconda_from_executable(os.path.join(DOWNLOADS_DIR, file_path))

