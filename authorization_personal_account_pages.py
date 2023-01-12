from selenium.webdriver.common.by import By
from base_page import BasePage

class AutorizationPersonalAccountLocators:
    LOCATOR_WORD_PERSONAL_ACCOUNT = (By.XPATH, "//div[@id='t-btn-tab-ls']")
    LOCATOR_FIELD_PERSONAL_ACCOUNT = (By.XPATH, "//input[@id='username']")
    LOCATOR_PERSONAL_ACCOUNT_PASSWORD = (By.XPATH, "//input[@id='password']")
    LOCATOR_WORD_FIELD_PERSONAL_ACCOUNT = (By.XPATH, "//span[contains(text(),'Лицевой счёт')]")
    LOCATOR_PERSONAL_ACCOUNT_BUTTON_REMEMBER_ME = (By.XPATH, "//span[@class='rt-checkbox__shape rt-checkbox__shape--circular rt-checkbox__shape--orange']")
    LOCATOR_PERSONAL_ACCOUNT_BUTTON_TO_COME_IN = (By.XPATH, "//button[@id='kc-login']")
    LOCATOR_PERSONAL_ACCOUNT_WRONG_LOGIN_OR_PASSWORD = (By.XPATH, "//span[@id='form-error-message']")



class PersonalAccountPageHelper(BasePage):

    def click_word_personal_account(self):
        return self.find_element(AutorizationPersonalAccountLocators.LOCATOR_WORD_PERSONAL_ACCOUNT, time=2).click()

    def entry_in_field_personal_account(self, word):
        field_personal_account = self.find_element(AutorizationPersonalAccountLocators.LOCATOR_FIELD_PERSONAL_ACCOUNT)
        field_personal_account.click()
        field_personal_account.send_keys(word)
        return field_personal_account

    def entry_personal_account_password(self, word):
        personal_account_password = self.find_element(AutorizationPersonalAccountLocators.LOCATOR_PERSONAL_ACCOUNT_PASSWORD)
        personal_account_password.click()
        personal_account_password.send_keys(word)
        return personal_account_password

    def click_personal_account_button_remember_me(self):
        personal_account_button_remember_me = self.find_element(AutorizationPersonalAccountLocators.LOCATOR_PERSONAL_ACCOUNT_BUTTON_REMEMBER_ME)
        personal_account_button_remember_me.click()
        return personal_account_button_remember_me

    def click_personal_account_button_to_come_in(self):
        personal_account_button_to_come_in = self.find_element(AutorizationPersonalAccountLocators.LOCATOR_PERSONAL_ACCOUNT_BUTTON_TO_COME_IN)
        personal_account_button_to_come_in.click()
        return personal_account_button_to_come_in

    def personal_account_wrong_login_or_password(self):
        personal_account_wrong_login_or_password = self.find_element(AutorizationPersonalAccountLocators.LOCATOR_PERSONAL_ACCOUNT_WRONG_LOGIN_OR_PASSWORD)
        return [x.text for x in personal_account_wrong_login_or_password]







