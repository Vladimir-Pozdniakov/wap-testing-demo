import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL").rstrip("/")
HEADLESS = bool(int(os.getenv("HEADLESS", 1)))
LOCAL_RUNNER = bool(int(os.getenv("LOCAL_RUNNER", 0)))
