from selenium.webdriver.common.by import By
import pytest
import time
from page_objects.login_page import LoginPage

class TestNegativeScenarios:
    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message", [("incorrectUser", "Password123", "Your username is invalid!"),("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        login_page = LoginPage(driver)
        # Open page
        login_page.open_page()
        # Type username into Username field
        # Type password into Password field
        # Push Submit button
        login_page.login(username, password)

        # Check url has not been changed
        assert login_page.curr_url == "https://practicetestautomation.com/practice-test-login/"
        # Verify error message is displayed
        # Verify error message text is Your username is invalid!
        assert login_page.curr_error_msg == expected_error_message
