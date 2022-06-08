import json
import os.path
import subprocess
from typing import Callable, Tuple
from data_classes import Response
from downloader.generic_downloader import download_program

from constants import FILE_EXISTS, DOWNLOADS_DIR, JSON_CONTENT_TYPE, SUCCESS, \
    MSG, INSTALL_SUCCESS


def install_program(program_name: str, installation_folder: str,
                    download_url: str,
                    install_command: str,
                    file_path: str,
                    version_checking_func: Callable = None):
    """
    Downloads and installs the program with the given parameters.

    :param program_name: The program's name
    :param installation_folder: the path to install the program to
    :param download_url: where to download it from
    :param install_command: how to install the program from the cli(silently)
    :param file_name: the name of the file
    :param version_checking_func: to be implemented, will check the version
    of the currently installed program(if found) and only install from
    download_url if it's a newer version.
    """
    # TODO: implement version checking
    if os.path.isdir(installation_folder):
        # TODO: change according to end handling
        return Response(True, program_name+FILE_EXISTS, 200, JSON_CONTENT_TYPE)

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

    msg =  INSTALL_SUCCESS % program_name if created_dir else error_msg
    status_code = 200 if created_dir else 500
    return Response(created_dir, msg, status_code, JSON_CONTENT_TYPE)
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

    print(f'out is {out}, err is {err}')

    if err:
        return False, err.decode().strip()

    return os.path.isdir(install_dir), out.decode()
