from selenium.webdriver.remote.webdriver import WebDriver

from framework.pom.base_page import BasePage
from framework.sut.urls import ACTIVITY_PAGE


class ActivityPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.url = ACTIVITY_PAGE
