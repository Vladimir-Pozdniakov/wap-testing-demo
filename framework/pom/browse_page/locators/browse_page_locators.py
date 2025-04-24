from selenium.webdriver.common.by import By


class BrowsePageLocators:
    search_field = (By.CSS_SELECTOR, "[type=search]")
    search_results = (By.CSS_SELECTOR, "li [title]")
