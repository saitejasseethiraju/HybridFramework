import time

import pytest

from pageObjects.LoginPageObject import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import  ExcelUtils


class Test_C002__DDT_Login_Ecom:
    baseurl = ReadConfig.get_application_url()
    path = './/TestData/LoginData.xlsx'
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_001_login(self, setup):
        self.logger.info("*********test_002_login*********")
        self.driver = setup
        self.driver.get(url=self.baseurl)
        self.login = Login(self.driver)
        rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
        print(rows)

        lct_status = []  # Empty List

        for row in range(2, rows+1):
            self.username = ExcelUtils.readData(self.path, 'Sheet1', row, 1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1', row, 2)
            self.exp = ExcelUtils.readData(self.path, 'Sheet1', row, 3)
            self.login.set_username(username=self.username)
            self.login.set_password(password=self.password)
            self.login.click_login()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = 'Dashboard / nopCommerce administration'

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*********passed with pass*********")
                    self.logger.info(f'Paaseed {self.username}, {self.password}')
                    assert True
                    self.login.click_logout()
                    lct_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("**** Failed with fail ****")
                    self.driver.save_screenshot(".\\Screenshots\\" + "act_exp_fail.png")
                    self.login.click_logout()
                    lct_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.driver.save_screenshot(".\\Screenshots\\" + "act_not_exp_fail.png")
                    self.logger.info("**** Failed with pass****")
                    lct_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("**** Passed with fail****")
                    lct_status.append("Pass")

        if "Fail" not in lct_status:
            self.logger.info("*******Login DDT test Passed***")
            self.driver.close()
            assert True
        else:
            self.logger.info("*******Login DDT test Failed***")
            self.driver.close()
            assert False

        self.logger.info("*******Login DDT test Completed*****")