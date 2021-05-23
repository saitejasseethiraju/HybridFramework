# from selenium import webdriver


class Login:
    _textbox_username_id = "Email"
    _textbox_password_id = "Password"
    _button_login_xpath = "//*[contains(@class,'login-button')]"
    _link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element_by_id(self._textbox_username_id).clear()
        self.driver.find_element_by_id(self._textbox_username_id).send_keys(username)

    def set_password(self, password):
        self.driver.find_element_by_id(self._textbox_password_id).clear()
        self.driver.find_element_by_id(self._textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self._button_login_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self._link_logout_linktext).click()
