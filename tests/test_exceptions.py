from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class TestExceptions:
    # Test case 1: NoSuchElementException
    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        # Open page - use fixture
        # Click Add button
        add_btn_locator = driver.find_element(By.ID, "add_btn")
        add_btn_locator.click()
        # Wait for Row 2 to show up
        # time.sleep(5)
        # Verify Row 2 input field is displayed
        # row2_div = driver.find_element(By.ID, "row2")
        # row2_input = row2_div.find_element(By.TAG_NAME, "input")
        # or
        # row2_input = driver.find_element(By.XPATH, "//div[@id='row2']/input")
        # explictly wait returns a web element
        row2_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='row2']/input"))
        )
        assert row2_input.is_displayed(), "Row2 Input should display on the screen"

    @pytest.mark.exceptions
    # Test case 2: ElementNotInteractableException
    def test_element_not_interactable_exception(self, driver):
        # Open page - use fixture
        # Click Add button
        add_btn_locator = driver.find_element(By.ID, "add_btn")
        add_btn_locator.click()
        # Wait for the second row to load
        row2_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='row2']/input"))
        )
        # Type text into the second input field
        row2_input.send_keys("Cheese")
        # Push Save button using locator By.name(“Save”) - raise ElementNotInteractableException
        # because there is another invisible button with "Save" name on DOM
        # save_btn_locator = driver.find_element(By.NAME, "Save")
        save_btn_locator = driver.find_element(By.XPATH, "//div[@id='row2']/button[@name='Save']")
        save_btn_locator.click()
        # Verify text saved
        # confirmation_locator = driver.find_element(By.ID, "confirmation")
        confirmation_locator = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "confirmation"))
        )
        assert confirmation_locator.text == "Row 2 was saved", "Confirmation message should appear on the screen"

