import sys
sys.path.append("/Users/Arusyak_Minasyan/Desktop/Python-working/Qwallity-Automation/Lesson_27_qwallity_app")
from Helpers.my_driver import BrowserHelper 
from Helpers.general_helpers import GeneralHelper

import config
from Pages.my_basket import QwallityEntry

helper = BrowserHelper()
driver = helper.driver()

login_page = QwallityEntry(driver)
login_page.navigate_to_page(config.url)

login_page.try_to_login()

