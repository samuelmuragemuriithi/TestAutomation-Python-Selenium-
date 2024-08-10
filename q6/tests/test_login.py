import pytest
from pages.login_page import LoginPage
import json

class TestLogin(BaseTest):
    @pytest.fixture(autouse=True)
    def setup(self):
        self.login_page = LoginPage(self.driver)

    def test_valid_login(self):
        with open('data/test_data.json') as f:
            data = json.load(f)
        self.login_page.enter_username(data['valid_credentials']['username'])
        self.login_page.enter_password(data['valid_credentials']['password'])
        self.login_page.click_login()
        assert "Dashboard" in self.driver.title

    def test_invalid_login(self):
        with open('data/test_data.json') as f:
            data = json.load(f)
        self.login_page.enter_username(data['invalid_credentials']['username'])
        self.login_page.enter_password(data['invalid_credentials']['password'])
        self.login_page.click_login()
        assert "Login Failed" in self.driver.page_source
