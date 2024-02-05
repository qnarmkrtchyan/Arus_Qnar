from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Helpers.general_helpers import GeneralHelper as Helper
import logging, time
import TestData.test_data as test_data
import random

from selenium.webdriver.common.by import By

class HomePage(Helper):
    # brand_section = (By.CSS_SELECTOR, "section:is(:scope > h3#brandNameFacet)")
    # brand_childs = (By.XPATH, "//ul[@aria-labelledby='brandNameFacet']")   

    # def selectBrand(self):
    #     brand_elements = self.driver.find_elements(*self.brand_childs)
    #     self.move_to_element(brand_elements)

    #     brand_index = random.randint(0, len(brand_elements) - 1)
    #     print(brand_index)
    #     brand_locator = (By.XPATH, f"//ul[@aria-labelledby='brandNameFacet']//li[{brand_index + 1}]//a[1]")  # Adjusted index       
    #     brand_element = self.driver.find_element(*brand_locator)

    #     #self.move_to_element(self.brand_section)
    #     self.move_to_element(brand_element)
    #     time.sleep(1)
    #     self.wait_visibility(brand_element).click()



    # def selectPrice(self):
    #     pass

    # def selectColor(self):
    #     pass

   

    # def verify_results(self, expected_brand):
    #     results = self.driver.find_elements(self.product_results)
    #     for result in results:
    #         # Extracting information from each result
    #         result_brand = result.find_element(By.XPATH, './/span[@data-qa="product-brand"]').text
    #         assert expected_brand.lower() in result_brand.lower()

 
    search_result_count_loc = (By.XPATH, "//span[@class='EC-z']")
    search_result_loc = (By.XPATH, "//article[@class='Vma-z YE-z']")
    brand_list_txt_loc = (By.XPATH, '//ul[@aria-labelledby="brandNameFacet"]/li/a/span[1]')
    price_list_txt_loc = (By.XPATH, '//ul[@aria-labelledby="priceFacet"]/li/a/span[1]')
    color_list_txt_loc = (By.XPATH, '//ul[@aria-labelledby="colorFacet"]/li/a/span[1]')
    filtered_items_loc = (By.XPATH,'//ul[@id="searchSelectedFilters"]//a')
 
    search_result = False
     
    def check_search_result(self):
        try:
            search_result = self.find_elem_dom(self.search_result_count_loc)
            self.wait_visibility(self.search_result_count_loc)
            if "items found" in search_result.text:
                logging.info(f"Search result: '{search_result.text}'.")
                self.search_result = True
            else:
                logging.info(f"No results found.")
                self.search_result = False
            return self.search_result
        except Exception as e:
            logging.error(f"Error in 'check_search_result': {e}")
           
    def filter_elem_randomly(self, locator):
        try:
            self.move_to_element(locator)
            self.find_elements(locator)
            items = self.find_elems_dom(locator)
            random_item = random.choice(items)
            random_item.click()
            item_txt = random_item.text
            return item_txt
        except Exception as e:
            logging.error(f"Error in 'filter_random_elem': {e}")
       
    def apply_filter_and_create_dict(self):
        try:
            if self.search_result:
                    selected_brand = self.filter_elem_randomly(self.brand_list_txt_loc)
                    self.wait_and_click(self.brand_list_txt_loc)
                    time.sleep(2)
                    selected_price = self.filter_elem_randomly(self.price_list_txt_loc)
                    self.wait_and_click(self.price_list_txt_loc)
                    time.sleep(2)
                    selected_color = self.filter_elem_randomly(self.color_list_txt_loc)
                    self.wait_and_click( self.color_list_txt_loc)
                    result_dict = {
                                    "brand": selected_brand,
                                    "price": selected_price,
                                    "color": selected_color
                                    }
                    logging.info(f"Applied Filters: {result_dict}")
                    return result_dict
            else:
                logging.info("No search results to apply filters for.")
        except Exception as e:
            logging.error(f"Error in 'apply_filters_to_product': {e}")
       
    def get_filtered_result_texts(self):
        try:
            result_dict = {}
            filtered_result_list = self.find_elems_dom(self.filtered_items_loc)
            self.find_elements(self.filtered_items_loc)
            for index, element in enumerate(filtered_result_list):
                key = ['color', 'brand', 'price'][index]
                result_dict[key] = element.text.strip()
            logging.info(f"Displayed Filters: {result_dict}")
            return result_dict
        except Exception as e:
            logging.error(f"Error in 'get_filtered_result_texts': {e}")