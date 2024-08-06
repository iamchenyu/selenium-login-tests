from selenium.webdriver.common.by import By
import pytest
import time

class TestExceptions:
    # Test case 1: NoSuchElementException
    @pytest.mark.exceptions
    def test_NoSuchElementException(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        # Click Add button
        add_btn_locator = driver.find_element(By.ID, "add_btn")
        add_btn_locator.click()
        # Wait for Row 2 to show up
        # time.sleep(5)
        driver.implicitly_wait(5)
        # Verify Row 2 input field is displayed
        row2_parent = driver.find_element(By.ID, "row2")
        row2_input = row2_parent.find_element(By.TAG_NAME, "input")
        assert row2_input.is_displayed(), "Row2 Input should display on the screen"




