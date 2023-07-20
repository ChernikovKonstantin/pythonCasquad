import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
