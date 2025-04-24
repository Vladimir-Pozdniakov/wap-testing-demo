import json
import re
import time
from datetime import datetime

import allure
import requests
from selenium.webdriver.remote.webdriver import WebDriver
from urllib3.exceptions import MaxRetryError, NewConnectionError

from settings import BASE_URL, LOCAL_RUNNER
from utilities.file_management import write_text_to_file

ALLURE_PROJECT = "twitch-mobile"
ALLURE_PROJECT_RESULTS = f"reports/{ALLURE_PROJECT}/results"
PATH_TO_ENV_PROPERTIES = f"{ALLURE_PROJECT_RESULTS}/environment.properties"
PATH_TO_ALLURE_PROPERTIES = f"{ALLURE_PROJECT_RESULTS}/allure.properties"
ALLURE_URL = "http://localhost:5050"


def step(title):
    def wrapper(func):
        def inner(*args, **kwargs):
            try:
                passed_args = re.findall(r"{(.*?)}", title)
                printed_title: str = title
                for passed_arg in passed_args:
                    printed_title = printed_title.replace(
                        f"{{{passed_arg}}}", str(kwargs[passed_arg])
                    )
                print(f"[Step]: {printed_title}")

                return func(*args, **kwargs)
            except Exception:
                time.sleep(0.8)
                now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                file_name = f"{now}-{func.__name__}-FAILED"
                print(
                    "[Info]: Start capturing a screenshot "
                    "due to the test failure:"
                )
                try:
                    driver: WebDriver = args[0].driver
                    screenshot = driver.get_screenshot_as_png()
                    allure.attach(
                        screenshot,
                        name=f"{file_name}.png",
                        attachment_type=allure.attachment_type.PNG,
                    )
                except Exception as e:
                    print(e)

                print(
                    "[Info]: Finish capturing a screenshot "
                    "due to the test failure."
                )

                raise

        return allure.step(title)(inner)

    return wrapper


def attach_log_to_report(log: str | list[str] | dict, name: str) -> None:
    if isinstance(log, list) and len(log) == 0 or len(log) == 0:
        return None

    if isinstance(log, str):
        allure.attach(log, name, allure.attachment_type.TEXT)
    else:
        log = json.dumps(log, indent=0)
        allure.attach(log, name, allure.attachment_type.JSON)
    return None


def attach_screenshot_to_report(image: bytes | str, name: str) -> None:
    name = name.lower().replace(" ", "_")
    name = name if name.endswith(".png") else f"{name}.png"
    if isinstance(image, bytes):
        allure.attach(image, name, allure.attachment_type.PNG)
    else:
        allure.attach.file(image, name, allure.attachment_type.PNG)


def generate_report_at_the_end() -> None:
    if LOCAL_RUNNER:
        try:
            allure_url = (
                f"{ALLURE_URL}" f"/generate-report?project_id={ALLURE_PROJECT}"
            )
            requests.get(url=allure_url)
            print("[Post-condition]: Generate Allure report.")
        except (
            NewConnectionError,
            requests.exceptions.ConnectionError,
            MaxRetryError,
        ):
            print(
                "\n[Post-condition]: \033[31mAllure Report "
                "Server is not accessible!\033[0m"
            )


def clean_report_results() -> None:
    if LOCAL_RUNNER:
        try:
            allure_url = (
                f"{ALLURE_URL}" f"/clean-results?project_id={ALLURE_PROJECT}"
            )
            response: dict = requests.get(url=allure_url).json()
            response_message = response.get("meta_data", {}).get("message")
            expected = (
                "Results successfully cleaned for project_id "
                f"'{ALLURE_PROJECT}'"
            )
            assert response_message == expected
            print("[Pre-condition]: Clean Allure report.")
        except (
            NewConnectionError,
            requests.exceptions.ConnectionError,
            MaxRetryError,
        ):
            print(
                "\n[Pre-condition]: \033[31mAllure Report "
                "Server is not accessible!\033[0m"
            )


def add_allure_report_properties() -> None:
    write_text_to_file(
        PATH_TO_ENV_PROPERTIES,
        [
            f"Server={BASE_URL}",
        ],
    )
