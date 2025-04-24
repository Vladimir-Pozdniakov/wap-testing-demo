import inspect
import json
import os
from pathlib import Path


def write_text_to_file(path: str, data: list[str]):
    try:
        file_path = Path.cwd() / path
        file_path.parent.mkdir(parents=True, exist_ok=True)
        env_file = file_path.open("w")

        for item in data:
            env_file.write(f"{item}\n")
        env_file.close()
    except (FileNotFoundError, PermissionError) as e:
        print(f"Could not write to the file: {path}\n{e.strerror}")


def read_json_file(path: str) -> dict | list | None:
    try:
        with open(path, "r") as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, FileExistsError):
        return None


def write_file(path: str, data: str) -> None:
    with open(path, "w") as file:
        file.write(data)


def get_test_screenshot_path(file_name: str) -> str:
    """Returns the full path to the screenshot file"""

    file_path = None

    stack = inspect.stack()
    for frame in stack:
        if frame.filename.endswith("_test.py"):
            screenshot_folder = f"{os.path.dirname(frame.filename)}/screenshots"
            os.makedirs(screenshot_folder, exist_ok=True)
            file_path = f"{screenshot_folder}/{file_name}.png"
            break

    return file_path
