from playwright.sync_api import Playwright

def pytest_configure(config):
    config.option.base_url = "https://www.saucedemo.com"
    config.option.headed = False
    config.option.browser_name = "chromium"