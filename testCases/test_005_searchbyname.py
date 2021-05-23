import time
import pytest
from pageObjects.LoginPageObject import Login
from pageObjects.add_new_customer_page import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.logger.info("************* SearchCustomerByName_005 **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Name **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        time.sleep(2)

        self.logger.info("************* searching customer by Name **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByName("Victoria Terces")
        self.driver.close()
        assert True==status
        self.logger.info("***************  TC_SearchCustomerByName_005 Finished  *********** ")