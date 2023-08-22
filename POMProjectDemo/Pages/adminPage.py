from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from SampleProjects.POMProjectDemo.Locators.locators import Locators

from SampleProjects.POMProjectDemo.GeneralFunction.functions import Usefulfunctions

from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string


class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_button_xpath = Locators.add_user_button
        # self.user_role_dropdown_xpath = Locators.user_role_dropdown
        self.listbox_dropdown_xpath = Locators.add_user_listbox_dropdown
        self.user_role_choose_admin_dropdown_xpath = Locators.add_user_user_role_dropdown
        self.employee_name_input_xpath = Locators.add_user_employee_name_input
        self.status_dropdown_xpath = Locators.add_user_status_dropdown
        self.user_name_xpath = Locators.add_user_username_input
        self.password_xpath = Locators.add_user_password_input
        self.confirm_password_xpath = Locators.add_user_confirm_password_input
        self.save_button_xpath = Locators.add_user_save_button

        # self.admin_sideBar = Locators.admin_side_bar_click
        # self.admin_page_title = Locators.titleAdminPage

    def get_into(self):
        Usefulfunctions.login_valid(self)
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers')

    def add_user(self):
        self.get_into()
        self.driver.find_element(By.XPATH, self.add_button_xpath).click()
        self.driver.find_element(By.XPATH, self.user_role_choose_admin_dropdown_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        user_role_options = wait.until(
            EC.visibility_of_all_elements_located((By.XPATH, self.listbox_dropdown_xpath)))
        user_role_options[0].click()
        # self.driver.find_element(By.XPATH, self.user_role_dropdown_xpath).click()
        input_text = "a"
        random_username = ''.join(
            random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(5))
        # Find the <input> element
        self.driver.find_element(By.XPATH, self.employee_name_input_xpath).send_keys(input_text)
        time.sleep(2)
        wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.listbox_dropdown_xpath)))
        employee_names_options = wait.until(
            EC.visibility_of_all_elements_located((By.XPATH, self.listbox_dropdown_xpath)))
        employee_names_options[0].click()
        self.driver.find_element(By.XPATH, self.status_dropdown_xpath).click()
        status_options = wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.listbox_dropdown_xpath)))
        status_options[0].click()
        self.driver.find_element(By.XPATH, self.user_name_xpath).send_keys(random_username)
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(
            "newAdmin123")
        self.driver.find_element(By.XPATH, self.confirm_password_xpath).send_keys(
            "newAdmin123")
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()

    def search_system_users(self):
        self.get_into()
        # table_row = self.driver.find_element(By.CLASS_NAME, 'oxd-table')

        rowname=self.driver.find_element(By.XPATH,"//div[contains(@class,'oxd-table-card-cell') and .//div[contains(@class, 'data')]]")
        check=rowname.text

        table = self.driver.find_element(By.XPATH, "//div[contains(@class,'oxd-table-card-cell')]")
        table_row = table.find_element(By.XPATH, "//div[contains(@class,'data')]")
        name=table_row.text

        # "//div[contains(@role,'listbo')]"
        # table_row = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "oxd-table-row")))
        type=table_row.type
        # for i in table_row:
        #     i.text
        # ee=table_row(1)

        # Find elements within the row and extract information
        # employee_name = table_row.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div[1]/div/div/div[1]/div[1]')
        empl= table_row.find_element(By.XPATH,"//div[contains(@class,'card')]")
        # oxd - table - card
        # ss=empl.text
        name=empl(1)

        # username = table_row.find_element(By.CSS_SELECTOR, ".data:nth-child(2)").text
        # user_role = table_row.find_element(By.CSS_SELECTOR, ".data:nth-child(3)").text
        # status = table_row.find_element(By.CSS_SELECTOR, ".data:nth-child(4)").text

        # Print the extracted information
        # print(f"Employee Name: {employee_name}")
        # print(f"Username: {username}")
        # print(f"User Role: {user_role}")
        # print(f"Status: {status}")






        # self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input').send_keys(rows[0].text)
        # self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()







