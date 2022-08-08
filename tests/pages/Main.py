from selenium.webdriver.common.by import By
from task3.framework.base.BasePage import BasePage
from task3.framework.base.Button import Button
from task3.framework.base.Text import Text


class Main(BasePage):
    BUTTON_ALERT_FRAME_WINDOWS = "//*[contains(@class,'category-cards')]//*[contains(text(),'Alerts')]"
    BUTTON_ELEMENTS = "//*[contains(@class,'category-cards')]//*[contains(text(),'Elements')]"
    MENU_MAIN_VALIDATE = "//*[contains(@class,'category-cards')]"

    __alerts_windows_frame_click = Button(By.XPATH, BUTTON_ALERT_FRAME_WINDOWS)
    __elements_click = Button(By.XPATH, BUTTON_ELEMENTS)
    __validate_main_page_open = Text(By.XPATH, MENU_MAIN_VALIDATE)

    def alerts_windows_frame_click(self):
        self.__alerts_windows_frame_click.click_on_button()

    def elements_click(self):
        self.__elements_click.click_on_button()

    def is_validate_main_page_open(self):
        return self.__validate_main_page_open.validate_text_on_page()
