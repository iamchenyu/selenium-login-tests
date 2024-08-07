from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class TestExceptions:
    # Test case 1: NoSuchElementException
    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver, open_exception_page):
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
    def test_element_not_interactable_exception(self, driver, open_exception_page):
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

    @pytest.mark.exceptions
    # Test case 3: InvalidElementStateException or JavascriptException
    def test_invalid_element_state_exception(self,driver,open_exception_page):
        # Open page
        # Click Edit button
        edit_btn_locator = driver.find_element(By.ID, "edit_btn")
        edit_btn_locator.click()
        # Clear input field
        # row1_input = driver.find_element(By.XPATH, "//div[@id='row1']/input")
        # Clear event might happen before finding the element
        # so the better practice is to add wait here
        row1_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='row1']/input"))
        )
        row1_input.clear()
        # Type text into the input field
        row1_input.send_keys("Cheese")
        # Save the new input value
        save_btn_locator = driver.find_element(By.ID, "save_btn")
        save_btn_locator.click()
        # Verify text changed by checking input's value attribute
        new_input_value = row1_input.get_attribute("value")
        assert new_input_value == "Cheese", f"Row1 input should be updated to Cheese, but got {new_input_value}"
    
    @pytest.mark.exceptions
    # Test case 4: StaleElementReferenceException
    def test_stale_element_reference_exception(self, driver, open_exception_page):
        # Open page
        # Find the instructions text element
        # instuctions_locator = driver.find_element(By.ID, "instructions")
        # Push add button
        add_btn_locator = driver.find_element(By.ID, "add_btn")
        add_btn_locator.click()
        # Verify instruction text element is no longer displayed
        instuctions_locator = WebDriverWait(driver,10).until(
            EC.invisibility_of_element_located((By.ID, "instructions"))
        )
        assert instuctions_locator, "Instruction element should not be displayed"

    @pytest.mark.exceptions
    # Test case 5: TimeoutException
    def test_timeout_exception(self,driver,open_exception_page):
        # Open page
        # Click Add button
        add_btn_locator = driver.find_element(By.ID, "add_btn")
        add_btn_locator.click()
        # Wait for 3 seconds for the second input field to be displayed
            # we can change it to 5 seconds to pass the test
        input2 = WebDriverWait(driver,3).until(
            EC.visibility_of_element_located(((By.XPATH, "//div[@id='row2']/input"))), "Timed out for Row 2 to be displayed"
        )
        # Verify second input field is displayed
        assert input2.is_displayed(), "Second input should be displayed"
        