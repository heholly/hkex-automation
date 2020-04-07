# File Name: EnvironmentSetUp
# Author: Karthick Dhakshinamoorthy
# Python Version: 3.5.4

from Pages.BasePage import BasePage


class A1A2FormFillingPage(BasePage):

    # Account details locators

    FORM_TITLE = ".afFormTitle.guidetextdraw.guidefield > div > p:nth-child(1)"
    SECTION1 = ".guidePanelNode.accountInformation.form-section-panel > div > div > div:nth-child(1)"
    SECTION2 = ".guidePanelNode.panel2.form-section-panel > div > div > div:nth-child(1)"

    SELECT_DCASS = "div.guideRadioButtonItem.guideFieldVerticalAlignment.accountType.hkex-radio " \
                   "> div:nth-child(2) > label"
    SERVICE_TYPE = "div.guideRadioButtonItem.guideFieldVerticalAlignment.serviceType.hkex-radio " \
                   "> div:nth-child(2)> label"
    PARTICIPANT_ID1 = "div.dropdown-menu.open.show > ul> li:nth-child(2) > a"
    P_ID_DROP_DOWN_BUTTON = "div.btn-group.bootstrap-select > button > span.filter-option.pull-left"

    CP_NAME = ".guideFieldNode.guideTextBox.name.input-section.shortDescriptionOnTop.af-field-empty " \
              "> div:nth-child(3) > input"
    CP_POSITION = ".guideFieldNode.guideTextBox.position.input-section.shortDescriptionOnTop.af-field-empty " \
                  "> div:nth-child(3) > input"
    CP_EMAIL = ".guideFieldNode.guideTextBox.email.input-section.shortDescriptionOnTop.af-field-empty " \
               "> div:nth-child(2) > input"
    CP_NUMBER = ".guideFieldNode.guideTextBox.phone.input-section.shortDescriptionOnTop.af-field-empty " \
                "> div:nth-child(3) > input"
    ADD_ANOTHER_CONTACT = ".guideFieldWidget.guideFieldButtonWidget.xfaButton " \
                          "> button[aria-label='+ ADD ANOTHER Contact ']"
    NEXT_REVIEW_SUBMIT = ".guideFieldNode.guideButton.submit.review-and-submit.shortDescriptionOnTop.af-field-empty" \
                         " > div > button"

    #  Section 1 Account details

    def get_form_title(self):
        form_title = self.get_text(self.FORM_TITLE)
        return form_title

    def get_section1_title(self):
        section1 = self.get_text(self.SECTION1)
        return section1

    def get_section2_title(self):
        section2 = self.get_text(self.SECTION2)
        return section2

    def select_dcass_account_type(self, account_type):
        self._select_list_value(self.SELECT_DCASS, account_type)
        return self

    def select_account_service_type(self, service_type):
        self._select_list_value(self.SERVICE_TYPE, service_type)
        return self

    def click_select_account_drop_down(self, default_dropdown_value):
        self._select_list_value(self.P_ID_DROP_DOWN_BUTTON, default_dropdown_value)
        return self

    def select_account_id(self):
        self.find_element_by_css_selector(self.PARTICIPANT_ID1).click()

    # Section 2 Contact information

    def click_add_another_contact(self):
        self.find_element_by_css_selector(self.ADD_ANOTHER_CONTACT).click()

    def enter_contact_information(self, name, ps, mail, number):
        self._enter_contact_person_name(name)
        self._enter_contact_person_position(ps)
        self._enter_contact_person_email(mail)
        self._enter_contact_telephone_number(number)

    # Footer button function

    def click_next_preview_submit_button(self):
        self.find_element_by_css_selector(self.NEXT_REVIEW_SUBMIT).click()

    # private methods

    def _enter_contact_person_name(self, name):
        self._select_contact_information_list_value(self.CP_NAME, name)
        return self

    def _enter_contact_person_position(self, position):
        self._select_contact_information_list_value(self.CP_POSITION, position)
        return self

    def _enter_contact_person_email(self, mail):
        self._select_contact_information_list_value(self.CP_EMAIL, mail)
        return self

    def _enter_contact_telephone_number(self, number):
        self._select_contact_information_list_value(self.CP_NUMBER, number)
        return self

    def _select_list_value(self, locator, types):
        element = self.find_elements_by_css_selector(locator)
        if not element:
            self.logger.error("***{0} account type element value is null***".format(types))
        else:
            for e in element:
                if e.text == types:
                    e.click()
                    self.logger.info("!!!selected {0} account type!!!".format(types))
                    break
        return self

    def _select_contact_information_list_value(self, locator, names):
        element = self.find_elements_by_css_selector(locator)
        if not element:
            self.logger.error("***Contact information name filed is null")
        else:
            count = 0
            for e in element:
                for name in names[count]:
                    e.send_keys(name)
                count = count + 1
        return self