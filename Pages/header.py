from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import config 
from Helpers.general_helpers import GeneralHelper 

class Marduk(GeneralHelper):
    btn_marduk = (By.XPATH, "//a[@class='H-z']")

    def go_to_login_page(self):
        self.wait_and_click(self.btn_marduk)
