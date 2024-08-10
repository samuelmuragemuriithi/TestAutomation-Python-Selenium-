"""
6. Test Framework Design:
 Design a basic test automation framework structure using Python and Selenium. 
 Explain the key components of your framework, such as test data management, page object model, and reporting.

"""
# Project Structure


# SeleniumTestFramework/
# │
# ├── tests/
# │   ├── test_login.py
# │   ├── test_checkout.py
# │   └── __init__.py
# │
# ├── pages/
# │   ├── login_page.py
# │   ├── checkout_page.py
# │   └── __init__.py
# │
# ├── data/
# │   ├── test_data.json
# │   └── config.yaml
# │
# ├── reports/
# │   ├── report.html
# │   └── screenshots/
# │
# ├── utils/
# │   ├── base_test.py
# │   ├── logger.py
# │   └── __init__.py
# │
# ├── requirements.txt
# ├── conftest.py
# └── README.md


# pytest --html=reports/report.html
