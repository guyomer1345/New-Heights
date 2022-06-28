from src.heights.heights import Heights
from src.package_manager import manager
from src.package_manager.constants import WORK_DIR
import os
import sys

EXE_NAME = 'test_cli.exe'

def copy_exe(exe_path, copy_path):
    with open(f'{exe_path}/{EXE_NAME}', 'rb') as reader:
        data = reader.read()
    
    with open(f'{copy_path}/{EXE_NAME}', 'wb') as writer:
        writer.write(data)

def main(): 
    heights = Heights("version")
    print(heights.path)
    if not heights.is_installed():
        install_path = input('Enter heights installation path: ')
        copy_exe(WORK_DIR, install_path)
        heights.install(path=install_path)
        manager.root_path = install_path
        print(f'cd {install_path} && {EXE_NAME}')
        os.system(f'cd {install_path} && {EXE_NAME}')
        sys.exit()
    
    actions = manager.get_packages_actions()
    print("Your available actions are: ")
    for action in actions:
        print(action)
        # Pick random actions
        print(manager.execute_action(action[0], action[1][0]))
    




    
    
