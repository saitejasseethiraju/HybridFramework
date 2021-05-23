import pytest
from selenium import webdriver
from pageObjects.LoginPageObject import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_C001_Login_Ecom:
    baseurl = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_001_homepage_title(self, setup):
        self.logger.info("*********test_001_homepage_title*********")
        self.logger.info("*********Verifying home page title*********")
        self.driver = setup
        self.driver.get(url=self.baseurl)
        act_title = self.driver.title
        if act_title == 'Your store. Login':
            assert True
            self.driver.close()
            self.logger.info("*********homepage_title passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_001_homepage_title.png")
            self.driver.close()
            self.logger.error("*********test_001_homepage_title failed*********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_002_login(self, setup):
        self.logger.info("*********test_002_login*********")
        self.driver = setup
        self.driver.get(url=self.baseurl)
        self.login = Login(self.driver)
        self.login.set_username(username=self.username)
        self.login.set_password(password=self.password)
        self.login.click_login()
        act_title = self.driver.title

        if act_title == 'Dashboard / nopCommerce administration':
            self.logger.info("*********test_002_login paasseed*********")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_002_login.png")
            self.driver.close()
            self.logger.error("*********test_002_login failed*********")
            assert False
