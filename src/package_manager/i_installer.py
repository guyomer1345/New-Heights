import abc


class IInstaller(abc.ABC):
    def __init__(self, id: str, version: str):
        self.id = id
        self.version = version

    def install(path: str):
        pass

    def uninstall(path: str):
        pass


