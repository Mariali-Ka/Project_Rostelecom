from selenium.webdriver.common.by import By
from base_page import BasePage

class RecoveryPasswordLocators:
    LOCATOR_WORD_RECOVERY_PHONE = (By.XPATH, "//div[@id='t-btn-tab-phone']")
    LOCATOR_WORD_RECOVERY_MAIL = (By.XPATH, "//div[@id='t-btn-tab-mail']")
    LOCATOR_WORD_RECOVERY_LOGIN = (By.XPATH, "//div[@id='t-btn-tab-login']")
    LOCATOR_WORD_RECOVERY_PERSONAL_ACCOUNT = (By.XPATH, "//div[@id='t-btn-tab-ls']")
    LOCATOR_FIELD_RECOVERY_USERNAME = (By.XPATH, "//input[@id='username']")
    LOCATOR_FIELD_SYMBOLS = (By.XPATH, "//input[@id='captcha']")
    LOCATOR_RECOVERY_BUTTON_CONTINUE = (By.XPATH, "//button[@id='reset']")
    LOCATOR_RECOVERY_LINK_COME_BACK = (By.XPATH, "//button[@id='reset-back']")
    LOCATOR_RECOVERY_WRONG_LOGIN_OR_PICTURES = (By.XPATH, "//span[@id='form-error-message']")
    LOCATOR_PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    LOCATOR_BUTTON_TO_COME_IN_RECOVERY = (By.XPATH, "//button[@id='kc-login']")
    LOCATOR_LINK_FORGOT_PASSWORD_RECOVERY = (By.XPATH, "//a[@id='forgot_password']")
    LOCATOR_WORD_AUTHORIZATION = (By.XPATH, "//h1[contains(text(),'Авторизация')]")





class RecoveryPageHelper(BasePage):

    def click_word_login_recovery(self):
        return self.find_element(RecoveryPasswordLocators.LOCATOR_WORD_RECOVERY_LOGIN, time=2).click()

    def click_word_phone_recovery(self):
        return self.find_element(RecoveryPasswordLocators.LOCATOR_WORD_RECOVERY_PHONE, time=2).click()

    def click_word_mail_recovery(self):
        return self.find_element(RecoveryPasswordLocators.LOCATOR_WORD_RECOVERY_MAIL, time=2).click()

    def click_word_personal_account_recovery(self):
        return self.find_element(RecoveryPasswordLocators.LOCATOR_WORD_RECOVERY_PERSONAL_ACCOUNT, time=2).click()

    def entry_field_phone_or_mail_or_login_or_personalaccount(self, word):
        field_login_recovery = self.find_element(RecoveryPasswordLocators.LOCATOR_FIELD_RECOVERY_USERNAME)
        field_login_recovery.click()
        field_login_recovery.send_keys(word)
        return field_login_recovery

    def entry_password_field(self, word):
        password_field = self.find_element(RecoveryPasswordLocators.LOCATOR_PASSWORD_FIELD)
        password_field.click()
        password_field.send_keys(word)
        return password_field

    def entry_field_symbols(self, word):
        field_symbols = self.find_element(RecoveryPasswordLocators.LOCATOR_FIELD_SYMBOLS)
        field_symbols.click()
        field_symbols.send_keys(word)
        return field_symbols

    def click_button_continue_recovery(self):
        button_continue_recovery = self.find_element(RecoveryPasswordLocators.LOCATOR_RECOVERY_BUTTON_CONTINUE)
        button_continue_recovery.click()
        return button_continue_recovery

    def click_link_come_back_recovery(self):
        link_come_back_recovery = self.find_element(RecoveryPasswordLocators.LOCATOR_RECOVERY_LINK_COME_BACK)
        link_come_back_recovery.click()
        return link_come_back_recovery

    def click_button_to_come_in_recovery(self):
        button_to_come_in_recovery = self.find_element(RecoveryPasswordLocators.LOCATOR_BUTTON_TO_COME_IN_RECOVERY)
        button_to_come_in_recovery.click()
        return button_to_come_in_recovery

    def click_link_forgot_password_recovery(self):
        link_forgot_password_recovery = self.find_element(RecoveryPasswordLocators.LOCATOR_LINK_FORGOT_PASSWORD_RECOVERY)
        link_forgot_password_recovery.click()
        return link_forgot_password_recovery

    def recovery_wrong_login_or_text_with_pictures(self):
        wrong_login_or_text_with_pictures = self.find_element(RecoveryPasswordLocators.LOCATOR_RECOVERY_WRONG_LOGIN_OR_PICTURES)
        return [x.text for x in wrong_login_or_text_with_pictures]

    def recovery_word_authorization_text(self):
        word_authorization_text = self.find_element(RecoveryPasswordLocators.LOCATOR_WORD_AUTHORIZATION)
        value_word_authorization_text = word_authorization_text.text
        return value_word_authorization_text







