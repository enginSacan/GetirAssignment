from pages.main_page import MainPage
from pages.splash_page import SplashPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.wishlist_page import WishlistPage


class Application:
    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.splash_page = SplashPage(driver)
        self.product_page = ProductPage(driver)
        self.cart_page = CartPage(driver)
        self.wishlist_page = WishlistPage(driver)
