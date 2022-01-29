import json
import os

from Constants import *
from Utils import download_file_with_response


def download_7zip() -> Tuple[str, int, Dict[str, str]]:
    return download_file_with_response(SEVEN_ZIP_URL)


def install_7zip_from_executable(executable_path: str):
    os.system(SEVEN_ZIP_INSTALL_COMMAND % executable_path)

    return os.path.isdir(SEVEN_ZIP_INSTALLATION_FOLDER)


def install_7zip():
    # TODO: implement version checking of 7-zip, existence of folder shouldn't be blocking
    if os.path.isdir(SEVEN_ZIP_INSTALLATION_FOLDER):
        return print('7-Zip already installed')

    response = download_7zip()

    if response[1] == 200:
        json_object = json.loads(response[0])
        file_path = json_object['msg']

        if FILE_EXISTS in file_path:
            print('File already exists, using local')
            file_path = file_path.replace(FILE_EXISTS, '')

        install_7zip_from_executable(os.path.join(DOWNLOADS_DIR, file_path))

# TODO:
#  add call to install_7zip

# FIXME: silent extraction of files
#   os.environ['PATH'] += ';%s' % SEVEN_ZIP_INSTALLATION_FOLDER
#   print('\n'.join(os.environ['PATH'].split(';')))
#   os.popen('7z x -y TelegramDesktopPortable_3.4.8.paf.exe -o%s' % os.path.join(INSTALLATIONS_DIR, 'TelegramPortable'))

