import pytest
from page_objects.login_page import LoginPage
from page_objects.loggedin_page import LoggedinPage

class TestPostiveScenarios:
    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        # Go to webpage
        login_page.open_page()

        # Type username student into Username field
        # Type password Password123 into Password field
        # Push Submit button
        login_page.login("student", "Password123")

        loggegin_page = LoggedinPage(driver)

        # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        assert loggegin_page.curr_url == loggegin_page.expected_url

        # Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        assert loggegin_page.curr_h1_text == "Logged In Successfully"

        # Verify button Log out is displayed on the new page
        assert loggegin_page.is_loggedout_btn_displayed


