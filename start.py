from typing import Tuple, Dict

from flask import Flask, request
import webview
import threading
# import pkg_resources.py2_warn
import sys
import os
import random
import string
import requests
import json
import time

from Constants import *


def init():
    if not os.path.isdir(DOWNLOADS_DIR):
        os.makedirs(DOWNLOADS_DIR)


def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))

    return result_str


app = Flask(__name__, static_url_path='')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def hello_world():
    return app.send_static_file('register.html')


def start_server():
    app.run(host='127.0.0.1', port=54321)


def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(DOWNLOADS_DIR + local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                    f.write(chunk)
    return local_filename


@app.route('/stage1')
def download_miniconda() -> Tuple[str, int, Dict[str, str]]:
    return download_file(ANACONDA_URL)




@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "1"
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


if __name__ == '__main__':
    init()

    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()

    # window = webview.create_window("Heights Install System", "http://127.0.0.1:54321/?q=" + get_random_alphanumeric_string(8), frameless=True)
    window = webview.create_window("Heights Install System", url="http://127.0.0.1:54321/?q=" + get_random_alphanumeric_string(8), html='', js_api=None, width=800, height=400, \
                      x=None, y=None, resizable=False, fullscreen=False, \
                      min_size=(200, 100), hidden=False, frameless=False, \
                      minimized=False, on_top=False, confirm_close=False, \
                      background_color='#FFF', text_select=False)
    webview.start(debug=True)
    sys.exit()