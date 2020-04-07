# File Name: EnvironmentSetUp
# Author: Karthick Dhakshinamoorthy
# Python Version: 3.5.4

import logging
import os
import sys
import json
import base64
from _datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class EnvironmentSetup(object):

    def __init__(self):
        hkex_test_data = open(os.path.expanduser('~/.HKEXSTRC'))
        test_data = json.loads(hkex_test_data.read())
        logging.info(test_data)
        hkex_test_data.close()

        if "base_url" in test_data:
            self.base_url = test_data["base_url"]

        if "username" in test_data:
            self.username = test_data["username"]

        if "password" in test_data:
            p = test_data["password"]
            self.password = self._password(p)

        if "browser" in test_data:
            self.browser = test_data["browser"]

        if "width" in test_data:
            self.width = test_data["width"]

        if "height" in test_data:
            self.height = test_data["height"]

    def create_browser_instance(self):
        if self.browser == "chrome":
            self.chrome_browser()
        elif self.browser == "IE":
            self.le_browser()
        return self.driver

    def le_browser(self):
        driver_path = self._get_driver_path()
        self.driver = webdriver.Ie(driver_path+"chromedriver.exe")
        logging.info("IE driver Instance created")
        self._set_browser_capabilities()

    def chrome_browser(self):
        driver_path = self._get_driver_path()
        self.driver = webdriver.Chrome(driver_path+"chromedriver.exe")
        logging.info("chrome driver Instance created")
        option = Options()
        option.add_argument("'disable-infobars'")
        self._set_browser_capabilities()

    def _get_driver_path(self):
        home = os.path.expanduser("~")
        driver_path = home + "\\AppData\\Local\Programs\\Python\\Python35\\Scripts\\"
        return driver_path

    def _set_browser_capabilities(self):
        self._set_browser_windows_size()
        self._set_default_implicit_wait_time()

    def _set_default_implicit_wait_time(self):
        self.driver.implicitly_wait(40)

    def _set_browser_windows_size(self):
        self.driver.set_window_size(width=self.width, height=self.height)

    def navigate_to_home(self):
        self.driver.get(self.base_url)

    def take_screen_shot(self):
        home = os.path.expanduser("~")
        screenshot_path = home + "\\ScreenShot"
        if sys.exc_info()[0]:  # Returns the info of exception being handled
            fail_url = self.driver.current_url
            print(fail_url)
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
            self.driver.get_screenshot_as_file(screenshot_path+'/%s.png' % now)
            fail_screenshot_url = 'http://debugtool/screenshots/%s.png' % now
            print(fail_screenshot_url)

    @staticmethod
    def _password(p):
        p_value = str(p)
        before_slice = base64.b64decode(p_value)
        password = str(before_slice).replace("'", "").lstrip("b")
        return password
