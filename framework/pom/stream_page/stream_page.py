from datetime import datetime

import allure
from selenium.webdriver.remote.webdriver import WebDriver

from framework.pom.base_page import BasePage
from framework.pom.stream_page.locators.stream_page_locators import (
    StreamPageLocators,
)
from framework.pom.stream_page.locators.stream_popup_locators import (
    StreamPopupLocators,
)


class StreamPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def close_stream_popup_if_appeared(self):
        popup = self.wait_element(
            StreamPopupLocators.popup, timeout=5, error=False
        )
        if popup is not None:
            with allure.step("Close the stream popup"):
                self.driver.find_element(StreamPopupLocators.close_btn).click()

    def wait_video_loaded(self, timeout=5) -> bool:
        start = datetime.now()
        while True:
            if self._is_video_playing(StreamPageLocators.video_stream):
                return True
            if (datetime.now() - start).total_seconds() > timeout:
                return False

    def _is_video_playing(self, video_locator: tuple[str, str]) -> bool:
        """
        Check if the video is currently playing
        :param video_locator:
        :return: True if the video is playing, False otherwise
        """
        video_selector = video_locator[1]
        is_playing = self.driver.execute_script(
            """
            var video = document.querySelector(arguments[0]);
            return video !== null &&
                   video.readyState > 2 &&
                   !video.paused &&
                   !video.ended &&
                   video.currentTime > 0;
        """,
            video_selector,
        )
        return bool(is_playing)
