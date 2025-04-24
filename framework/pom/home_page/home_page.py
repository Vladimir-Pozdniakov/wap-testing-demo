from framework.pom.base_page import BasePage
from framework.sut.urls import HOME_PAGE


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = HOME_PAGE
