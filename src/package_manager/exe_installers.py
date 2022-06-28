from src.package_manager.exe_installer import ExeInstaller
from src.package_manager.constants import Apps

miniconda = Apps.MiniConda.value
seven_zip = Apps.SevenZip.value

seven_zip_installer = ExeInstaller(
                                                        seven_zip.APP_NAME,
                                                         '1.0.0', 
                                                        seven_zip.URL,  
                                                        seven_zip.INSTALL_COMMAND,
                                                        seven_zip.INSTALLATION_FOLDER
                                                        )

miniconda_installer = ExeInstaller(
                                                        miniconda.APP_NAME,
                                                         '1.0.0', 
                                                        miniconda.URL,  
                                                        miniconda.INSTALL_COMMAND,
                                                        miniconda.INSTALLATION_FOLDER
                                                        )
