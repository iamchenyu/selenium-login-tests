from selenium import webdriver
import pytest

# if we want to run tests in all browsers, we can use `params`
# @pytest.fixture(params=["chrome", "safari"])
@pytest.fixture(params=["chrome"])
def driver(request):
    browser = request.param
    # to print out messages in fixture, use -s flag
    print(f"start in driver fixture - {browser}")
    if browser == "chrome":
        # the option keeps the browser open after the process has ended
        # so long as the quit command is not sent to the driver
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        my_driver = webdriver.Chrome(options=options)
    elif browser == "safari":
        # --browser=safari
        my_driver = webdriver.Safari()      
    else:
        raise TypeError(f"Browser can only be chrome or safari, but got {browser}")
    # implictly wait
    # my_driver.implicitly_wait(5)
    yield my_driver
    print(f"end in driver fixture - {browser}")
    my_driver.quit()

# @pytest.fixture
# def driver(request):
#     browser = request.config.getoption("--browser")
#     # to print out messages in fixture, use -s flag
#     print(f"start in driver fixture - {browser}")
#     if browser == "chrome":
#         # the option keeps the browser open after the process has ended
#         # so long as the quit command is not sent to the driver
#         options = webdriver.ChromeOptions()
#         options.add_experimental_option("detach", True)
#         my_driver = webdriver.Chrome(options=options)
#     elif browser == "safari":
#         # --browser=safari
#         my_driver = webdriver.Safari()
#     else:
#         raise TypeError(f"Browser can only be chrome or safari, but got {browser}")
#     yield my_driver
#     print(f"end in driver fixture - {browser}")
#     my_driver.quit()

@pytest.fixture
def open_exception_page(driver):
    driver.get("https://practicetestautomation.com/practice-test-exceptions/")

@pytest.fixture
def open_login_page(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser option: chrome or safari")