import time
from datetime import datetime

import allure
from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from utilities.file_management import get_test_screenshot_path


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = self.__class__.__name__

    def open(self, url: str = None):
        url = url or self.url
        with allure.step(f"Open the '{url}' page"):
            self.driver.get(url)

    def wait_element(
        self, locator: tuple[str, str], timeout=10, error=True
    ) -> WebElement | None:
        wait = WebDriverWait(self.driver, timeout)
        try:
            return wait.until(lambda d: d.find_element(*locator))
        except TimeoutException:
            if error:
                raise TimeoutException(
                    f"Element with locator '{locator}' was not found "
                    f"on the page"
                )
            else:
                return None

    def wait_elements(self, locator: tuple[str, str]) -> list[WebElement]:
        """
        Waits for the given elements to appear on a web page.

        This method waits for the presence of one or more web elements
        located by the specified locator tuple. It attempts to locate the
        elements multiple times within a specified timeout period and ensures
        the stability of the element count before returning the final
        list of elements.

        :param locator: A tuple containing the strategy and locator used to
                        identify the elements (e.g., (By.ID, "example")).
                        The first element is the locator type such as "By.ID",
                        and the second element is the locator value.
        :return: A list of located WebElement objects.
        """
        elements = []
        elements_count = 0
        attempts = 5
        wait = WebDriverWait(self.driver, 10)

        while attempts > 0:
            try:
                elements = wait.until(lambda d: d.find_elements(*locator))
            except TimeoutException:
                pass

            if elements_count == len(elements):
                break

            elements_count = len(elements)
            attempts -= 1
            time.sleep(0.5)

        return elements

    def scroll_to_element_center(
        self, element: tuple[str, str] | WebElement
    ) -> WebElement:
        if isinstance(element, tuple):
            element = self.wait_element(element)

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                behavior: 'smooth',
                block: 'center',
                inline: 'center'
            });
        """,
            element,
        )
        # Wait for animation stabilization
        time.sleep(0.5)

        return element

    def take_screenshot(self, filename: str = None) -> bytes | bool:
        self.wait_until_dom_fully_loaded()
        png = self.driver.get_screenshot_as_png()
        if filename:
            path = get_test_screenshot_path(filename)
            try:
                with open(path, "wb") as f:
                    f.write(png)
            except OSError:
                return False
        return png

    def wait_until_dom_fully_loaded(self, storage=5, timeout=10) -> float:
        """
        Waits until the DOM (Document Object Model) is fully loaded and stable,
        ensuring that the document content does not change significantly
        over time. The method continuously checks the state of the DOM using
        JavaScript execution within the context of a web driver interface.
        It considers the DOM fully loaded when the HTML content remains
        unchanged for a defined series of checks. This method returns the time
        it took for the DOM to stabilize, measured in seconds.

        This function is designed for environments where dynamic content
        loading might occur (e.g., JavaScript-heavy websites), and determining
        the exact point of DOM stability is necessary before further actions.

        :return: The time it took to load and stabilize the DOM in seconds.
        :rtype: float
        """
        script = "return document.body.innerHTML;"
        states = []
        start = datetime.now()
        time_loading = 0
        called_class = self.__class__.__name__

        while True:
            dom = self.driver.execute_script(script)
            states.append(dom)
            # Keep only the last {storage} values of the DOM state
            states = states[-storage:]

            if len(states) == storage:
                # Check if the last DOM states are the same
                time_loading = round(
                    (datetime.now() - start).total_seconds(), 3
                )
                if all(x == states[-1] for x in states):
                    print(
                        f"[Info]: {called_class} DOM loaded "
                        f"in {time_loading} seconds"
                    )
                    return time_loading
                time.sleep(0.2)

            if time_loading > timeout:
                called_class = self.__class__.__name__
                print(f"[Info]: {called_class} DOM loading timeout")
                return False

    def get_element_by_position(
        self, position: int, locator: tuple[str, str], error_message: str = None
    ):
        elements = self.wait_elements(locator)
        try:
            element = elements[position - 1]
        except IndexError as e:
            raise AssertionError(error_message, str(e))

        return self.scroll_to_element_center(element)
