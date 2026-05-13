from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.firefox.options import Options as firefox_options

class DriverFactory:
    _driver = None

    @classmethod
    def get_driver(cls, browser):

        if cls._driver is None:
            if browser.lower() == "chrome":
                options = chrome_options()
                options.add_argument("--start-maximized")
                options.add_argument("--disable-notifications")
                cls._driver = webdriver.Chrome(options=options)

            elif browser.lower() == "firefox":
                options = firefox_options()
                options.set_preference("dom.webnotifications.enabled", False)
                cls._driver = webdriver.Firefox(options=options)
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None