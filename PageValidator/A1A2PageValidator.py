# File Name: AlA2PagValidator
# Author: Karthick Dhakshinamoorthy
# Python Version: 3.5.4

from Pages.A1_A2_Page.A1A2FormFillingPage import A1A2FormFillingPage
from Utils.GenericValidator import GenericValidator


class A1A2PageValidator(A1A2FormFillingPage):

    validator = GenericValidator()

    def validate_a1_a2_form_title(self):
        expected_result = "DCASS ACCOUNT MAINTENANCE"
        actual_result = A1A2FormFillingPage.get_form_title(self)
        self.validator.verify_two_values_are_equal(actual_result, expected_result)

    def validate_a1_a2_account_details_title(self):
        expected_result = "SECTION 1 | ACCOUNT DETAILS"
        actual_result = A1A2FormFillingPage.get_section1_title(self)
        self.validator.verify_two_values_are_equal(actual_result, expected_result)

    def validate_a1_a2_contact_details_title(self):
        expected_result = "SECTION 2 | CONTACT INFORMATION"
        actual_result = A1A2FormFillingPage.get_section2_title(self)
        self.validator.verify_two_values_are_equal(actual_result, expected_result)