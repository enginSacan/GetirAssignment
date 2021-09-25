from selenium.webdriver.common.by import By

from base_element import BaseElement
from base_page import BasePage
from variables import Variables


class SplashPage(BasePage):
    @property
    def skip_button(self):
        locator = (By.ID, Variables.skip_btn_id)

        return BaseElement(self.driver, locator[0], locator[1])

    @property
    def next_button(self):
        locator = (By.ID, Variables.skip_btn_id)
        return BaseElement(self.driver, locator[0], locator[1])

    def skip_splash_page(self):
        self.skip_button.click()

    def next_page(self):

        self.next_button.click()
