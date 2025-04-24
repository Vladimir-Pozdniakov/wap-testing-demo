from selenium.webdriver.remote.webdriver import WebDriver

from framework.pom.base_page import BasePage


class StreamerProfilePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
