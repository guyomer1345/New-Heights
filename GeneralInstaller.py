import json
import os.path
from typing import Callable, Tuple, Dict

from Constants import FILE_EXISTS, DOWNLOADS_DIR, JSON_CONTENT_TYPE
from Utils import download_file_with_response


def download_program(url: str) -> Tuple[str, int, Dict[str, str]]:
    """
    Attempts to download the program from the given url

    :param url: the program's installer's url
    :return: a response object according to the results of the download
    """
    return download_file_with_response(url)


def install_program(program_name: str, installation_folder: str,
                    download_url: str,
                    install_command: str,
                    version_checking_func: Callable = None):
    """
    Downloads and installs the program with the given parameters.

    :param program_name: The program's name
    :param installation_folder: the path to install the program to
    :param download_url: where to download it from
    :param install_command: how to install the program from the cli(silently)
    :param version_checking_func: to be implemented, will check the version
    of the currently installed program(if found) and only install from
    download_url if it's a newer version.
    """
    # TODO: implement version checking
    if os.path.isdir(installation_folder):
        # TODO: change according to end handling
        return json.dumps({'success': True,
                           'msg': program_name + ' Already Installed'}), 200,\
               JSON_CONTENT_TYPE

    response = download_program(download_url)

    # TODO: make less 'magic number-y', make response object and stuff
    if response[1] == 200:
        json_object = json.loads(response[0])
        file_path = json_object['msg']

        if FILE_EXISTS in file_path:
            print('File already exists, using local')  # assuming version check
            file_path = file_path.replace(FILE_EXISTS, '')

        install_program_from_executable(install_command, installation_folder,
                                        os.path.join(DOWNLOADS_DIR, file_path))

    return response

        # TODO: add handling of success and failure


def install_program_from_executable(install_command: str, install_dir: str,
                                    executable_path: str) -> bool:
    """
    Runs the installation command and returns whether the folder was created
    or not.

    :param install_command: the command to run with the installation executable
    :param install_dir: where the output should be
    :param executable_path: the path of the executable
    :return: whether the folder was created or not.
    """
    # TODO: add error handling
    os.system(install_command % executable_path)

    return os.path.isdir(install_dir)
