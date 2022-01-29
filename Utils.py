from Constants import *
import json
import time
import requests


def download_file(url):
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
