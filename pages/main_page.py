import random
from selenium.webdriver.common.by import By

from base_element import BaseElement
from base_page import BasePage
from variables import Variables


class MainPage(BasePage):

    @property
    def hamburger_button(self):
        locator = (By.XPATH, Variables.hamburger_btn_xpath)
        return BaseElement(self.driver, locator[0], locator[1])
    @property
    def hamburger_category(self):
        locator = (By.XPATH, Variables.hamburger_all_categories_xpath)
        return BaseElement(self.driver, locator[0], locator[1])
    @property
    def baby_care_in_hamburger(self):
        locator = (By.XPATH, Variables.hamburger_baby_care_xpath)
        return BaseElement(self.driver, locator[0], locator[1])

    @property
    def snack_in_scroll(self):
        locator = (By.XPATH, Variables.snacks_in_scroll_xpath)
        return BaseElement(self.driver, locator[0], locator[1])

    @property
    def snack_in_hamburger(self):
        locator = (By.XPATH, Variables.hamburger_snacks_xpath)
        return BaseElement(self.driver, locator[0], locator[1])

    @property
    def cart_icon(self):
        locator = (By.ID, Variables.cart_btn_id)
        return BaseElement(self.driver, locator[0], locator[1])

    @property
    def wishlist_in_hamburger(self):
        locator = (By.XPATH, Variables.wishlist_in_hamburger_xpath)
        return BaseElement(self.driver, locator[0], locator[1])

    def open_hamburger_menu(self):
        self.hamburger_button.click()

    def go_to_baby_products(self):
        self.baby_care_in_hamburger.click()

    def go_to_snack_products(self):
        self.open_hamburger_menu()
        self.snack_in_hamburger.click()

    def go_to_cart(self):
        self.cart_icon.click()

    def get_category_number_and_choose_random(self):
        self.hamburger_category.text
        hamburger_categories = self.driver.find_elements(By.XPATH, Variables.hamburger_all_categories_xpath)
        print("Category number is: "+len(hamburger_categories))
        random_category_number = random.randint(0, len(hamburger_categories))
        hamburger_categories[random_category_number].click()

    def open_wishlist(self):
        self.open_hamburger_menu()
        self.wishlist_in_hamburger.click()
