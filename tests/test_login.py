import pytest
from pages.login_page import LoginPage

@pytest.mark.smoke
@pytest.mark.regression
class TestLogin:
    """Tests para la funcionalidad de login"""
    
    def test_login_success(self, page):
        """TC001: Login exitoso con usuario valido"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        
        # Validate we're on products page
        assert "/inventory.html" in page.url
        print("TC001: Login exitoso")