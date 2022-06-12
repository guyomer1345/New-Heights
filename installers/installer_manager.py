from installers.i_installer import IInstaller
from data_classes import Response
from typing import List

class InstallerManager:
    def __init__(self, installers: List[IInstaller], root_path: str):
        self.installers = installers
        self.root_path = root_path

    def install(self, id: str) -> Response:
        return[installer.install() for installer in self.installers if installer.id == id]

    def uninstall(self:str, id: str) -> None:
        [installer.uninstall() for installer in self.installers if installer.id == id]
