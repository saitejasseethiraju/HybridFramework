import time
import pytest
from pageObjects.LoginPageObject import Login
from pageObjects.add_new_customer_page import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen



class Test_SearchCustomerByEmail_004:
    baseurl = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("************* SearchCustomerByEmail_004 **********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Email **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("************* searching customer by emailID **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        self.driver.close()
        assert True == status
        self.logger.info("***************  TC_SearchCustomerByEmail_004 Finished  *********** ")