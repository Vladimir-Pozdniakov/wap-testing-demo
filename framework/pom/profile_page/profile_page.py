from selenium.webdriver.remote.webdriver import WebDriver

from framework.pom.base_page import BasePage
from framework.sut.urls import PROFILE_PAGE


class ProfilePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.url = PROFILE_PAGE
