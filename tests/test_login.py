from pages.login_page import LoginPage
from config.config import Config
from playwright.sync_api import Playwright, Page, expect


def test_valid_login(page):
    login = LoginPage(page)
    login.navigate(Config.BASE_URL)
    login.login(Config.VALID_USER, Config.VALID_PASSWORD)
    
    expect(page).to_have_url(Config.INVENTORY_URL)
    
def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.navigate(Config.BASE_URL)
    login_page.login(Config.INVALID_USER, Config.VALID_PASSWORD)
    
    error = login_page.get_error_message()
    assert login_page.error_message_invalid_credentials in error

def test_locked_out_user_login(page):
    login_page = LoginPage(page)
    login_page.navigate(Config.BASE_URL)
    login_page.login(Config.LOCKED_OUT_USER, Config.VALID_PASSWORD)
    
    error = login_page.get_error_message()
    assert login_page.error_message_locked_user in error