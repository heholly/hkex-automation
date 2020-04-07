# File Name: LoginPage
# Author: Karthick Dhakshinamoorthy
# Python Version: 3.5.4

from Pages.BasePage import BasePage


class LoginPage(BasePage):

    USERNAME = ".form-group:nth-child(1) > input"
    PASSWORD = ".form-group:nth-child(2) > input"
    SUBMIT_BUTTON = ".form-group:nth-child(4) > input"

    def enter_user_credential(self, username, password):
        self.logger.info("Enter user name")
        name = self.find_element_by_css_selector(self.USERNAME)
        name.send_keys(username)
        self.logger.info("Enter password")
        pass_w = self.find_element_by_css_selector(self.PASSWORD)
        pass_w.send_keys(password)
        self.find_element_by_css_selector(self.SUBMIT_BUTTON).click()
        self.logger.info("!!!successfully logged in")