from selenium.webdriver.common.by import By
from task3.framework.base.BasePage import BasePage
from task3.framework.base.Link import Link
from task3.framework.base.Text import Text
from task3.framework.base.Driver import Driver


class Links(BasePage):
    HOME_LINK = "//*[contains(@id,'simpleLink')]"
    VALIDATE_LINKS = "//*[contains(@id,'linkWrapper')]"

    __validate_links_form = Text(By.XPATH, VALIDATE_LINKS)
    __link_home_click = Link(By.XPATH, HOME_LINK)

    def switch_to_new_window(self):
        Driver().switch_to_window(-1)

    def switch_to_links_window(self):
        Driver().switch_to_window(0)

    def are_validate_links_form(self):
        return self.__validate_links_form.validate_text_on_page()

    def link_home_click(self):
        self.__link_home_click.click_on_link()
