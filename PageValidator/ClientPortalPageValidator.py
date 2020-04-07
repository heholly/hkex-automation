# File Name: DashBoardPageValidator
# Author: Karthick Dhakshinamoorthy
# Python Version: 3.5.4

from Utils import Helper
from TestData.ClientPortalTestData import UserBanner
from Pages.DashBoard.ClientPortalPage import ClientPortalPage
from Utils.GenericValidator import GenericValidator


class ClientPortalPageValidator(ClientPortalPage):

    validator = GenericValidator()

    def validate_greeting_message(self):
        actual_result = UserBanner.Greetings
        expected_result = ClientPortalPage.get_greeting_message(self)
        self.validator.verify_two_values_are_equal(expected_result, actual_result)

    def validate_z_index_value(self):
        actual_result = "101"
        expected_result = ClientPortalPage.get_search_box_index_value(self)
        self.validator.verify_two_values_are_equal(expected_result, actual_result)

    def validate_default_language_value(self, language):
        actual_result = language
        expected_result = ClientPortalPage.get_default_language_value(self)
        self.validator.verify_two_values_are_equal(expected_result, actual_result)

    def validate_weather_date(self):
        expected_result = Helper.get_current_date()
        actual_result = ClientPortalPage.get_weather_date(self)
        self.validator.verify_two_values_are_equal(expected_result, actual_result)

    def validate_temperature(self):
        actual_result = ClientPortalPage.get_temperature(self)
        self.validator.verify_value_is_not_null(actual_result)

    def validate_weather_icon_is_display(self):
        actual_result = ClientPortalPage.get_weather_icon(self)
        expected_result = UserBanner.IN_LINE
        self.validator.verify_two_values_are_equal(expected_result, actual_result)

    def validate_user_menu_items_icons(self):
        self._validate_user_profile_icon_display()
        self._validate_user_settings_icon_display()
        self._validate_sign_out_icon_display()

    def _validate_user_profile_icon_display(self):
        actual__profile_icon = ClientPortalPage.get_user_profile_icon(self)
        expected_result = UserBanner.IN_LINE
        self.validator.verify_two_values_are_equal(expected_result, actual__profile_icon)

    def _validate_user_settings_icon_display(self):
        actual_setting_icon = ClientPortalPage.get_user_settings_icon(self)
        expected_result = UserBanner.IN_LINE
        self.validator.verify_two_values_are_equal(expected_result, actual_setting_icon)

    def _validate_sign_out_icon_display(self):
        actual_sign_out_icon = ClientPortalPage.get_sign_out_icon(self)
        expected_result = UserBanner.IN_LINE
        self.validator.verify_two_values_are_equal(expected_result, actual_sign_out_icon)

    def validate_user_menu_items(self):
        expected_profile = UserBanner.Profile
        expected_setting = UserBanner.Setting
        expected_sign_out = UserBanner.SignOut
        actual_profile = ClientPortalPage.get_user_menu_profile_text(self)
        actual_setting = ClientPortalPage.get_user_setting_text(self)
        actual_sign_out = ClientPortalPage.get_sign_out_text(self)
        self.validator.verify_two_values_are_equal(expected_profile, actual_profile)
        self.validator.verify_two_values_are_equal(expected_setting, actual_setting)
        self.validator.verify_two_values_are_equal(expected_sign_out, actual_sign_out)

    def validate_user_name_department(self):
        actual_user_name = ClientPortalPage.get_user_name(self)
        actual_department = ClientPortalPage.get_department_name(self)
        expected_user_name = UserBanner.Name
        expected_department = UserBanner.DEPT
        self.validator.verify_two_values_are_equal(expected_user_name, actual_user_name)
        self.validator.verify_two_values_are_equal(expected_department, actual_department)