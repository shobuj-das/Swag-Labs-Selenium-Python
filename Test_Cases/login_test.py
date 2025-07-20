import pytest
from pages.login_page import LoginPage

def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url

@pytest.mark.parametrize("username, password",[
    ("standard_user", "invalidPass"),
    ("invalid_user", "secret_sauce"),
    ("invalid_user", "invalidPass"),
    ("", "secret_sauce"),
    ("standard_user", ""),
    ("", "")
])
def test_unsuccessful_login(driver, username, password):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(username, password)
    assert login_page.is_login_fail()

@pytest.mark.parametrize("username, password",[
    ("visual_user", "secret_sauce"),
    ("error_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("locked_out_user", "secret_sauce"),
    ("standard_user", "secret_sauce")
])
def test_all_successful_login(driver, username, password):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(username, password)
    assert login_page.is_login_successful()
