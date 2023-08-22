from selenium.webdriver.common.by import By
from SampleProjects.POMProjectDemo.Locators.locators import Locators


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.welcome_link_xpath = Locators.welcome_link_xpath
        self.logout_link_xpath = Locators.logout_link_xpath
        self.side_bar_search_xpath = Locators.search_input_xpath
        self.list_search = Locators.search_input_list_xpath

    def click_welcome(self):
        self.driver.find_element(By.XPATH, self.welcome_link_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_link_xpath).click()

    def input_for_side_bar_search(self, search_side_bar):
        self.driver.find_element(By.XPATH, self.side_bar_search_xpath).clear()
        self.driver.find_element(By.XPATH, self.side_bar_search_xpath).send_keys(search_side_bar)

    def list_ul_side_bar_search(self):
        side_bar_search_list = self.driver.find_element(By.XPATH, self.list_search)
        items = side_bar_search_list.find_element(By.TAG_NAME, 'ul')
        return items
