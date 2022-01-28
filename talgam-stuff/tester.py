import zipfile
import os

WORK_DIR = os.path.dirname(os.path.realpath(__file__))

def ziper():
    filename = os.path.join(WORK_DIR, "tst.exe")
    # zip file handler  
    os.system("7-Zip\\7z.exe l -ba {}".format(filename))

if __name__ == "__main__":
    ziper()