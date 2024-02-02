from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import my_config 
from Helpers.general_helpers import GeneralHelper as Helper
import logging
import TestData.test_data as test_data

class header6PMPage(Helper):
    search_input = (By.ID, "searchall")
    search_btn = (By.XPATH,"//form[@id = 'searchForm']//button")
    login_icon = (By.XPATH, "//div[@class='z-z']/a[contains(@href, 'account')]")


    def open_login_page(self):
        try:
            self.wait_and_click(self.login_icon)
            logging.info("The login page was opened successfully!")

        except Exception as e:
            logging.info(f"There was an error, {e}")

    def search_items(self):
        try:
            self.find_and_send_keys(self.search_input, test_data.search_text)
            self.find_and_click(self.search_btn)
        except Exception as e:
            logging.info(f"There was an error, {e}")