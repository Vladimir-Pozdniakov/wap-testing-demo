import pytest

from framework.pom.bottom_menu.bottom_menu import BottomMenu
from framework.pom.browse_page.browse_page import BrowsePage
from framework.pom.category_page.category_page import CategoryPage
from framework.pom.home_page.home_page import HomePage
from framework.pom.streamer_profile_page.streamer_profile_page import (
    StreamerProfilePage,
)


@pytest.fixture
def home_page(driver):
    return HomePage(driver)


@pytest.fixture
def bottom_menu(driver):
    return BottomMenu(driver)


@pytest.fixture
def browse_page(driver):
    return BrowsePage(driver)


@pytest.fixture
def category_page(driver):
    return CategoryPage(driver)


@pytest.fixture
def streamer_profile_page(driver):
    return StreamerProfilePage(driver)
