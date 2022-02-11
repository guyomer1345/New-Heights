from Constants import MINICONDA_INSTALL_COMMAND, \
    MINICONDA_INSTALLATION_FOLDER, MINICONDA_URL, MINICONDA_NAME, \
    \
    SEVEN_ZIP_INSTALL_COMMAND, SEVEN_ZIP_INSTALLATION_FOLDER, SEVEN_ZIP_URL,\
    SEVEN_ZIP_NAME

from GeneralInstaller import install_program


def install_miniconda():
    return install_program(MINICONDA_NAME, MINICONDA_INSTALLATION_FOLDER,
                           MINICONDA_URL, MINICONDA_INSTALL_COMMAND)


def install_7zip():
    return install_program(SEVEN_ZIP_NAME, SEVEN_ZIP_INSTALLATION_FOLDER,
                           SEVEN_ZIP_URL, SEVEN_ZIP_INSTALL_COMMAND)
