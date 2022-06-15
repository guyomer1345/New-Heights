from src.package_manager.i_installer import IInstaller
from src.errors import *
import subprocess
import requests
import logging
import socket
import os

logging.basicConfig(level=logging.INFO)

class ExeInstaller(IInstaller):
    def __init__(self, download_path, id, version, url, install_cmd, install_path) -> None:
        super().__init__(id, version)
        self.download_path = download_path
        self.url = url
        self.install_cmd = install_cmd
        self.install_path = install_path


    def __download_file(self, path)  -> None:
        """
        This functions tries to download an exe

        :param path: The path to download the exe to
        :raise FileAlreadyDownladed: Raises when the file already exists
        :raise HTTPError: Raises when there was an error in the download
        :raise InvalidDownloadUrl: Raises when a connection wasn't established to the url
        :return: None
        """
        if os.path.exists(path):
            raise(FileAlreadyDownloaded(f"Already downloaded {self.id}"))

        try:
            with requests.get(self.url, stream=True) as r:
                r.raise_for_status()
                with open(path , 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
        except requests.exceptions.HTTPError as e:
            raise(HTTPError(e))
        except socket.error as e:
            raise(InvalidDownloadUrl(e))

    def  __download_file_with_errors(self, path) -> Response:
        """
        This function wraps the download_file function and adds error handling

        :param path: The path to download the exe to
        :return: Response object indicating whether the download was successful or not
        """
        try:
            self.__download_file(path=path)
        except CriticalDownloadErrors as e:
            logging.error(f"Couldn't download {self.id}: {e}")
            return Response(False, str(e),
                                StatusCodes.INTERNAL_SERVER_ERROR.value, JSON_CONTENT_TYPE)

        except WarningDownloadErros as e:
            logging.warning(f"Warning in downloading {self.id}: {e}")
        
        return  Response(True, SUCCESS, StatusCodes.OK.value, JSON_CONTENT_TYPE)


    def __install_exe(self, path) -> None:
        """
        This functions tries to install an exe

        :param path: The path to install the exe to
        :raise FileAlreadyInstalled: Raises when the path to install the exe already exists
        :raise ExeInstallerError: Raises when the installer returns an error
        :raise InstallFailed: Raises when the installer finished but the folder doesn't exsist
        :return: None
        """
        if os.path.exists(self.install_path):
            raise(FileAlreadyInstalled(f'{self.id} aready installed.'))

        proc = subprocess.Popen(self.install_cmd % path,
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                        shell=True)

        out, err = proc.communicate()
        err = err.decode()

        if err:
            raise(ExeInstallerError(f"Failed to install {self.id}: {err}"))

        if not os.path.exists(self.install_path):
            raise(InstallFailed(f"Failed to install {self.id}: {err}"))

    def __install_exe_with_errors(self, path) -> Response:
        """
        This functions wraps install_exe and handles errors
        :param path: The path to install the exe to
        :reutrn: Response object indicating whether the installalation was successful or not
        """
        try:
            self.__install_exe(path=path)
        except CriticalInstallerErrors as e:
            logging.error(e)
            return Response(False, str(e), 
                                StatusCodes.INTERNAL_SERVER_ERROR.value, JSON_CONTENT_TYPE)

        except WarningInstallerErros as e:
            logging.warning(e)

        return  Response(True, SUCCESS, StatusCodes.OK.value, JSON_CONTENT_TYPE)

    def install(self) -> Response:
        """
        This functions downloads and installs a program

        :return: Response object indicaitng whether it succeeded or not
        """
        path = os.path.join(self.download_path, f'{self.id}.exe')
        
        download_response = self.__download_file_with_errors(path = path)
        if not download_response.success_status:
            return download_response

        logging.info(f'Finished downloading {self.id}')


        install_response = self.__install_exe_with_errors(path = path)
        if not install_response.success_status:
            return install_response

        logging.info(f'Finsihed installing {self.id}')
        return install_response

    def uninstall(self):
       pass