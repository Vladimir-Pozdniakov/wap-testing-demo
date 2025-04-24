from selenium.webdriver.common.by import By


class BottomMenuLocators:
    home = (By.XPATH, "//div[contains(text(), 'Home')]")
    browse = (By.XPATH, "//div[contains(text(), 'Browse')]")
    activity = (By.XPATH, "//div[contains(text(), 'Activity')]")
    profile = (By.XPATH, "//div[contains(text(), 'Profile')]")
