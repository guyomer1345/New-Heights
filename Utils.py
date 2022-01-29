from Constants import *
import json
import time
import requests


def download_file(url: str) -> Tuple[str, int, Dict[str, str]]:
    name = url.split('/')[-1]

    if os.path.exists(DOWNLOADS_DIR + name):
        file_time = os.path.getctime(DOWNLOADS_DIR + name)
        if not ((time.time() - file_time) / 3600 > 24*30):
            return json.dumps({'success':True, 'msg':str(name) + FILE_EXISTS}), 200, JSON_CONTENT_TYPE

    try:
        filename = download_file(url)
    except requests.exceptions.HTTPError as e:
        return json.dumps({'error':False, 'msg':str(e), 'httpcode':e.response.status_code}), 500, JSON_CONTENT_TYPE

    if filename:
        return json.dumps({'success':True, 'msg':str(filename)}), 200, JSON_CONTENT_TYPE

    return json.dumps({'error':False, 'msg':str(filename)}), 500, JSON_CONTENT_TYPE
