from unittest import TestCase
from EnvEnvironmentSetup import EnvironmentSetup
from Pages.A1_A2_Page.A1A2FormFillingPage import A1A2FormFillingPage
from Pages.LoginPage import LoginPage
from PageValidator.A1A2PageValidator import A1A2PageValidator
from TestData.A1A2TestData import ServiceType, AccountType, ContactInformation, DropDown


class TestAA1A2Form(TestCase):

    @classmethod
    def setUpClass(cls):
        initial_setup = EnvironmentSetup()
        cls.driver = initial_setup.create_browser_instance()
        cls.username = initial_setup.username
        cls.password = initial_setup.password
        initial_setup.navigate_to_home()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # DCASS account test cases
    def test_open_dcass_seoch_account(self):
        login = LoginPage(self.driver)
        login.enter_user_credential(self.username, self.password)
        form_page = A1A2FormFillingPage(self.driver)
        form_page.select_dcass_account_type(AccountType.DCASS)
        form_page.select_account_service_type(ServiceType.OPEN_SEOCH)
        form_page.click_select_account_drop_down(DropDown.NAME)
        form_page.select_account_id()
        form_page.click_add_another_contact()
        form_page.enter_contact_information(ContactInformation.NAME, ContactInformation.POSITION,
                                            ContactInformation.EMAIL, ContactInformation.PHONE)
        form_page.click_next_preview_submit_button()

    def test_open_dcass_hkcc_account(self):
        login = LoginPage(self.driver)
        login.enter_user_credential(self.username, self.password)
        form_page = A1A2FormFillingPage(self.driver)
        form_page.select_dcass_account_type(AccountType.DCASS)
        form_page.select_account_service_type(ServiceType.OPEN_HKCC)
        form_page.click_select_account_drop_down(DropDown.NAME)
        form_page.select_account_id()
        form_page.enter_contact_information(ContactInformation.NAME, ContactInformation.POSITION,
                                            ContactInformation.EMAIL, ContactInformation.PHONE)

    def test_close_dcass_seoch_account(self):
        login = LoginPage(self.driver)
        login.enter_user_credential(self.username, self.password)
        form_page = A1A2FormFillingPage(self.driver)
        form_page.select_dcass_account_type(AccountType.DCASS)
        form_page.select_account_service_type(ServiceType.CLOSE_SEOCH)
        form_page.click_select_account_drop_down(DropDown.NAME)
        form_page.select_account_id()
        form_page.enter_contact_information(ContactInformation.NAME, ContactInformation.POSITION,
                                            ContactInformation.EMAIL, ContactInformation.PHONE)

    def test_close_dcass_hkcc_account(self):
        login = LoginPage(self.driver)
        login.enter_user_credential(self.username, self.password)
        form_page = A1A2FormFillingPage(self.driver)
        form_page.select_dcass_account_type(AccountType.DCASS)
        form_page.select_account_service_type(ServiceType.CLOSE_HKCC)
        form_page.click_select_account_drop_down(DropDown.NAME)
        form_page.select_account_id()
        form_page.enter_contact_information(ContactInformation.NAME, ContactInformation.POSITION,
                                            ContactInformation.EMAIL, ContactInformation.PHONE)

    # OBEP account test cases
    def test_open_obep_seoch_account(self):
        login = LoginPage(self.driver)
        login.enter_user_credential(self.username, self.password)
        form_page = A1A2FormFillingPage(self.driver)
        form_page.select_dcass_account_type(AccountType.OBEP)
        form_page.select_account_service_type(ServiceType.OPEN_SEOCH)
        form_page.click_select_account_drop_down(DropDown.NAME)
        form_page.select_account_id()
        form_page.enter_contact_information(ContactInformation.NAME, ContactInformation.POSITION,
                                            ContactInformation.EMAIL, ContactInformation.PHONE)

    def test_close_obep_seoch_account(self):
        login = LoginPage(self.driver)
        login.enter_user_credential(self.username, self.password)
        form_page = A1A2FormFillingPage(self.driver)
        form_page.select_dcass_account_type(AccountType.OBEP)
        form_page.select_account_service_type(ServiceType.CLOSE_HKCC)
        form_page.click_select_account_drop_down(DropDown.NAME)
        form_page.select_account_id()
        form_page.enter_contact_information(ContactInformation.NAME, ContactInformation.POSITION,
                                            ContactInformation.EMAIL, ContactInformation.PHONE)

    def test_trial_run(self):
        login = LoginPage(self.driver)
        login.enter_user_credential(self.username, self.password)
        #login.enter_user_credential("admin", "admin")
        #adp = A1A2FormFillingPage(self.driver)
        page_validator = A1A2PageValidator(self.driver)
        page_validator.validate_a1_a2_account_details_title()
        page_validator.validate_a1_a2_contact_details_title()
        page_validator.validate_a1_a2_form_title()





