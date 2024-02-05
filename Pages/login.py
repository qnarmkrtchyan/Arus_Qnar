from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # TODO, remove not used libs
from selenium.webdriver.support import expected_conditions as EC # TODO, remove not used libs
from selenium.webdriver.common.keys import Keys # TODO, remove not used libs
import my_config 
from Helpers.general_helpers import GeneralHelper 

class Login(GeneralHelper):    
        email = (By.XPATH, "//input[@id='ap_email']")
        password = (By.XPATH, "//input[@id='ap_password']")
        login_btn = (By.ID, "signInSubmit")
        
        def try_to_login(self):
            self.find_and_send_keys(self.email, my_config.email)   
            self.find_and_send_keys(self.password, my_config.password)
            self.wait_and_click(self.login_btn)
             

