from selenium.webdriver.common.by import By
from base_page import BasePage

class TemporaryCodeLocators:
    LOCATOR_WORD_PHONE_AUTHORIZATION = (By.XPATH, "//div[@id='t-btn-tab-phone']")
    LOCATOR_NUMBER_PHONE_AUTHORIZATION = (By.XPATH, "//input[@id='username']")
    LOCATOR_EMAIL_PASSWORD_AUTHORIZATION = (By.XPATH, "//input[@id='password']")
    LOCATOR_BUTTON_REMEMBER_ME_AUTHORIZATION = (By.XPATH, "//span[@class='rt-checkbox__shape rt-checkbox__shape--circular rt-checkbox__shape--orange']")
    LOCATOR_BUTTON_TO_COME_IN_AUTHORIZATION = (By.XPATH, "//button[@id='kc-login']")
    LOCATOR_PRIVATE_OFFICE = (By.XPATH, "//a[@id='lk-btn']")
    LOCATOR_PRIVATE_OFFICE_USERNAME = (By.XPATH, "//h2[@class='sc-bvFjSx iqOiiv']")
    LOCATOR_PRIVATE_OFFICE_USERNAME_LOG_OFF = (By.XPATH, "//span[contains(text(),'Выйти')]")
    LOCATOR_EMAIL_PHONE_AUTHORIZATION_CODE = (By.XPATH, "//input[@id='address']")
    LOCATOR_BUTTON_TO_GET_CODE = (By.XPATH, "//button[@id='otp_get_code']")
    LOCATOR_CHANGE_PHONE_OR_MAIL_CODE = (By.XPATH, "//button[@name='otp_back_phone']")
    LOCATOR_FORM_WORK_HINT = (By.XPATH, "//p[contains(text(),'Укажите почту или номер телефона, на которые необх')]")
    LOCATOR_BUTTON_NUMBER_1_CODE = (By.XPATH, "//input[@id='rt-code-0']")
    LOCATOR_BUTTON_NUMBER_2_CODE = (By.XPATH, "//input[@id='rt-code-1']")
    LOCATOR_BUTTON_NUMBER_3_CODE = (By.XPATH, "//input[@id='rt-code-2']")
    LOCATOR_BUTTON_NUMBER_4_CODE = (By.XPATH, "//input[@id='rt-code-3']")
    LOCATOR_BUTTON_NUMBER_5_CODE = (By.XPATH, "//input[@id='rt-code-4']")
    LOCATOR_BUTTON_NUMBER_6_CODE = (By.XPATH, "//input[@id='rt-code-5']")





class TemporaryCodePageHelper(BasePage):

    def click_word_phono_authoriz(self):
        return self.find_element(TemporaryCodeLocators.LOCATOR_WORD_PHONE_AUTHORIZATION, time=2).click()

    def entry_phone_number_authoriz(self, word):
        phone_number_authoriz = self.find_element(TemporaryCodeLocators.LOCATOR_NUMBER_PHONE_AUTHORIZATION)
        phone_number_authoriz.click()
        phone_number_authoriz.send_keys(word)
        return phone_number_authoriz

    def entry_email_password_authoriz(self, word):
        email_password_authoriz = self.find_element(TemporaryCodeLocators.LOCATOR_EMAIL_PASSWORD_AUTHORIZATION)
        email_password_authoriz.click()
        email_password_authoriz.send_keys(word)
        return email_password_authoriz

    def entry_email_phone_authoriz_code(self, word):
        email_phone_authoriz_code = self.find_element(TemporaryCodeLocators.LOCATOR_EMAIL_PHONE_AUTHORIZATION_CODE)
        email_phone_authoriz_code.click()
        email_phone_authoriz_code.send_keys(word)
        return email_phone_authoriz_code

    def entry_number_1_code(self, word):
        number_1_code = self.find_element(TemporaryCodeLocators.LOCATOR_BUTTON_NUMBER_1_CODE)
        number_1_code.click()
        number_1_code.send_keys(word)
        return number_1_code

    def entry_number_2_code(self, word):
        number_2_code = self.find_element(TemporaryCodeLocators.LOCATOR_BUTTON_NUMBER_2_CODE)
        number_2_code.click()
        number_2_code.send_keys(word)
        return number_2_code

    def entry_number_3_code(self, word):
        number_3_code = self.find_element(TemporaryCodeLocators.LOCATOR_BUTTON_NUMBER_3_CODE)
        number_3_code.click()
        number_3_code.send_keys(word)
        return number_3_code

    def entry_number_4_code(self, word):
        number_4_code = self.find_element(TemporaryCodeLocators.LOCATOR_BUTTON_NUMBER_4_CODE)
        number_4_code.click()
        number_4_code.send_keys(word)
        return number_4_code

    def entry_number_5_code(self, word):
        number_5_code = self.find_element(TemporaryCodeLocators.LOCATOR_BUTTON_NUMBER_5_CODE)
        number_5_code.click()
        number_5_code.send_keys(word)
        return number_5_code

    def entry_number_6_code(self, word):
        number_6_code = self.find_element(TemporaryCodeLocators.LOCATOR_BUTTON_NUMBER_6_CODE)
        number_6_code.click()
        number_6_code.send_keys(word)
        return number_6_code

    def click_button_remember_authoriz(self):
        button_remember_authoriz = self.find_element(TemporaryCodeLocators.LOCATOR_BUTTON_REMEMBER_ME_AUTHORIZATION)
        button_remember_authoriz.click()
        return button_remember_authoriz

    def click_button_to_come_in_authoriz(self):
        button_to_come_in_authoriz = self.find_element(TemporaryCodeLocators.LOCATOR_BUTTON_TO_COME_IN_AUTHORIZATION)
        button_to_come_in_authoriz.click()
        return button_to_come_in_authoriz

    def click_link_private_office(self):
        link_private_office = self.find_element(TemporaryCodeLocators.LOCATOR_PRIVATE_OFFICE)
        link_private_office.click()
        return link_private_office

    def click_link_private_office_username(self):
        link_private_office_username = self.find_element(TemporaryCodeLocators.LOCATOR_PRIVATE_OFFICE_USERNAME)
        link_private_office_username.click()
        return link_private_office_username

    def click_link_office_username_log_off(self):
        link_office_username_lod_off = self.find_element(TemporaryCodeLocators.LOCATOR_PRIVATE_OFFICE_USERNAME_LOG_OFF)
        link_office_username_lod_off.click()
        return link_office_username_lod_off

    def click_button_to_get_code(self):
        button_to_get_code = self.find_element(TemporaryCodeLocators.LOCATOR_BUTTON_TO_GET_CODE)
        button_to_get_code.click()
        return button_to_get_code

    def click_link_change_phone_code(self):
        link_change_phone_code = self.find_element(TemporaryCodeLocators.LOCATOR_CHANGE_PHONE_OR_MAIL_CODE)
        link_change_phone_code.click()
        return link_change_phone_code

    def form_work_hint_code(self):
        form_work_hint = self.find_element(TemporaryCodeLocators.LOCATOR_FORM_WORK_HINT)
        return [x.text for x in form_work_hint]










