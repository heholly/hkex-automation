# File Name: TestClientPortal
# Author: Karthick Dhakshinamoorthy
# Python Version: 3.5.4

import unittest
from EnvironmentSetup.EnvironmentSetup import EnvironmentSetup
from TestData.ClientPortalTestData import UserBanner
from Pages.LoginPage import LoginPage
from Pages.DashBoard.ClientPortalPage import ClientPortalPage
from PageValidator.ClientPortalPageValidator import ClientPortalPageValidator


class TestClientPortal(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initial_setup = EnvironmentSetup()
        cls.username = cls.initial_setup.username
        cls.password = cls.initial_setup.password

    def setUp(self):
        self.driver = self.initial_setup.create_browser_instance()
        self.initial_setup.navigate_to_home()
        login = LoginPage(self.driver)
        login.enter_user_credential(self.username, self.password)
        self.client_portal = ClientPortalPage(self.driver)
        self.dash_board_validator = ClientPortalPageValidator(self.driver)

    def tearDown(self):
        self.initial_setup.take_screen_shot()
        self.driver.quit()

    def test_user_greeting(self):
        """ HKEXCPFW-191 - [User Banner] Greetings """
        self.client_portal.get_greeting_message()
        self.dash_board_validator.validate_greeting_message()

    def test_user_search_by_mouse(self):
        """ HKEXCPFW-197 - [User Banner] Search Button """
        self.client_portal.click_search_icon()
        self.client_portal.enter_search_item("DCASS")
        self.dash_board_validator.validate_z_index_value()
        self.client_portal.click_search_button()

    def test_user_search_by_keyboard(self):
        """ HKEXCPFW-197 - [User Banner] Search Button """
        self.client_portal.click_search_icon()
        self.client_portal.enter_search_by_keyboard("OBEP")

    def test_switch_language_to_en(self):
        """ HKEXCPFW-208 - [User Banner] Language Selected """
        self.dash_board_validator.validate_default_language_value(UserBanner.EN)
        self.client_portal.click_language_drop_down()
        self.client_portal.select_en_language()
        self.dash_board_validator.validate_default_language_value(UserBanner.EN)

    def test_switch_language_to_hk(self):
        """ HKEXCPFW-208 - [User Banner] Language Selected """
        self.dash_board_validator.validate_default_language_value(UserBanner.EN)
        self.client_portal.click_language_drop_down()
        self.client_portal.select_hk_language()
        self.dash_board_validator.validate_default_language_value(UserBanner.HK)

    def test_switch_language_to_ch(self):
        """ HKEXCPFW-208 - [User Banner] Language Selected """
        self.dash_board_validator.validate_default_language_value(UserBanner.EN)
        self.client_portal.click_language_drop_down()
        self.client_portal.select_ch_language()
        self.dash_board_validator.validate_default_language_value(UserBanner.CH)

    def test_weather_date(self):
        """ HKEXCPFW-209 - [User Banner] Weather Information icon, date and temperature """
        self.dash_board_validator.validate_weather_icon_is_display()
        self.dash_board_validator.validate_weather_date()
        self.dash_board_validator.validate_temperature()

    def test_user_name_department(self):
        """ HKEXCPFW-193 - [User Banner] User Profile Icon and Menu items exist"""
        self.dash_board_validator.validate_user_name_department()
        self.client_portal.click_user_menu_drop_down()
        self.dash_board_validator.validate_user_menu_items()
        self.dash_board_validator.validate_user_menu_items_icons()

    def test_open_user_profile(self):
        """ HKEXCPFW-193 - [User Banner] User Profile open user profile"""
        self.client_portal.click_user_menu_drop_down()
        self.client_portal.select_user_profile()

    def test_open_user_setting(self):
        """ HKEXCPFW-193 - [User Banner] User Profile open user setting"""
        self.client_portal.click_user_menu_drop_down()
        self.client_portal.select_user_settings()

    def test_sign_out_dash_board(self):
        """ HKEXCPFW-193 - [User Banner] User Profile sing out"""
        #self.client_portal.click_user_menu_drop_down()
        self.client_portal.click_sign_out()

