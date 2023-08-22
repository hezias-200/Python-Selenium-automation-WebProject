class Locators():
    # Login page objects
    username_textbox_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'
    password_textbox_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'
    login_button_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    invalid_username_password_message_xpath = '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]'

    # Home page objects
    welcome_link_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span'
    logout_link_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a'
    search_input_xpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input'
    search_input_list_xpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]'

    # Admin page objects
    admin_side_bar_click = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'
    title_admin_page = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input'
    add_user_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'

    # Admin page/Add User
    add_user_user_role_dropdown = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]'
    add_user_employee_name_input = f"//input[@placeholder='Type for hints...']"
    add_user_listbox_dropdown = "//div[contains(@role,'listbo')]"
    add_user_status_dropdown = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div'
    add_user_username_input = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input'
    add_user_password_input = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input'
    add_user_confirm_password_input = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input'
    add_user_save_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]'
