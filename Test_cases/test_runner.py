import sys
sys.path.append("/Users/qnarmkrtchyan/Desktop/Arus_Qnar")
from  conftest import driver
from Helpers.general_helpers import GeneralHelper
import config


driver = conftest.driver()

login_page = QwallityEntry(driver)
login_page.navigate_to_page(config.url)

login_page.try_to_login()

