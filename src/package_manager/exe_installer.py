from src.package_manager.i_installer import IInstaller
from src.errors import *
import subprocess
import tempfile
import requests
import logging
import socket
import shutil
import os

logging.basicConfig(level=logging.INFO)

class ExeInstaller(IInstaller):
    def __init__(self,  id, version, url, install_cmd, install_path) -> None:
        super().__init__(id, version)
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

    def  __download_file_with_errors(self, path) -> bool:
        """
        This function wraps the download_file function and adds error handling

        :param path: The path to download the exe to
        :return: Response object indicating whether the download was successful or not
        """
        try:
            self.__download_file(path=path)
        except CriticalDownloadErrors as e:
            logging.error(f"Couldn't download {self.id}: {e}")
            return False
        except WarningDownloadErros as e:
            logging.warning(f"Warning in downloading {self.id}: {e}")
        
        return True


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

    def __install_exe_with_errors(self, path) -> bool:
        """
        This functions wraps install_exe and handles errors
        :param path: The path to install the exe to
        :reutrn: Response object indicating whether the installalation was successful or not
        """
        try:
            self.__install_exe(path=path)
        except CriticalInstallerErrors as e:
            logging.error(e)
            return False

        except WarningInstallerErros as e:
            logging.warning(e)

        return  True

    def __find_uninstaller(self) -> str:
        for root, dirs, files in os.walk(self.install_path):
            for file in files:
                if 'uninstall' in file.lower() and 'exe' in file.lower():
                    return (os.path.join(root, file))
        
        raise(FileNotFoundError(f"Couldn't find the uninstaller for {self.id},"+
                                                f"try removing the following folder manually: {self.install_path}"))

    def __run_uninstaller(self, uninstaller) -> None:
        proc = subprocess.Popen(f'"{uninstaller}" /S',
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                        shell=True)

        out, err = proc.communicate()
        err = err.decode()

        shutil.rmtree(self.install_path, ignore_errors=True)
        if err or os.path.isdir(self.install_path):
            raise(ExeUninstallerError(f"Failed to uninstall {self.id}: {err}, "+
                                                     f"try removing the following folder manually: {self.install_path}"))

    def install(self) -> bool:
        """
        This functions downloads and installs a program

        :return: Response object indicaitng whether it succeeded or not
        """
        temp_dir = tempfile.TemporaryDirectory()
        path = os.path.join(temp_dir.name, f'{self.id}.exe')
        
        download_response = self.__download_file_with_errors(path = path)
        if not download_response:
            return download_response

        logging.info(f'Finished downloading {self.id}')


        install_response = self.__install_exe_with_errors(path = path)
        if not install_response:
            return install_response

        logging.info(f'Finsihed installing {self.id}')
        return install_response

    def uninstall(self) -> bool:
        try:
            uninstaller = self.__find_uninstaller()
        except FileNotFoundError as e:
            logging.error(e)
            return False
        
        try:
            self.__run_uninstaller(uninstaller)
        except ExeUninstallerError as e:
            logging.error(e)
            return False

        shutil.rmtree(self.install_path, ignore_errors=True)
        return True



        
        
