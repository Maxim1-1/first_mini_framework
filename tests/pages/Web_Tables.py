from selenium.webdriver.common.by import By
from task3.framework.base.BasePage import BasePage
from task3.framework.base.Form import Form
from task3.framework.base.Button import Button
from task3.framework.base.Text import Text
from task3.framework.base.Link import Link


class Locators:
    BUTTON_ADD = "//*[contains(@id,'addNewRecordButton')]"
    FORM_REGISTRATION = "//*[contains(@id,'registration-form-modal')]"
    READ_DATA_USER = "//*[contains(@class,'-odd')]"
    REGISTRATION_FORM = "//*[contains(@id,'registration-form-modal')]"
    FIRST_NAME_FIELD = "//input[contains(@id,'firstName')]"
    LAST_NAME_FIELD = "//input[contains(@id,'lastName')]"
    EMAIL_FIELD = "//input[contains(@id,'userEmail')]"
    AGE_FIELD = "//input[contains(@id,'age')]"
    SALARY_FIELD = "//input[contains(@id,'salary')]"
    DEPARTAMENT_FIELD = "//input[contains(@id,'department')]"
    SUBMIT = "//*[contains(@id,'submit')]"
    USERS = "//*[@class='rt-table']/*[@class='rt-tbody']/div"
    DELETE_USERS = "// *[contains( @ id, 'delete-record')]"


class WebTables(BasePage):
    __button_add_click = Button(By.XPATH, Locators.BUTTON_ADD)
    __button_submit_click = Button(By.XPATH, Locators.SUBMIT)
    __validate_form_registragion = Text(By.XPATH, Locators.FORM_REGISTRATION)

    def button_add_click(self):
        self.__button_add_click.click_on_button()

    def button_submit_click(self):
        self.__button_submit_click.click_on_button()

    def is_validate_form_registragion(self):
        return self.__validate_form_registragion.validate_text_on_page()

    def read_value_first_user(self, number_user=1):
        users_list = []
        elements = Form(By.XPATH, Locators.USERS).get_fields()
        for users in elements:
            if users.text != '       ':
                users_list.append((users.text).splitlines())
        return users_list[number_user - 1]

    def read_value_last_user(self):
        users_list = []
        elements = Form(By.XPATH, Locators.USERS).get_fields()
        for users in elements:
            if users.text != '       ':
                users_list.append((users.text).splitlines())
        return users_list[- 1]

    def delete_new_user(self):
        elements = Link(By.XPATH, Locators.DELETE_USERS).get_links()
        elements[-1].click()

    def data_entry(self, users):
        input_name = Form(By.XPATH, Locators.FIRST_NAME_FIELD).entering_data_in_field(users[0])
        input_last_name = Form(By.XPATH, Locators.LAST_NAME_FIELD).entering_data_in_field(users[1])
        input_age = Form(By.XPATH, Locators.AGE_FIELD).entering_data_in_field(users[2])
        input_email = Form(By.XPATH, Locators.EMAIL_FIELD).entering_data_in_field(users[3])
        input_salary = Form(By.XPATH, Locators.SALARY_FIELD).entering_data_in_field(users[4])
        input_departament = Form(By.XPATH, Locators.DEPARTAMENT_FIELD).entering_data_in_field(users[5])

    def read_count_users(self):
        elements = Link(By.XPATH, Locators.DELETE_USERS).get_links()
        return len(elements)

    def is_validate_add_user(self,before,after):
        if len(set(before) & set(after)) <=5:
            return True
        else:
            return False
