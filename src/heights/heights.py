import json
import os
import sys

class Heights:
    def __init__(self, version: str):
        self.id = "heights.exe"
        self.version = version
        self.path = os.getcwd()

    def __versiontuple(self, version: str) -> int:
        return tuple(map(int, (version.split("."))))

    def __is_old_version(self, current_version: str, latest_version: str) -> bool:
        return self.__versiontuple(current_version) > self.__versiontuple(latest_version)

    def is_installed(self) -> bool:
        if not os.path.exists(os.path.join(self.path, 'status.json')):
            return False
        
        return True

    def __copy_exe(self, install_path: str):
        with open(f'{self.path}/{self.id}', 'rb') as reader:
            data = reader.read()
        
        with open(f'{install_path}/{self.id}', 'wb') as writer:
            writer.write(data)

    def is_up_to_date(self) -> bool:
        if not self.is_installed():
            return False

        with open(os.path.join(self.path, 'status.json'), 'r') as f:
            status = json.loads(f.read())

        current_version = status['version']
        if self.__is_old_version(current_version, self.version):
            return False
        
        return True

    def install(self, install_path: str) -> None:
        self.__copy_exe(install_path)

        status = {
            'is_installed': True,
            'version': self.version
        }

        with open(f'{install_path}/status.json', 'w') as f:
            f.write(json.dumps(status))

        os.system(f'cd {install_path} && {self.id}')
        sys.exit()

    def update() -> None:
        return NotImplementedError()