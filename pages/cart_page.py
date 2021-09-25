from selenium.webdriver.common.by import By

from base_element import BaseElement
from base_page import BasePage
from variables import Variables


class CartPage(BasePage):
    @property
    def remove_button(self):
        locator = (By.XPATH, Variables.remove_btn_xpath)
        return BaseElement(self.driver, locator[0], locator[1])

    @property
    def product_name(self):
        locator = (By.XPATH, Variables.product_names_xpath)
        return BaseElement(self.driver, locator[0], locator[1])

    def remove_all_products(self):
        self.remove_button.text
        remove_buttons = self.driver.find_elements(By.XPATH, Variables.remove_btn_xpath)
        for remove_button in remove_buttons:
            remove_button.click()

    def check_products_in_cart(self, products):
        self.product_name.text
        product_names = self.driver.find_elements(By.XPATH, Variables.product_names_xpath)
        product_prices = self.driver.find_elements(By.XPATH, Variables.product_prices_xpath)

        for product_name in product_names:
            if product_name not in products.keys():
                return False
        for product_price in product_prices:
            if product_price not in products.values():
                return False
        return True
