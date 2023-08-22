from selenium.webdriver.common.by import By
from SampleProjects.POMProjectDemo.Locators.locators import Locators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_xpath = Locators.username_textbox_xpath
        self.password_textbox_xpath = Locators.password_textbox_xpath
        self.login_button_xpath = Locators.login_button_xpath
        self.login_invalid_username_password_xpath = Locators.invalid_username_password_message_xpath

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.username_textbox_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def check_invalid_username_password_massage(self):
        msg = self.driver.find_element(By.XPATH, self.login_invalid_username_password_xpath).text
        return msg

