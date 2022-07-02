from src.heights.heights import Heights
from src.package_manager import manager
from src.package_manager.constants import WORK_DIR
import os
import sys

def main(): 
    heights = Heights("version")
    print(heights.path)
    if not heights.is_installed():
        install_path = input('Enter heights installation path: ')
        heights.install(install_path)
    
    actions = manager.get_packages_actions()
    print("Your available actions are: ")
    for action in actions:
        print(action)
        # Pick random actions
        print(manager.execute_action(action[0], action[1][0]))
    




    
    
