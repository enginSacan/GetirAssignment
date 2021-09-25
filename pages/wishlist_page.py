import random
from selenium.webdriver.common.by import By

from base_element import BaseElement
from base_page import BasePage
from variables import Variables


class WishlistPage(BasePage):

    @property
    def wishlist_item(self):
        locator = (By.XPATH, Variables.wishlist_items_xpath)
        return BaseElement(self.driver, locator[0], locator[1])

    @property
    def wishlist_remove_icon(self):
        locator = (By.XPATH, Variables.wishlist_remove_icon_xpath)
        return BaseElement(self.driver, locator[0], locator[1])

    def count_wishlist(self):
        self.wishlist_item.text
        wishlist_list_items = self.driver.find_elements(By.XPATH, Variables.wishlist_items_xpath)
        return len(wishlist_list_items)

    def remove_items_in_wishlist(self):
        self.wishlist_remove_icon.value
        wishlist_remove_icons = self.driver.find_elements(By.XPATH, Variables.wishlist_remove_icon_xpath)
        for wishlist_remove in wishlist_remove_icons:
            wishlist_remove.click()
