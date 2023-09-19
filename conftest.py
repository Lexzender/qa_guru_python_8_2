from selene.support.shared import browser
import pytest

@pytest.fixture(scope="session", autouse=True)
def browser_config():
    browser.config.window_width = 1280
    browser.config.window_height = 720
    yield
    browser.quit()