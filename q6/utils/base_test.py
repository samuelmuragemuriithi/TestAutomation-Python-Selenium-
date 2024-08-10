import pytest
from selenium import webdriver
import yaml

class BaseTest:
    @pytest.fixture(scope="class", autouse=True)
    def setup_class(self, request):
        with open("data/config.yaml", "r") as file:
            config = yaml.safe_load(file)
        self.driver = webdriver.Chrome(executable_path=config['webdriver_path'])
        request.cls.driver = self.driver
        yield
        self.driver.quit()
