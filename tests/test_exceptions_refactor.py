from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.exception_page import ExceptionPage
import pytest

class TestExceptions:
    # Test case 1: NoSuchElementException
    @pytest.mark.exceptions
    @pytest.mark.temp
    def test_no_such_element_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open_page()
        exception_page.click_add_button()
        assert exception_page.is_row2_input_displayed, "Row2 Input should display on the screen"

    # Test case 2: ElementNotInteractableException
    @pytest.mark.exceptions
    @pytest.mark.temp
    def test_element_not_interactable_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open_page()
        exception_page.click_add_button()
        exception_page.type_row2_input("Cheese")
        exception_page.click_save2_button()
        assert exception_page.confirmation_text == "Row 2 was saved", "Confirmation message should appear on the screen"

    # Test case 3: InvalidElementStateException or JavascriptException
    @pytest.mark.exceptions
    @pytest.mark.temp
    def test_invalid_element_state_exception(self,driver):
        exception_page = ExceptionPage(driver)
        exception_page.open_page()
        exception_page.click_edit_button()
        exception_page.clear_row1_input()
        exception_page.type_row1_input("Cheese")
        exception_page.click_save1_button()
        new_input_value = exception_page.get_row1_input_value()
        assert new_input_value == "Cheese", f"Row1 input should be updated to Cheese, but got {new_input_value}"
    
    # Test case 4: StaleElementReferenceException
    @pytest.mark.exceptions
    @pytest.mark.temp
    def test_stale_element_reference_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open_page()
        exception_page.click_add_button()
        assert exception_page.is_instructions_not_displayed, "Instruction element should not be displayed"

    # Test case 5: TimeoutException
    @pytest.mark.exceptions
    @pytest.mark.temp
    def test_timeout_exception(self,driver):
        exception_page = ExceptionPage(driver)
        exception_page.open_page()
        exception_page.click_add_button()
        assert exception_page.is_row2_input_displayed, "Second input should be displayed"
        