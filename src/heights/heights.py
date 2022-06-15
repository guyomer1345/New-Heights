import json
import os

class Heights:
    def __init__(self, path: str, version: str):
        self.path = path
        self.version = version

    def __versiontuple(self, version: str) -> int:
        return tuple(map(int, (version.split("."))))

    def __is_old_version(self, current_version: str, latest_version: str) -> bool:
        return self.__versiontuple(current_version) > self.__versiontuple(latest_version)

    def is_installed(self) -> bool:
        if not os.path.exists(os.path.join(self.path, 'status.json')):
            return False
        
        return True
  
    def is_up_to_date(self) -> bool:
        if not self.is_installed():
            return False

        with open(os.path.join(self.path, 'status.json'), 'r') as f:
            status = json.loads(f.read())

        current_version = status['version']
        if self.__is_old_version(current_version, self.version):
            return False
        
        return True

    def install(self) -> None:

        status = {
            'is_installed': True,
            'version': self.version
        }

        with open(f'{self.path}/status.json', 'w') as f:
            f.write(json.dumps(status))

    def update() -> None:
        return NotImplementedError()