from selenium.webdriver.remote.webdriver import WebDriver

from framework.pom.activity_page.activity_page import ActivityPage
from framework.pom.bottom_menu.locators.bottom_menu_locators import (
    BottomMenuLocators,
)
from framework.pom.browse_page.browse_page import BrowsePage
from framework.pom.home_page.home_page import HomePage
from framework.pom.profile_page.profile_page import ProfilePage
from framework.reporter.reporter import step


class BottomMenu:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @property
    @step("Click on the 'Home' bottom menu")
    def click_home(self) -> HomePage:
        self.driver.find_element(*BottomMenuLocators.home).click()
        return HomePage(self.driver)

    @property
    @step("Click on the 'Browse' bottom menu")
    def click_browse(self) -> BrowsePage:
        self.driver.find_element(*BottomMenuLocators.browse).click()
        return BrowsePage(self.driver)

    @property
    @step("Click on the 'Activity' bottom menu")
    def click_activity(self) -> ActivityPage:
        self.driver.find_element(*BottomMenuLocators.activity).click()
        return ActivityPage(self.driver)

    @property
    @step("Click on the 'Profile' bottom menu")
    def click_profile(self) -> ProfilePage:
        self.driver.find_element(*BottomMenuLocators.profile)
        return ProfilePage(self.driver)
