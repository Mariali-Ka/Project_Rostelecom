from selenium.webdriver.common.by import By
from base_page import BasePage

class AutorizationLoginLocators:
    LOCATOR_WORD_LOGIN = (By.XPATH, "//div[@id='t-btn-tab-login']")
    LOCATOR_FIELD_LOGIN = (By.XPATH, "//input[@id='username']")
    LOCATOR_LOGIN_PASSWORD = (By.XPATH, "//input[@id='password']")
    LOCATOR_WORD_FIELD_LOGIN = (By.XPATH, "//span[contains(text(),'Логин')]")
    LOCATOR_LOGIN_BUTTON_REMEMBER_ME = (By.XPATH, "//span[@class='rt-checkbox__shape rt-checkbox__shape--circular rt-checkbox__shape--orange']")
    LOCATOR_LOGIN_BUTTON_TO_COME_IN = (By.XPATH, "//button[@id='kc-login']")
    LOCATOR_YOUR_LOGIN_WHEN_REGISTERING = (By.XPATH, "//span[contains(text(),'Введите логин, указанный при регистрации')]")
    LOCATOR_LOGIN_WRONG_LOGIN_OR_PASSWORD = (By.XPATH, "//span[@id='form-error-message']")



class LoginPageHelper(BasePage):

    def click_word_login(self):
        return self.find_element(AutorizationLoginLocators.LOCATOR_WORD_LOGIN, time=2).click()

    def entry_in_field_login(self, word):
        in_field_login = self.find_element(AutorizationLoginLocators.LOCATOR_FIELD_LOGIN)
        in_field_login.click()
        in_field_login.send_keys(word)
        return in_field_login

    def entry_login_password(self, word):
        login_password = self.find_element(AutorizationLoginLocators.LOCATOR_LOGIN_PASSWORD)
        login_password.click()
        login_password.send_keys(word)
        return login_password

    def click_login_button_remember_me(self):
        login_button_remember_me = self.find_element(AutorizationLoginLocators.LOCATOR_LOGIN_BUTTON_REMEMBER_ME)
        login_button_remember_me.click()
        return login_button_remember_me

    def click_login_button_to_come_in(self):
        login_button_to_come_in = self.find_element(AutorizationLoginLocators.LOCATOR_LOGIN_BUTTON_TO_COME_IN)
        login_button_to_come_in.click()
        return login_button_to_come_in

    def login_wrong_login_or_password(self):
        login_wrong_login_or_password = self.find_element(AutorizationLoginLocators.LOCATOR_LOGIN_WRONG_LOGIN_OR_PASSWORD)
        return [x.text for x in login_wrong_login_or_password]

    def your_login_when_registering(self):
        login_when_registering = self.find_element(AutorizationLoginLocators.LOCATOR_YOUR_LOGIN_WHEN_REGISTERING)
        return [x.text for x in login_when_registering]





