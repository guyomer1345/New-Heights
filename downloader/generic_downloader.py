from typing import Tuple, Dict
import time
import json
import os
import requests
from data_classes import Response
from constants import DOWNLOADS_DIR, FILE_EXISTS, JSON_CONTENT_TYPE


def download_file(url, local_filename=None):
    """
    Sends a GET request to the url, saving the (supposedly) executable file
    response in the download directory.

    :param url: where to send the GET request to
    :return: the filename, relative to the download directory
    """
    if not local_filename:
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
        if not ((time.time() - file_time) / 3600 > 24 * 30):
            return Response(True, str(name)+ FILE_EXISTS, 200, JSON_CONTENT_TYPE)

    try:
        filename = download_file(url)
    except requests.exceptions.HTTPError as e:
        return Response(True, str(e), 500 , JSON_CONTENT_TYPE)

    if filename:
        return Response(True, str(filename), 200 ,JSON_CONTENT_TYPE)

    return Response(False, str(filename), 500, JSON_CONTENT_TYPE)


def download_program(url: str) -> Tuple[str, int, Dict[str, str]]:
    """
    Attempts to download the program from the given url

    :param url: the program's installer's url
    :return: a response object according to the results of the download
    """
    return download_file_with_response(url)