from selenium.webdriver.common.by import By
import pytest
import time

class TestNegativeScenarios:
    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message", [("incorrectUser", "Password123", "Your username is invalid!"),("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, open_login_page, username, password, expected_error_message):
        # Open browser
        # Open page
        # driver.get("https://practicetestautomation.com/practice-test-login/")
        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username)
        # Type password Password123 into Password field
        password_locator = driver.find_element(By.ID, "password")
        password_locator.send_keys(password)
        # Push Submit button
        submit_btn_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_btn_locator.click()
            # give it more time to show the error message
        time.sleep(1)
        # Check url has not been changed
        assert driver.current_url == "https://practicetestautomation.com/practice-test-login/"
        # Verify error message is displayed
        error_locator = driver.find_element(By.ID, "error")
        assert error_locator.is_displayed(), "Error message should display on the screen"
        # Verify error message text is Your username is invalid!
        assert error_locator.text == expected_error_message

    # @pytest.mark.login
    # @pytest.mark.negative
    # def test_negative_username(self, driver):
    #     # Open browser
    #     # Open page
    #     driver.get("https://practicetestautomation.com/practice-test-login/")
    #     # Type username incorrectUser into Username field
    #     username_locator = driver.find_element(By.ID, "username")
    #     username_locator.send_keys("incorrectUser")
    #     # Type password Password123 into Password field
    #     password_locator = driver.find_element(By.ID, "password")
    #     password_locator.send_keys("Password123")
    #     # Push Submit button
    #     submit_btn_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
    #     submit_btn_locator.click()
    #         # give it more time to show the error message
    #     time.sleep(1)
    #     # Check url has not been changed
    #     assert driver.current_url == "https://practicetestautomation.com/practice-test-login/"
    #     # Verify error message is displayed
    #     error_locator = driver.find_element(By.ID, "error")
    #     assert error_locator.is_displayed(), "Error message should display on the screen"
    #     # Verify error message text is Your username is invalid!
    #     assert error_locator.text == "Your username is invalid!"

    # @pytest.mark.login
    # @pytest.mark.negative    
    # def test_negative_password(self, driver):
    #     # Open Browser
    #     # Open page
    #     driver.get("https://practicetestautomation.com/practice-test-login/")
    #     # Type username student into Username field
    #     username_locator = driver.find_element(By.ID, "username")
    #     username_locator.send_keys("student")
    #     # Type password incorrectPassword into Password field
    #     password_locator = driver.find_element(By.XPATH, "//input[@id='password']")
    #     password_locator.send_keys("incorrectPassword")
    #     # Push Submit button
    #     submit_btn_locator = driver.find_element(By.CLASS_NAME, "btn")
    #     submit_btn_locator.click()
    #     time.sleep(1)
    #     # Check url has not been changed
    #     assert driver.current_url == "https://practicetestautomation.com/practice-test-login/", "URL should stay the same"
    #     # Verify error message is displayed
    #     error_locator = driver.find_element(By.ID, "error")
    #     assert error_locator.is_displayed(), "Error message should be displayed on the screen"
    #     # Verify error message text is Your password is invalid!
    #     assert error_locator.text == "Your password is invalid!", "Error message should be 'Your password is invalid!'"