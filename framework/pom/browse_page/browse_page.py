from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from framework.pom.base_page import BasePage
from framework.pom.browse_page.locators.browse_page_locators import (
    BrowsePageLocators,
)
from framework.pom.category_page.category_page import CategoryPage
from framework.reporter.reporter import step
from framework.sut.urls import BROWSE_PAGE


class BrowsePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.url = BROWSE_PAGE

    @step("Search for: {text}")
    def search_for(self, text: str) -> None:
        self.wait_element(BrowsePageLocators.search_field).send_keys(text)

    @step("Click on the search result on position: {position}")
    def click_search_result(self, position: int = 1) -> CategoryPage:
        self._search_result(position).click()
        return CategoryPage(self.driver)

    def _search_result(self, position: int = 1) -> WebElement:
        results = self.wait_elements(BrowsePageLocators.search_results)
        try:
            return results[position - 1]
        except IndexError:
            raise NoSuchElementException("The search results is not displayed")
