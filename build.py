# -*- coding: utf-8 -*-
import PyInstaller.__main__


def main():
    """
    Add Documentation here
    """
    PyInstaller.__main__.run([
        # '--name=%s' % "Heights_Installation",
        '--onefile',
        '--windowed',
        # '--uac-admin',
        '--add-data=%s' % "static;static",
        '--icon=%s' % 'Heights.ico',
        'start.py'
    ])  # "--hidden-import=%s" % "_winreg, winreg.HKEY_LOCAL_MACHINE, platform, os, sys, logging, clint.textui",


if __name__ == '__main__':
    main()