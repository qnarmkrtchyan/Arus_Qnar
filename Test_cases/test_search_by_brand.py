#Note
#export PATH=$PATH:/Users/qnarmkrtchyan/Library/Python/3.9/bin
#I have to export this every time before the run, so my system will recognise the 'pytest' keyword.
from  conftest import driver as mydriver
from Helpers.general_helpers import GeneralHelper as Helper
import my_config
import logging,datetime
from Pages.login import Login
from Pages.header import header6PMPage
from Pages.header import header6PMPage
import TestData.test_data as test_data
import time

def test_search_by_brand(mydriver):

    t_start = datetime.datetime.now()
    logging.info(f"Program has started at: {t_start}")

    driver = mydriver
    helper_obj = Helper(driver)
    helper_obj.navigate_to_page(my_config.url)
    
    #login part
    header_nav = header6PMPage(driver)
    header_nav.open_login_page()
    login_page = Login(driver)
    login_page.try_to_login()

    #search part
    
    header_nav.search_items()
    time.sleep(5)