from flask import Flask, request
import webview
import threading
import sys
import random
import string
import logging
import installers
from constants import *
import installers

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


@app.route('/')
def hello_world():
    return app.send_static_file('register.html')


def start_server():
    app.run(host='127.0.0.1', port=54321)


@app.route('/install')
def download():
    app_name = request.args.get('name', '')
    installers.manager.install(app_name)


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


if __name__ == '_1_main__':
    init()

    t = threading.Thread(target=start_server)

    debug_mode = '-d' in sys.argv
    t.daemon = not debug_mode

    t.start()

    if not debug_mode:
        window = webview.create_window("Heights Install System",
                                       url="http://127.0.0.1:54321/?q=" +
                                           get_random_alphanumeric_string(
                                               8), height=400,
                                       resizable=False, min_size=(200, 100),
                                       background_color='#FFF')
        webview.start(debug=True)
        sys.exit()
