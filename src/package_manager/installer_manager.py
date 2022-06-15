from src.package_manager.i_installer import IInstaller
from typing import List, Tuple
from dataclasses import dataclass
from typing import Dict, Any
from enum import Enum
import json

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
        with open(f'{self.root_path}/packages.json', 'r') as f:
            installed_packages = json.loads(f.read())
        
        return installed_packages['installed_packages']

    def __update_installed_packages_json(self, installed_packages: List[Dict[str, str]]) -> None:
        with open(f'{self.root_path}/packages.json', 'w') as f:
            f.write(json.dumps(installed_packages))

    def __add_package(self, installed_packages: str, current_package: Package) -> None:
        installed_packages['installed_packages'].append({"id": current_package.id, 
                                                                                        "version": current_package.version})

    def __remove_package(self, installed_packages: str, current_package: Package) -> None:
        for package in installed_packages['installed_packages']:
            if package['id'] == current_package.id:
                installed_packages['installed_packages'].remove(package)
                self.__update_installed_packages_json(installed_packages)

    def __update_package(self, installed_packages: str, current_package: Package) -> None:
        for package in installed_packages['installed_packages']:
            if package['id'] == current_package.id:
                package['version'] = current_package.version
                self.__update_installed_packages_json(installed_packages)

    def __versiontuple(self, version: str) -> Tuple[int]: 
        return tuple(map(int, (version.split("."))))
    
    def  __get_package(self, id: str, packages:  List[Dict[str, str]]) -> Dict[str, str]:
        return [package for package in packages if package['id'] == id]

    def __is_older_version(self, current_version: str, latest_version: str) -> bool:
        return self.__versiontuple(current_version) < self.__versiontuple(latest_version)

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
        Returns all the available actions for current user (un/install, update)
        """
        actions = []
        recommended_packages = self.get_recommended_packages()
        installed_packages = self.get_installed_packages()

        for package in recommended_packages:
            if not self.__get_package(package['id'], installed_packages):
                actions.append((package['id'], [ActionType.INSTALL]))
            
            if self.__get_package(package['id'], installed_packages):
                available_actions = [ActionType.UNINSTALL]
                current_package = self.__get_package(package['id'], installed_packages)[0]
                if self.__is_older_version(current_package['version'], package['version']):
                    available_actions.append(ActionType.UPDATE)
                
                actions.append((package['id'], available_actions))
            
        return actions

    def execute_action(self, id: str, action: ActionType):
        """
        Execute an action
        """
        pass


