from appium import webdriver
from app.Application import Application


def before_scenario(context, scenario):
    desired_caps = {
        "deviceName": "emulator-5554",
        "platformName": "android",
        "appPackage": "com.allandroidprojects.getirsample",
        "appActivity": ".startup.SplashActivity",
        "noReset": True
    }

    context.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    context.app = Application(context.driver)


def after_scenario(context, scenario):
    context.driver.quit()
