from Constants import DOWNLOADS_DIR, FILE_EXISTS, JSON_CONTENT_TYPE
import json
import time
import requests
import os
from typing import Tuple, Dict


def download_file(url):
    """
    Sends a GET request to the url, saving the (supposedly) executable file
    response in the download directory.

    :param url: where to send the GET request to
    :return: the filename, relative to the download directory
    """
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(DOWNLOADS_DIR + local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                # if chunk:
                f.write(chunk)
    return local_filename


# TODO: implement dataclass of response
def download_file_with_response(url: str) -> Tuple[str, int, Dict[str, str]]:
    """
    Attempts to download the file located at the url if it doesn't already
    exist, returning JSON GET response, can be implemented for start.py

    :param url: where to download the file from
    :return: a JSON GET response
    """
    # TODO: add error handling of url?
    name = url.split('/')[-1]

    if os.path.exists(DOWNLOADS_DIR + name):
        file_time = os.path.getctime(DOWNLOADS_DIR + name)

        # TODO: change to proper version checking
        if not ((time.time() - file_time) / 3600 > 24*30):
            return json.dumps({'success':True, 'msg':str(name) + FILE_EXISTS}), 200, JSON_CONTENT_TYPE

    try:
        filename = download_file(url)
    except requests.exceptions.HTTPError as e:
        return json.dumps({'error':False, 'msg':str(e), 'httpcode':e.response.status_code}), 500, JSON_CONTENT_TYPE

    if filename:
        return json.dumps({'success':True, 'msg':str(filename)}), 200, JSON_CONTENT_TYPE

    return json.dumps({'error':False, 'msg':str(filename)}), 500, JSON_CONTENT_TYPE
