import time
from typing import Union

import webview
import logging

from webview import Window

from src.package_manager.constants import *
import installers
from installers import InstallerManager

logging.basicConfig(level=logging.INFO)


def init():
    # TODO: cleanup the directory if exists
    if not os.path.isdir(DOWNLOADS_DIR):
        os.makedirs(DOWNLOADS_DIR)
    #TODO: Create packages.json


class Api:
    def __init__(self):
        self._window = None  # type: Union[Window, None]
        self._original_size = (400, 800)
        self.manager = InstallerManager(
            installers=[
                installers.seven_zip_installer,
                installers.miniconda_installer,
            ],
            root_path="./system/installations/"
        )

    def get_actions(self):
        return [
            {
                "id": "python",
                "actions": ["remove", "update"]
            },
            {
                "id": "7-zip",
                "actions": ["install"]
            },
            {
                "id": "miniconda",
                "actions": ["remove"]
            },
        ] * 4

    def check_update(self):
        pass


    def resize(self, height: int):
        width, _ = self._original_size
        self._window.resize(self._window.width, height)

    def get_status(self):
        time.sleep(3) # this sleep is here just for design purpose (remove on prod)
        status = self.manager.get_available()
        return status

    def execute_action(self, id: str, action: str):
        result = {
            "status": "OK"
        }
        print(f"Executing {action} on '{id}'")
        time.sleep(2)
        return result

    def set_windows(self, window: Window):
        self._window = window

    def close(self):
        self._window.destroy()


if __name__ == '__main__':
    init()

    api = Api()
    window = webview.create_window("Heights Install System",
                                   url="static/index.html",
                                   height=400,
                                   width=800,
                                   frameless = True,
                                   easy_drag = True,
                                   js_api=api,
                                   resizable=False
                                   )
    api.set_windows(window)
    webview.start(debug=True, http_server=True)
