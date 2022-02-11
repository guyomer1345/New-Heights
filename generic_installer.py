import json
import os.path
import subprocess
from typing import Callable, Tuple, Dict

from constants import FILE_EXISTS, DOWNLOADS_DIR, JSON_CONTENT_TYPE, SUCCESS, \
    MSG, INSTALL_SUCCESS
from utils import download_file_with_response


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
        return json.dumps({SUCCESS: True,
                           MSG: program_name + FILE_EXISTS}), 200, \
               JSON_CONTENT_TYPE

    response = download_program(download_url)

    # TODO: make less 'magic number-y', make response object and stuff
    if response[1] == 200:
        json_object = json.loads(response[0])
        file_path = json_object[MSG]

        if FILE_EXISTS in file_path:
            # change to logging.debug/send to another endpoint?
            print('File already exists, using local')  # assuming version check
            file_path = file_path.replace(FILE_EXISTS, '')

        created_dir, error_msg = install_program_from_executable(
            install_command,
            installation_folder,
            os.path.join(
                DOWNLOADS_DIR,
                file_path))

        return json.dumps({SUCCESS: created_dir,
                           MSG: INSTALL_SUCCESS % program_name if created_dir
                           else error_msg}), 200 if created_dir else 500, \
               JSON_CONTENT_TYPE

    return response

    # TODO: add handling of success and failure


def install_program_from_executable(install_command: str, install_dir: str,
                                    executable_path: str) -> Tuple[bool, str]:
    """
    Runs the installation command and returns whether the folder was created
    or not.

    :param install_command: the command to run with the installation executable
    :param install_dir: where the output should be
    :param executable_path: the path of the executable
    :return: whether the folder was created or not.
    """
    # TODO: add error handling
    proc = subprocess.Popen(install_command % executable_path,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            shell=True)

    out, err = proc.communicate()

    print(out, err)

    if err:
        return False, err.decode().strip()

    return os.path.isdir(install_dir), out.decode()
