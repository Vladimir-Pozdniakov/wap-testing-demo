from selenium.webdriver.common.by import By


class CategoryPageLocators:
    article_tile = (By.CSS_SELECTOR, "article")
    profile_name = (By.CSS_SELECTOR, "article [href$='/home']:not([tabindex])")
    live_stream = (By.CSS_SELECTOR, "button img")
