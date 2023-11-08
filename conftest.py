from selene.support.shared import browser
import pytest


@pytest.fixture()
def open_browser():
    browser.open('https://google.com')
    yield
    browser.quit()

@pytest.fixture(autouse=True)
def browser_window():
    browser.config.window_width = 1080
    browser.config.window_height = 800

@pytest.fixture
def no_result_search():
    yield
    print("По Вашему запросу результатов не найдено")
