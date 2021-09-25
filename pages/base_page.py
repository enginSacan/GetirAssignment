
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def back_last_page(self):
        self.driver.back()
