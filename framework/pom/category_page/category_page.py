from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from framework.pom.base_page import BasePage
from framework.pom.category_page.locators.category_page_locators import (
    CategoryPageLocators,
)
from framework.pom.stream_page.stream_page import StreamPage
from framework.pom.streamer_profile_page.streamer_profile_page import (
    StreamerProfilePage,
)
from framework.reporter.reporter import step


class CategoryPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @step("Click on the streamer profile on position: {position}")
    def click_streamer_profile(self, position: int = 1) -> StreamerProfilePage:
        self._streamer_profile_name(position).click()
        return StreamerProfilePage(self.driver)

    @step("Click on the Live Streamer on position: {position}")
    def click_live_stream(self, position: int = 1) -> StreamPage:
        self._live_stream(position).click()
        stream_page = StreamPage(self.driver)
        stream_page.wait_video_loaded()
        return stream_page

    def _streamer_profile_name(self, position: int = 1) -> WebElement:
        return self.get_element_by_position(
            position=position,
            locator=CategoryPageLocators.profile_name,
            error_message="The profile position is not present",
        )

    def _live_stream(self, position: int = 1) -> WebElement:
        return self.get_element_by_position(
            position=position,
            locator=CategoryPageLocators.live_stream,
            error_message="The Live Stream position is not present",
        )
