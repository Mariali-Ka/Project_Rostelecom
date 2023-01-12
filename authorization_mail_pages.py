from selenium.webdriver.common.by import By
from base_page import BasePage

class AutorizationMAILLocators:
    LOCATOR_WORD_MAIL = (By.XPATH, "//div[@id='t-btn-tab-mail']")
    LOCATOR_EMAIL_MAIL = (By.XPATH, "//input[@id='username']")
    LOCATOR_MAIL_PASSWORD = (By.XPATH, "//input[@id='password']")
    LOCATOR_WORD_EMAIL_MAIL = (By.XPATH, "//span[contains(text(),'Электронная почта')]")
    LOCATOR_MAIL_BUTTON_REMEMBER_ME = (By.XPATH, "//span[@class='rt-checkbox__shape rt-checkbox__shape--circular rt-checkbox__shape--orange']")
    LOCATOR_MAIL_BUTTON_TO_COME_IN = (By.XPATH, "//button[@id='kc-login']")
    LOCATOR_MAIL_WRONG_LOGIN_OR_PASSWORD = (By.XPATH, "//span[@id='form-error-message']")


class MailPageHelper(BasePage):

    def click_word_mail(self):
        return self.find_element(AutorizationMAILLocators.LOCATOR_WORD_MAIL, time=2).click()

    def entry_email_mail(self, word):
        email_mail = self.find_element(AutorizationMAILLocators.LOCATOR_EMAIL_MAIL)
        email_mail.click()
        email_mail.send_keys(word)
        return email_mail

    def entry_mail_password(self, word):
        mail_password = self.find_element(AutorizationMAILLocators.LOCATOR_MAIL_PASSWORD)
        mail_password.click()
        mail_password.send_keys(word)
        return mail_password

    def click_mail_button_remember_me(self):
        mail_button_remember_me = self.find_element(AutorizationMAILLocators.LOCATOR_MAIL_BUTTON_REMEMBER_ME)
        mail_button_remember_me.click()
        return mail_button_remember_me

    def click_mail_button_to_come_in(self):
        mail_button_to_come_in = self.find_element(AutorizationMAILLocators.LOCATOR_MAIL_BUTTON_TO_COME_IN)
        mail_button_to_come_in.click()
        return mail_button_to_come_in

    def mail_wrong_login_or_password(self):
        wrong_login_or_password = self.find_element(AutorizationMAILLocators.LOCATOR_MAIL_WRONG_LOGIN_OR_PASSWORD)
        return [x.text for x in wrong_login_or_password]



