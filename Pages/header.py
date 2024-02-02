from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import config 
from Helpers.general_helpers import GeneralHelper as Helper
import logging

class header6PMPage(Helper):
    search_input = (By.XPATH, "//input[@id='searchall']")
    search_btn = (By.XPATH,"//form[@id = 'searchForm']//button")
    login_icon = (By.CSS_SELECTOR, "a[text = 'My Account']")
    signin_page_text = (By.CSS_SELECTOR, "h1[text = 'Sign-In'")

    def open_login_page(self):
        try:
            self.find_and_click(self.login_icon)
            self.wait_visibility(self.signin_page_text)
            if self.signin_page_text:
                logging.info("The signin was opened successfully!")
            else:
                logging.info("The signin wasn't opened!")

        except Exception as e:
            logging.info(f"There was an error, {e}")
