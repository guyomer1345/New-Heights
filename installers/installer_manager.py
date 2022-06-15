from dataclasses import dataclass
from enum import Enum, auto

from installers.i_installer import IInstaller
from data_classes import Response
from typing import List, Dict, Any


@dataclass
class Package:
    id: str
    version: str

class ActionType(Enum):
    UPDATE = "update"
    INSTALL = "install"
    UNINSTALL = "uninstall"

@dataclass
class Action:
    type: ActionType
    package: Package

class InstallerManager:
    def __init__(self, installers: List[IInstaller], root_path: str):
        self.installers = installers
        self.root_path = root_path

    def get_installed_packages(self) -> List[Dict[str, Any]]:
        """
        returns the current installed packages
        """
        return None


    def get_recommended_packages(self) -> List[Dict[str, Any]]:
        """
        returns the recommended packages for heights
        """
        return [{
            "id": installer.id,
            "version": installer.version,
            "is_installed": False
        }
            for installer in self.installers
        ]

    def get_packages_actions(self) -> List:
        """
        Returns all the  available actions for current user (un/install, update)
        """
        return []

    def execute_action(self, id: str, action: ActionType):
        """
        Execute an action
        """
        pass

    def install(self, id: str) -> Response:
        return [installer.install() for installer in self.installers if installer.id == id]

    def uninstall(self: str, id: str) -> None:
        [installer.uninstall() for installer in self.installers if installer.id == id]
