from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import my_config 
from Helpers.general_helpers import GeneralHelper as Helper
import logging, time
import TestData.test_data as test_data

class header6PMPage(Helper):
    search_input = (By.CSS_SELECTOR,"input[placeholder = 'Search 6pm.com']")
    search_btn = (By.XPATH,"//form[@id = 'searchForm']//button")
    login_icon = (By.XPATH, "//div[@class='z-z']/a[contains(@href, 'account')]")
    btn_search = (By.XPATH, "//button[normalize-space()='Submit Search']")
    def open_login_page(self):
        try:
            self.wait_and_click(self.login_icon)
            logging.info("The login page was opened successfully!")

        except Exception as e:
            logging.info(f"There was an error, {e}")

    def search_items(self):
        try:
            inp = self.find_and_send_keys(self.search_input, test_data.search_text)
            time.sleep(2)
            self.wait_and_click(self.btn_search)
            time.sleep(2)
            # self.find_and_click(self.search_btn)
        except Exception as e:
            logging.info(f"There was an error, {e}")