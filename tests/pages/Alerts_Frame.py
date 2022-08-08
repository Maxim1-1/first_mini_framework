from selenium.webdriver.common.by import By
from task3.framework.utils import Utils
from task3.framework.base.BasePage import BasePage
from task3.framework.base.Button import Button
from task3.framework.base.Text import Text
from task3.framework.base.Driver import Driver


class Locator:
    BROWSER_WIN_MENU = "//*[contains(@class,'accordion')]//span[contains(text(),'Browser Windows')]"
    ALERT_MENU = "//*[contains(@class,'accordion')]//span[contains(text(),'Alerts')]"
    ALERTS_FORM_VALIDATE = "//*[contains(@id,'javascriptAlertsWrapper')]"
    BUTTON_TO_SEE_ALERTS = "//*[contains(@id,'alertButton')]"
    BUTTON_CONFIRM = "//*[contains(@id,'confirmButton')]"
    BROWSER_WINDOWS_VALIDATE = "//*[contains(@id,'browserWindows')]"
    SELECTED_CONFIRM_TEXT = "//*[contains(@id,'confirmResult')]"
    BUTTON_PROMPT = "//*[contains(@id,'promtButton')]"
    PROMPT_TEXT_RESULT = "//*[contains(@id,'promptResult')]"
    NASTED_FRAMES_MENU = "//*[contains(@class,'accordion')]//span[contains(text(),'Nested')]"
    NASTED_FRAMES_VALIDATE = "//*[contains(@id,'Wrapper')]"


class AlertsPage(BasePage):
    __button_browser_windows_click = Button(By.XPATH, Locator.BROWSER_WIN_MENU)
    __element_alerts_click = Button(By.XPATH, Locator.ALERT_MENU)
    __validate_form_alert = Text(By.XPATH, Locator.ALERTS_FORM_VALIDATE)
    __button_to_see_alert_click = Button(By.XPATH, Locator.BUTTON_TO_SEE_ALERTS)
    __validate_browser_windows_form = Text(By.XPATH, Locator.BROWSER_WINDOWS_VALIDATE)
    __button_confirm_click = Button(By.XPATH, Locator.BUTTON_CONFIRM)
    __button_prompt_click = Button(By.XPATH, Locator.BUTTON_PROMPT)
    __button_prompt_text = Button(By.XPATH, Locator.PROMPT_TEXT_RESULT)
    __button_nested_frame_click = Button(By.XPATH, Locator.NASTED_FRAMES_MENU)
    value_generate = Utils().generate_random_string()
    text = value_generate

    def button_browser_windows_click(self):
        self.__button_browser_windows_click.click_on_button()

    def element_alerts_click(self):
        self.__element_alerts_click.click_on_button()

    def is_validate_form_alert(self):
        return self.__validate_form_alert.validate_text_on_page()

    def button_to_see_alert_click(self):
        self.__button_to_see_alert_click.click_on_button()

    def click_alert_OK(self):
        Driver().accept_alert()

    def is_validate_browser_windows_form(self):
        return self.__validate_browser_windows_form.validate_text_on_page()

    def button_confirm_click(self):
        self.__button_confirm_click.click_on_button()

    def button_prompt_click(self):
        self.__button_prompt_click.click_on_button()

    def input_text_in_alert(self):
        Driver().alert_send(self.value_generate)

    def button_prompt_text(self):
        return self.__button_prompt_text.button_get_text()

    def button_nested_frame_click(self):
        self.__button_nested_frame_click.click_on_button()

    def is_validate_button_to_see(self):
        value = Utils().read_data_json('test_data.json', 'BUTTON_TO_SEE_TEXT')
        if value in Driver().alert_get_text():
            return True
        else:
            return False

    def is_validate_button_confirm(self):
        value = Utils().read_data_json('test_data.json', 'ALERT_BUTTON_CONFIRM_TEXT')
        if value in Driver().alert_get_text():
            return True
        else:
            return False

    def is_validate_button_prompt(self):
        value = Utils().read_data_json('test_data.json', 'ALERT_BUTTON_PROMT')
        if value in Driver().alert_get_text():
            return True
        else:
            return False

    def is_validate_confirm_text(self):
        value = Utils().read_data_json('test_data.json', 'CONFIRM_TEXT_BUTTON_AFTER_CLICK')
        if value in Text(By.XPATH, Locator.SELECTED_CONFIRM_TEXT).get_text():
            return True
        else:
            return False
