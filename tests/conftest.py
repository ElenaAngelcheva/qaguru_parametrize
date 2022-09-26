import pytest
from selene.support.shared import browser


@pytest.fixture(params=[(1980, 1080), (1500, 1000), (1300, 1100), (600, 800)])
def browser_windows_size(request):
    return request


@pytest.fixture()
def browser_size(browser_windows_size):
    browser.open('https://github.com')
    width = browser_windows_size.param[0]
    height = browser_windows_size.param[1]
    browser.driver.set_window_size(width=width, height=height)


@pytest.fixture()
def browser_open():
    browser.open('https://github.com')











