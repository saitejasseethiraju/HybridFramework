import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == 'ie':
        driver = webdriver.Ie()
    elif browser == 'edge':
        print("Launching edge Browser")
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


#### pytest html report####
# it is the hook for adding environment info to html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop commerce'
    config._metadata['Module Name'] = 'customers'
    config._metadata['Tester'] = 'Saiteja'


# it is hook for delete/modify environment info to html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)







