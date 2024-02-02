#Note
#export PATH=$PATH:/Users/qnarmkrtchyan/Library/Python/3.9/bin
#I have to export this every time before the run, so my system will recognise the 'pytest' keyword.
from  conftest import driver as mydriver
from Helpers.general_helpers import GeneralHelper as Helper
import config
import logging,datetime
from Pages.login import Login
from Pages.header import header6PMPage
from Pages.header import header6PMPage
from TestData import test_data


def test_search_by_brand(mydriver):
    try:
        t_start = datetime.datetime.now()
        logging.info(f"Program has started at: {t_start}")

        driver = mydriver
        helper_obj = Helper(driver)
        helper_obj.navigate_to_page(config.url)
        
        header_nav = header6PMPage(driver)
        header_nav.open_login_page()
        login_page = Login(driver)
        login_page.try_to_login()
        logging.info(f"user with email {config.email} has been logged in successfully!")

        helper_obj.find_and_send_keys(header6PMPage.search_input, test_data.search_text)
        helper_obj.find_and_click(header6PMPage.search_btn)
        logging.info(f"The search of {test_data.search_text} was successfully!")



    except Exception as e:
        logging.info(f"There was an error, {e}")

