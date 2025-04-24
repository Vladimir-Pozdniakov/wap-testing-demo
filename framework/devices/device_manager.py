from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.remote.webdriver import WebDriver

from settings import HEADLESS


class DeviceManager:
    def __init__(self, browser: str):
        self.browser = browser

    def get_driver(self) -> WebDriver:
        if self.browser == "chrome-mobile":
            return webdriver.Chrome(self.get_mobile_chrome_options())
        if self.browser == "chrome":
            return webdriver.Chrome()
        elif self.browser == "firefox":
            return webdriver.Firefox()
        else:
            raise ValueError(
                f"Browser {self.browser} is not supported."
                f"Possible values: chrome-mobile, chrome, "
                f"firefox"
            )

    def get_mobile_chrome_options(self) -> ChromeOptions:
        """
        Fixture that provides a Chrome WebDriver configured for mobile view.
        """
        chrome_options = ChromeOptions()

        # Mobile emulation settings
        mobile_emulation = {
            "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
            "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; "
            "Nexus 5 Build/JOP40D) "
            "AppleWebKit/535.19 (KHTML, like Gecko) "
            "Chrome/18.0.1025.166 Mobile Safari/535.19",
            "clientHints": {"platform": "Android", "mobile": True},
        }

        # Enable mobile emulation
        chrome_options.add_experimental_option(
            name="mobileEmulation", value=mobile_emulation
        )
        # Disable browser automation notification
        chrome_options.add_experimental_option(
            name="excludeSwitches", value=["enable-automation"]
        )
        chrome_options.add_argument("--window-size=375,812")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("disable-infobars")

        if HEADLESS:
            chrome_options.add_argument("--headless=new")

        return chrome_options
