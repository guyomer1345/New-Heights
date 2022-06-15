import time
from typing import Union, List, Dict, Any

from flask import Flask, request
import webview
import threading
import sys
import random
import string
import logging

from webview import Window

import installers
from constants import *
import installers
from installers import InstallerManager
from installers.exe_installer import ExeInstaller

logging.basicConfig(level=logging.INFO)


def init():
    # TODO: cleanup the directory if exists
    if not os.path.isdir(DOWNLOADS_DIR):
        os.makedirs(DOWNLOADS_DIR)


def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for _ in range(
        length)))

    return result_str


app = Flask(__name__, static_url_path='')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


# @app.route('/')
# def hello_world():
#     return app.send_static_file('register.html')


# def start_server():
#     app.run(host='127.0.0.1', port=54321)


# @app.route('/install')
# def download():
#     app_name = request.args.get('name', '')
#     installers.manager.install(app_name)


# @app.after_request
# def add_header(response):
#     """
#     Add headers to both force latest IE rendering engine or Chrome Frame,
#     and also to cache the rendered page for 10 minutes.
#     """
#     response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
#     response.headers["Pragma"] = "no-cache"
#     response.headers["Expires"] = "1"
#     response.headers['Cache-Control'] = 'public, max-age=0'
#
#     return response
#

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
                "actions": ["uninstall", "update"]
            },
            {
                "id": "7-zip",
                "actions": ["install"]
            },
            {
                "id": "miniconda",
                "actions": ["uninstall"]
            },
        ]

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
