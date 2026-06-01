from pages.login_page import LoginPage
from config.config import Config

def test_valid_login(page):
    login = LoginPage(page)
    login.navigate(Config.BASE_URL)
    login.login(Config.VALID_USER, Config.VALID_PASSWORD)
    
    assert "inventory" in page.url
    
def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.navigate(Config.BASE_URL)
    login_page.login(Config.INVALID_USER, Config.VALID_PASSWORD)
    
    error = login_page.get_error_message()
    assert "locked out" in error.lower()