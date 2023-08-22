from SampleProjects.POMProjectDemo.Pages.loginPage import LoginPage


class Usefulfunctions:
    def __init__(self, driver):
        self.driver = driver

    def login_valid(self):
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com/')
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
