import allure

from framework.reporter.reporter import attach_screenshot_to_report


class TestStreamerProfilePage:
    @allure.title("Streamer profile page mobile view")
    def test_streamer_profile_page_mobile_view(self, home_page, bottom_menu):
        home_page.open()
        browse_page = bottom_menu.click_browse
        browse_page.search_for(text="StarCraft II")
        category_page = browse_page.click_search_result(position=1)
        streamer_profile_page = category_page.click_streamer_profile(position=2)

        screenshot = streamer_profile_page.take_screenshot(
            "streamer_profile_page"
        )

        attach_screenshot_to_report(
            screenshot, name="streamer_profile_page.png"
        )

    @allure.title("Video stream is started on the stream page")
    def test_video_stream_is_started_on_the_stream_page(
        self, home_page, bottom_menu
    ):
        home_page.open()
        browse_page = bottom_menu.click_browse
        browse_page.search_for(text="StarCraft II")
        category_page = browse_page.click_search_result(position=3)
        stream_page = category_page.click_live_stream(position=1)
        stream_page.close_stream_popup_if_appeared()

        screenshot = stream_page.take_screenshot("stream_page")

        attach_screenshot_to_report(screenshot, name="stream_page.png")
