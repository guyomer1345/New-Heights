import os
from custom_installers import install_miniconda

install_miniconda()

os.system('conda create -n temp python=3.5 -y && activate temp &&  pip install -r requirements.txt ')
os.system('activate temp && python start.py')
os.system('conda env remove --name temp')

