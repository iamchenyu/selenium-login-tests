import pytest
import time
from selenium.webdriver.common.by import By

class TestPostiveScenarios:
    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        # Go to webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")
        # time.sleep(2)

        # Type username student into Username field
        username_locator = driver.find_element(By.NAME, "username")
        username_locator.send_keys("student")

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.ID, "password")
        password_locator.send_keys("Password123")

        # Push Submit button
        submit_btn_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_btn_locator.click()

        time.sleep(5)

        # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        acutal_url = driver.current_url
        assert acutal_url in "https://practicetestautomation.com/logged-in-successfully/"

        # Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        text_locator = driver.find_element(By.TAG_NAME, "h1")
        actual_text = text_locator.text
        assert actual_text == "Logged In Successfully"

        # Verify button Log out is displayed on the new page
        # logout_btn_locator = driver.find_element(By.XPATH, "//a[@class='wp-block-button__link has-text-color has-background has-very-dark-gray-background-color']")
        logout_btn_locator = driver.find_element(By.LINK_TEXT, "Log out")
        assert logout_btn_locator.is_displayed()


