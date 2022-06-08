from downloader import download_program
from constants import Apps


def download_miniconda():
    return download_program(Apps.MiniConda.value.URL)


def download_7zip():
    return download_program(Apps.SevenZip.value.URL)
