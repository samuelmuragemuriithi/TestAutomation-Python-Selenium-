import pytest
from selenium import webdriver

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = 'reports/report.html'

@pytest.hookimpl(trylast=True)
def pytest_exception_interact(node, call, report):
    if report.failed:
        driver = node.instance.driver
        screenshot_file = f"reports/screenshots/{node.name}.png"
        driver.save_screenshot(screenshot_file)
