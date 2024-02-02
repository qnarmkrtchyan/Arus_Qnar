from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import my_config 
from Helpers.general_helpers import GeneralHelper as Helper
import logging

class header6PMPage(Helper):
    search_input = (By.XPATH, "//input[@id='searchall']")
    search_btn = (By.XPATH,"//form[@id = 'searchForm']//button")
    login_icon = (By.XPATH, "//div[@class='z-z']/a[contains(@href, 'account')]")


    def open_login_page(self):
        try:
            self.wait_and_click(self.login_icon)
            logging.info("The login page was opened successfully!")

        except Exception as e:
            logging.info(f"There was an error, {e}")
