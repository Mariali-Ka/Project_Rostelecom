from selenium.webdriver.common.by import By
from base_page import BasePage

class YaSearchLocators:

    LOCATOR_LINK_REGISTRATION = (By.XPATH, "//a[@id='kc-register']")
    LOCATOR_NAME_REGISTRATION = (By.XPATH, "//input[@name='firstName']")
    LOCATOR_FAMILY_REGISTRATION = (By.XPATH, "//input[@name='lastName']")
    LOCATOR_FIELD_REGION_REGISTRATION = (By.XPATH, "rt-input-container rt-select__input")
    LOCATOR_REGISTRATION_LINK_COME_BACK = (By.XPATH, "//button[@id='reset-back']")
    LOCATOR_REGISTRATION_WORD_TEXT = (By.XPATH, "//h1[contains(text(),'Регистрация')]")
    LOCATOR_REGISTRATION_COMMENT_BY_NAME_OR_FAMILY = (By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")
    LOCATOR_REGISTRATION_EMAIL_OR_PHONE = (By.XPATH, "//input[@id='address']")
    LOCATOR_REGISTRATION_COMMENT_BY_EMAIL_OR_PHONE = (By.XPATH, "//span[contains(text(),'Введите телефон в формате +7ХХХХХХХХХХ или +375XXX')]")
    LOCATOR_PASSWORD_REGISTRATION = (By.XPATH, "//input[@id='password']")
    LOCATOR_COMMENT_LENGTH_PASSWORD_REGISTRATION = (By.XPATH, "(//*[text()='Длина пароля должна быть не менее 8 символов'])[1]")
    LOCATOR_COMMENT_UPPERCASE_PASSWORD_REGISTRATION = (By.XPATH, "//span[contains(text(),'Пароль должен содержать хотя бы одну заглавную бук')]")
    LOCATOR_COMMENT_LOWERCASE_PASSWORD_REGISTRATION = (By.XPATH, "//span[contains(text(),'Пароль должен содержать хотя бы одну прописную бук')]")
    LOCATOR_COMMENT_LATIN_PASSWORD_REGISTRATION = (By.XPATH, "//span[contains(text(),'Пароль должен содержать только латинские буквы')]")
    LOCATOR_COMMENT_SYMBOLS_PASSWORD_REGISTRATION = (By.XPATH, "//span[contains(text(),'Пароль должен содержать хотя бы 1 спецсимвол или х')]")
    LOCATOR_PASSWORD_CONFIRMATION_REGISTRATION = (By.XPATH, "//input[@id='password-confirm']")
    LOCATOR_BUTTON_REGISTER = (By.XPATH, "//button[@name='register']")
    LOCATOR_REGISTRATION_ACCOUNT_EXISTS = (By.XPATH, "//h2[contains(text(),'Учётная запись уже существует')]")
    LOCATOR_BUTTON_LOGIN_TO_ACCOUNT = (By.XPATH, "//button[@name='gotoLogin']")
    LOCATOR_LINK_PASSWORD_RECOVERY = (By.XPATH, "//a[@id='reg-err-reset-pass']")



class SearchHelper(BasePage):

    def click_word_registration(self):
        return self.find_element(YaSearchLocators.LOCATOR_LINK_REGISTRATION, time=2).click()

    def click_button_register(self):
        button_register = self.find_element(YaSearchLocators.LOCATOR_BUTTON_REGISTER)
        button_register.click()
        return button_register

    def click_button_login_to_account(self):
        button_login_to_account = self.find_element(YaSearchLocators.LOCATOR_BUTTON_LOGIN_TO_ACCOUNT)
        button_login_to_account.click()
        return button_login_to_account

    def click_link_password_recovery(self):
        link_password_recovery = self.find_element(YaSearchLocators.LOCATOR_LINK_PASSWORD_RECOVERY)
        link_password_recovery.click()
        return link_password_recovery

    def word_name_registration(self, word):
        name_registration = self.find_element(YaSearchLocators.LOCATOR_NAME_REGISTRATION)
        name_registration.click()
        name_registration.send_keys(word)
        return name_registration

    def word_family_registration(self, word):
        family_registration = self.find_element(YaSearchLocators.LOCATOR_FAMILY_REGISTRATION)
        family_registration.click()
        family_registration.send_keys(word)
        return family_registration

    def registration_email_or_phone(self, word):
        address_email_or_phone = self.find_element(YaSearchLocators.LOCATOR_REGISTRATION_EMAIL_OR_PHONE)
        address_email_or_phone.click()
        address_email_or_phone.send_keys(word)
        return address_email_or_phone

    def registration_password(self, word):
        password_registration = self.find_element(YaSearchLocators.LOCATOR_PASSWORD_REGISTRATION)
        password_registration.click()
        password_registration.send_keys(word)
        return password_registration

    def registration_password_confirmation(self, word):
        password_confirmation_registration = self.find_element(YaSearchLocators.LOCATOR_PASSWORD_CONFIRMATION_REGISTRATION)
        password_confirmation_registration.click()
        password_confirmation_registration.send_keys(word)
        return password_confirmation_registration

    def page_registration_word_text(self):
        registration_word_text = self.find_element(YaSearchLocators.LOCATOR_REGISTRATION_WORD_TEXT)
        value_registration_word_text = registration_word_text.text
        return value_registration_word_text

    def registration_comment_by_name_or_family(self):
        note_by_name_text = self.find_element(YaSearchLocators.LOCATOR_REGISTRATION_COMMENT_BY_NAME_OR_FAMILY)
        return [x.text for x in note_by_name_text]

    def registration_comment_by_email_or_phone(self):
        note_by_name_text = self.find_element(YaSearchLocators.LOCATOR_REGISTRATION_COMMENT_BY_EMAIL_OR_PHONE)
        return [x.text for x in note_by_name_text]

    def registration_comment_length_password(self):
        comment_password_text = self.find_element(YaSearchLocators.LOCATOR_COMMENT_LENGTH_PASSWORD_REGISTRATION)
        return [x.text for x in comment_password_text]

    def registration_comment_uppercase_password(self):
        comment_uppercase_password_text = self.find_element(YaSearchLocators.LOCATOR_COMMENT_UPPERCASE_PASSWORD_REGISTRATION)
        return [x.text for x in comment_uppercase_password_text]

    def registration_comment_lowercase_password(self):
        comment_lowercase_password_text = self.find_element(YaSearchLocators.LOCATOR_COMMENT_LOWERCASE_PASSWORD_REGISTRATION)
        return [x.text for x in comment_lowercase_password_text]

    def registration_comment_latin_password(self):
        comment_latin_password_text = self.find_element(YaSearchLocators.LOCATOR_COMMENT_LATIN_PASSWORD_REGISTRATION)
        return [x.text for x in comment_latin_password_text]

    def registration_comment_symbols_password(self):
        comment_symbols_password_text = self.find_element(YaSearchLocators.LOCATOR_COMMENT_SYMBOLS_PASSWORD_REGISTRATION)
        return [x.text for x in comment_symbols_password_text]

    def registration_account_exists(self):
        account_exists_text = self.find_element(YaSearchLocators.LOCATOR_REGISTRATION_ACCOUNT_EXISTS)
        return [x.text for x in account_exists_text]




