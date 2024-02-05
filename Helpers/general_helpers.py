from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import shutil
import os
import logging


class GeneralHelper():

    def __init__(self, driver):
        self.driver = driver
  
    def navigate_to_page(self, page_url):
        try:
            self.driver.get(page_url)
        except Exception as e:
            print(f"Error navigating to page: {e}")
        
    def move_to_element(self, element):
        try:
            locator = self.driver.find_element(*element)
            self.driver.execute_script("arguments[0].scrollIntoView();", locator)
        except Exception as e:
            print(f"Error moving to element: {e}")


    def wait_and_click(self, element):
        try:
            elem = WebDriverWait(self.driver, 100).until(
                EC.element_to_be_clickable((element)))
            elem.click()
        except Exception as e:
            print(f"Error waiting and clicking: {e}")
    
    def find_elem_dom(self, loc, sec=20):
        try:
            elem = WebDriverWait(self.driver, sec).until(
                EC.presence_of_element_located(loc))
            return elem
        except Exception as e:
            print(f"Error finding element in DOM: {e}")
        
    

    def wait_visibility(self, element):
        try:
            elem = WebDriverWait(self.driver, 60).until(
                EC.visibility_of_element_located(element))
            return elem
        except Exception as e:
            print(f"Error waiting for element visibility: {e}")
    
    def find_elements(self, element):
        try:
            elem = WebDriverWait(self.driver, 60).until(
                EC.visibility_of_all_elements_located(element))
            return elem
        except Exception as e:
            print(f"Error waiting for element visibility: {e}")
    
    def find_elems_dom(self, element, timeout=100):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(element))
        except Exception as e:
            logging.error(f"Error in 'find_elems_in_dom': {e}")
    
    def find_and_send_keys(self, element, inp_text):
        try:
            elem = self.wait_visibility(element)
            elem.send_keys(inp_text)
        except Exception as e:
            print(f"Error finding element and sending keys: {e}")
    

    def write_to_file(self, text_to_write):
        try:
            with open(os.path.join(os.path.dirname(__file__), data.file_name), 'a+') as f:
                f.write(f'{str(text_to_write)}\n')
        except Exception as e:
            print(f"Error writing to file: {e}")


    # def find_and_click(self, element, ):
    #     try:
    #         EC.element_to_be_clickable(element)
    #         element.click()

    #     except Exception as e:
    #         print(f"Error: {e}")


# TODO,add logging in all methods            