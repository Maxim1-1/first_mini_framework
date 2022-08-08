from selenium.webdriver.common.by import By
from task3.framework.base.BasePage import BasePage
from task3.framework.base.Button import Button
from task3.framework.base.Text import Text



class ElementsPage(BasePage):
    WEB_TABLES = "//*[contains(@class,'accordion')]//span[contains(text(),'Web Tables')]"
    WEB_TABLES_VALIDATE = "//*[contains(@class,'Table')]"

    __button_web_tables_click = Button(By.XPATH, WEB_TABLES)
    __validate_form_web_tables = Text(By.XPATH, WEB_TABLES_VALIDATE)

    def button_web_tables_click(self):
        self.__button_web_tables_click.click_on_button()

    def is_validate_form_web_tables(self):
        return self.__validate_form_web_tables.validate_text_on_page()