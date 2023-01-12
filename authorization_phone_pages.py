from selenium.webdriver.common.by import By
from base_page import BasePage

class AutorizationLocators:
    LOCATOR_WORD_PHONE = (By.XPATH, "//div[@id='t-btn-tab-phone']")
    LOCATOR_NUMBER_PHONE = (By.XPATH, "//input[@id='username']")
    LOCATOR_EMAIL_PASSWORD = (By.XPATH, "//input[@id='password']")
    LOCATOR_BUTTON_REMEMBER_ME = (By.XPATH, "//span[@class='rt-checkbox__shape rt-checkbox__shape--circular rt-checkbox__shape--orange']")
    LOCATOR_BUTTON_TO_COME_IN = (By.XPATH, "//button[@id='kc-login']")
    LOCATOR_INVALID_PHONE_FORMAT = (By.XPATH, "//span[contains(text(),'Неверный формат телефона')]")
    LOCATOR_WRONG_LOGIN_OR_PASSWORD = (By.XPATH, "//span[@id='form-error-message']")
    LOCATOR_FORGOT_PASSWORD = (By.XPATH, "//a[@id='forgot_password']")
    LOCATOR_BUTTON_COME_BACK = (By.XPATH, "//button[@id='reset-back']")


class SearchPageHelper(BasePage):

    def click_word_phono(self):
        return self.find_element(AutorizationLocators.LOCATOR_WORD_PHONE, time=2).click()

    def entry_phone_number(self, word):
        phone_number = self.find_element(AutorizationLocators.LOCATOR_NUMBER_PHONE)
        phone_number.click()
        phone_number.send_keys(word)
        return phone_number

    def entry_email_password(self, word):
        email_password = self.find_element(AutorizationLocators.LOCATOR_EMAIL_PASSWORD)
        email_password.click()
        email_password.send_keys(word)
        return email_password

    def click_button_remember_me(self):
        button_remember_me = self.find_element(AutorizationLocators.LOCATOR_BUTTON_REMEMBER_ME)
        button_remember_me.click()
        return button_remember_me

    def click_button_to_come_in(self):
        button_to_come_in = self.find_element(AutorizationLocators.LOCATOR_BUTTON_TO_COME_IN)
        button_to_come_in.click()
        return button_to_come_in

    def entry_negative_phone_number(self):
        negative_phone_number = self.find_element(AutorizationLocators.LOCATOR_INVALID_PHONE_FORMAT)
        return [x.text for x in negative_phone_number]

    def entry_negative_number_or_password(self):
        negative_number_or_password = self.find_element(AutorizationLocators.LOCATOR_WRONG_LOGIN_OR_PASSWORD)
        return [x.text for x in negative_number_or_password]

    def click_forgot_password(self):
        forgot_password = self.find_element(AutorizationLocators.LOCATOR_FORGOT_PASSWORD)
        forgot_password.click()
        return forgot_password

    def click_button_come_back(self):
        button_come_back = self.find_element(AutorizationLocators.LOCATOR_BUTTON_COME_BACK)
        button_come_back.click()
        return button_come_back





