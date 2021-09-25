import random
from selenium.webdriver.common.by import By

from base_element import BaseElement
from base_page import BasePage
from variables import Variables


class ProductPage(BasePage):
    added_products = {}

    @property
    def product_detail(self):
        locator = (By.ID, Variables.products_detail_id)
        return BaseElement(self.driver, locator[0], locator[1])

    @property
    def add_cart(self):
        locator = (By.ID, Variables.add_cart_btn_id)
        return BaseElement(self.driver, locator[0], locator[1])

    @property
    def price_text(self):
        locator = (By.XPATH, Variables.price_text_xpath)
        return BaseElement(self.driver, locator[0], locator[1])

    @property
    def product_name(self):
        locator = (By.XPATH, Variables.product_text_xpath)
        return BaseElement(self.driver, locator[0], locator[1])

    @property
    def products_wishlist_icon(self):
        locator = (By.XPATH, Variables.products_wishlist_icon_xpath)
        return BaseElement(self.driver, locator[0], locator[1])

    def open_random_product_details(self):
        self.product_detail.text
        product_details = self.driver.find_elements(By.ID, Variables.products_detail_id)
        random_product_number = random.randint(0, len(product_details))
        product_details[random_product_number].click()
        self.get_product_price()

    def get_product_price(self):
        price = self.price_text.text
        product = self.product_name.text
        self.added_products[product] = price
        print(str(self.added_products))

    def add_product_to_cart(self):
        self.add_cart.click()

    def add_three_product_to_wishlist(self):
        self.products_wishlist_icon.text
        products_wishlists = self.driver.find_elements(By.XPATH, Variables.products_wishlist_icon_xpath)
        if len(products_wishlists) > 2:
            for x in range(3):
                products_wishlists[x].click()

