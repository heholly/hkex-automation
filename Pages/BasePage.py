# File Name: BasePage
# Author: Karthick Dhakshinamoorthy
# Python Version: 3.5.4

import sys
import os
import unittest
from datetime import datetime
from Utils import Logger


class BasePage(object):

    def __init__(self, selenium_driver):
        self.driver = selenium_driver
        self.logger = Logger.logger

    # find by element  selectors
    def find_element_by_css_selector(self, locator):
        return self.driver.find_element_by_css_selector(locator)

    def find_elements_by_css_selector(self, locator):
        return self.driver.find_elements_by_css_selector(locator)

    # find element selectors
    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def get_text(self, locator):
        element = self.find_element_by_css_selector(locator)
        return element.text
