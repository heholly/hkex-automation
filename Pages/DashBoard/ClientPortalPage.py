# File Name: ClientPortalPage
# Author: Karthick Dhakshinamoorthy
# Python Version: 3.5.4

from Utils import Helper
from selenium.webdriver.common.keys import Keys
from Pages.BasePage import BasePage
from TestData.ClientPortalTestData import UserBanner


class ClientPortalPage(BasePage):

    # user banner locator
    GREETING_MESSAGE = "div.topbar > ul > li:nth-child(2) > div > P"
    SEARCH_ICON = ".topbar > ul > li:nth-child(3) > button"
    SEARCH_INPUT_FIELD = ".topbar >form > div > input"
    SEARCH_BUTTON = ".topbar > form > div > button"
    DEFAULT_LANGUAGE = ".language-select > a > span"
    LANGUAGE_DROPDOWN = ".language-select > a > i:nth-child(3)"
    HK_LANGUAGE = ".language-select.show > div > a:nth-child(2)"
    CH_LANGUAGE = ".language-select.show > div > a:nth-child(3)"
    EN_LANGUAGE = ".language-select.show > div > a:nth-child(4)"
    WEATHER_DATE = ".topbar > ul > li:nth-child(2) > p:nth-child(1)"
    WEATHER_TEMP = ".topbar > ul > li:nth-child(2) > p:nth-child(3)"
    WEATHER_ICON = ".topbar > ul > li:nth-child(2) > i"
    USER_NAME = ".profile-left > div[class='username']"
    DEPARTMENT_NAME = ".profile-left > div[class='department']"
    PROFILE_DROP_DOWN = ".profile-right > a"
    USER_PROFILE = ".profile-right > div > a:nth-child(2) > span"
    USER_SETTING = ".profile-right > div > a:nth-child(3) > span"
    SIGN_OUT = ".profile-right > div > a:nth-child(4) > span"
    USER_PROFILE_ICON = ".profile-right > div > a:nth-child(2) > i"
    USER_SETTING_ICON = ".profile-right > div > a:nth-child(3) > i"
    SIGN_OUT_ICON = ".profile-right > div > a:nth-child(4) > i"

    def click_search_icon(self):
        self.logger.info("click search  icon")
        self.find_element_by_css_selector(self.SEARCH_ICON).click()
        self.logger.info("clicked search  icon")

    def click_search_button(self):
        self.find_element_by_css_selector(self.SEARCH_BUTTON).click()
        self.logger.info("clicked search  button")

    def enter_search_by_keyboard(self, input_string):
        self.logger.info("enter  search  string and hit keyboard enter")
        element = self.find_element_by_css_selector(self.SEARCH_INPUT_FIELD)
        element.send_keys(input_string)
        element.send_keys(Keys.ENTER)

    def enter_search_item(self, input_string):
        self.logger.info("enter  search  string")
        element = self.find_element_by_css_selector(self.SEARCH_INPUT_FIELD)
        element.send_keys(input_string)

    def get_search_box_index_value(self):
        element = self.find_element_by_css_selector(self.SEARCH_INPUT_FIELD)
        index_value = element.value_of_css_property("z-index")
        return index_value

    def get_greeting_message(self):
        self.logger.info("Fetch  user greeting")
        greeting_message = self.get_text(self.GREETING_MESSAGE)
        return greeting_message

    def get_default_language_value(self):
        self.logger.info("Fetch  default language")
        default_language = self.get_text(self.DEFAULT_LANGUAGE)
        return default_language

    def click_language_drop_down(self):
        self.logger.info("select language drop down")
        self.find_element_by_css_selector(self.LANGUAGE_DROPDOWN).click()

    def select_hk_language(self):
        self.logger.info("select Cantonese language")
        self.find_element_by_css_selector(self.HK_LANGUAGE).click()

    def select_ch_language(self):
        self.logger.info("select Mandarin language")
        self.find_element_by_css_selector(self.CH_LANGUAGE).click()

    def select_en_language(self):
        self.logger.info("select English language")
        self.find_element_by_css_selector(self.EN_LANGUAGE).click()

    def get_weather_date(self):
        self.logger.info("get weather date")
        actual_date = self.get_text(self.WEATHER_DATE)
        actual_result = Helper.trim_white_space(actual_date)
        return actual_result

    def get_temperature(self):
        self.logger.info("get temperature")
        actual_result = self.get_text(self.WEATHER_TEMP)
        return actual_result

    def get_weather_icon(self):
        self.logger.info("check weather icon exist")
        element = self.find_element_by_css_selector(self.WEATHER_ICON)
        element.is_displayed()
        actual_result = element.value_of_css_property(UserBanner.DISPLAY)
        return actual_result

    def get_user_profile_icon(self):
        self.logger.info("check user profile icon exist")
        element = self.find_element_by_css_selector(self.USER_PROFILE_ICON)
        element.is_displayed()
        actual_result = element.value_of_css_property(UserBanner.DISPLAY)
        return actual_result

    def get_user_settings_icon(self):
        self.logger.info("check user settings icon exist")
        element = self.find_element_by_css_selector(self.USER_SETTING_ICON)
        element.is_displayed()
        actual_result = element.value_of_css_property(UserBanner.DISPLAY)
        return actual_result

    def get_sign_out_icon(self):
        self.logger.info("check sign out icon exist")
        element = self.find_element_by_css_selector(self.SIGN_OUT_ICON)
        element.is_displayed()
        actual_result = element.value_of_css_property(UserBanner.DISPLAY)
        return actual_result

    def get_user_name(self):
        self.logger.info("get user name")
        user_name = self.get_text(self.USER_NAME)
        return user_name

    def get_department_name(self):
        self.logger.info("get department name")
        department_name = self.get_text(self.DEPARTMENT_NAME)
        return department_name

    def get_user_menu_profile_text(self):
        self.logger.info("get user menu profile name")
        profile_text = self.get_text(self.USER_PROFILE)
        return profile_text

    def get_user_setting_text(self):
        self.logger.info("get user setting name")
        setting_text = self.get_text(self.USER_SETTING)
        return setting_text

    def get_sign_out_text(self):
        self.logger.info("get sign out")
        sign_out = self.get_text(self.SIGN_OUT)
        return sign_out

    def click_user_menu_drop_down(self):
        self.logger.info("click user menu drop down")
        self.find_element_by_css_selector(self.PROFILE_DROP_DOWN).click()

    def select_user_profile(self):
        self.logger.info("select user profile")
        self.find_element_by_css_selector(self.USER_PROFILE).click()

    def select_user_settings(self):
        self.logger.info("select user setting")
        self.find_element_by_css_selector(self.USER_SETTING).click()

    def click_sign_out(self):
        self.logger.info("select sign out")
        self.find_element_by_css_selector(self.SIGN_OUT).click()



