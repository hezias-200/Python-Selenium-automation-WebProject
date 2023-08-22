import os
import sys
import unittest
from selenium.webdriver.support import expected_conditions as EC
import time

import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from SampleProjects.POMProjectDemo.Pages.adminPage import AdminPage
from SampleProjects.POMProjectDemo.GeneralFunction.functions import Usefulfunctions

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from SampleProjects.POMProjectDemo.Pages.loginPage import LoginPage

from SampleProjects.POMProjectDemo.Pages.homePage import HomePage

options = Options()
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # chrome binary location specified here
options.add_argument("--start-maximized")  # open Browser in maximized mode
options.add_argument("--no-sandbox")  # bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(options=options, executable_path=r'C:\Users\pythonautomation\chromedriver.exe')
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_login_valid(self):
        Usefulfunctions.login_valid(self)

    def test_disconnect_user_valid(self):
        Usefulfunctions.login_valid(self)
        homepage = HomePage(self.driver)
        homepage.click_welcome()
        homepage.click_logout()

    def test_login_invalid_username(self):
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com/')
        login = LoginPage(driver)
        login.enter_username("Admin1")
        login.enter_password("admin123")
        login.click_login()
        invalid_username_message = login.check_invalid_username_password_massage()
        self.assertEqual(invalid_username_message, "Invalid credentials")

    def test_login_invalid_password(self):
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com/')
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin1234444444")
        login.click_login()
        invalid_username_password_message = login.check_invalid_username_password_massage()
        self.assertEqual(invalid_username_password_message, "Invalid credentials")

    def test_input_search_side_bar_homepage(self):
        input_search = "Ad"
        driver = self.driver

        Usefulfunctions.login_valid(self)
        homepage = HomePage(driver)
        homepage.input_for_side_bar_search(input_search)
        items = homepage.list_ul_side_bar_search()
        try:
            self.assertIn(input_search, items.text)
        except Exception as e:
            print(f"Test 5: We did the search and the input '{input_search}' doesn't exist in list search")
        finally:
            homepage.click_welcome()
            homepage.click_logout()

    def test_admin_page_add_user(self):

        homepage = HomePage(self.driver)
        adminpage = AdminPage(self.driver)
        adminpage.add_user()

        try:
            self.assertEqual(self.driver.current_url,
                             'https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers')
        except:
            raise Exception('The User Not Add')

        finally:
            homepage.click_welcome()
            homepage.click_logout()

    def test_check_if_user_add(self):
        adminpage = AdminPage(self.driver)
        adminpage.search_system_users()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Finished")


if __name__ == '__main__':
    unittest.main()
testRunner = HtmlTestRunner.HTMLTestRunner(output='C:/Users/Hezi Aspir/PycharmProjects/pythonProject5/reports')

# //python -m unittest login.LoginTest
