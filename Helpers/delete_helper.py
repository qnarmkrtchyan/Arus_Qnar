from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import shutil
from conftest import BrowserHelper 
import os


class DeleteHelper:
    def delete_file(self, files):
        file_path = os.path.join(os.path.dirname(__file__), files)
        try:
            if os.path.exists(file_path):
                if os.path.isdir(file_path):
                    confirm = input(f"Do you want to remove '{files}' folder and its contents? (yes/no): ")
                    if confirm.lower() == "yes":
                        shutil.rmtree(file_path)
                        print(f"'{files}' folder and its contents have been deleted.")
                    elif confirm.lower() == "no":
                        print(f"'{files}' folder hasn't been deleted.")
                    else:
                        print(f"'{files}' folder hasn't been deleted, because of incorrect input.")
                else:
                    confirm = input(f"Do you want to remove '{files}' file? (yes/no): ")
                    if confirm.lower() == "yes":
                        os.remove(file_path)
                        print(f"'{files}' file has been deleted.")
                    elif confirm.lower() == "no":
                        print(f"'{files}' file hasn't been deleted.")
                    else:
                        print(f"'{files}' file hasn't been deleted, because of incorrect input.")
            else:
                print(f"'{files}' does not exist.")
        except Exception as e:
            print(f"Error occurred while deleting '{files}'. Exception: {e}")