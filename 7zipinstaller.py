import json

from Constants import *
from Utils import download_file


def download_7zip() -> Tuple[str, int, Dict[str, str]]:
    return download_file(SEVEN_ZIP_URL)


def install_7zip(file_path: str):
    os.system('conda activate py3; ' + SEVEN_ZIP_URL % (file_path, DOWNLOADS_DIR + r'\7-Zip'))


def download_and_install():
    response = download_7zip()

    if response[1] == 200:
        json_object = json.load(response[0])
        file_path = json_object['msg']

        if FILE_EXISTS in file_path:
            file_path = file_path.replace(FILE_EXISTS, '')

        install_7zip(file_path)

download_and_install()

