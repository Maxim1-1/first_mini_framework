from selenium.webdriver.common.by import By
from task3.framework.base.BasePage import BasePage
from task3.framework.base.Button import Button
from task3.framework.base.Link import Link
from task3.framework.base.Text import Text
from task3.framework.base.Driver import Driver
from task3.framework.utils import Utils


class Locator:
    NEW_TAB_BUTTON = "//button[contains(@id,'tabButton')]"
    ELEMENTS_MENU = "//*[contains(@class,'accordion')]//*[contains(text(),'Elements')]"
    LINKS_MENU = "//*[contains(@class,'accordion')]//*[text()='Links']"
    HOME_LINK = "//*[contains(@id,'simpleLink')]"
    TEXT_FRAME = "/html/descendant::h1"
    TEXT_BOTTOM_FRAME = "//*[@id='frame2']"
    SHOW_ELEMENT = "//*[contains(@class,'show')]"
    SAMPLE_PAGE_TEXT = "//*[@id='sampleHeading']"
    VALIDATE_LINKS = "//*[contains(@id,'linkWrapper')]"
    BROWSER_WINDOWS_VALIDATE = "//*[contains(@id,'browserWindows')]"


class BrowserWindows(BasePage):
    __button_new_tab_click = Button(By.XPATH, Locator.NEW_TAB_BUTTON)
    __validate_text_on_sample_page = Text(By.XPATH, Locator.SAMPLE_PAGE_TEXT)
    __button_elements_click = Button(By.XPATH, Locator.ELEMENTS_MENU)
    __validate_browser_windows_form = Text(By.XPATH, Locator.BROWSER_WINDOWS_VALIDATE)
    __button_links_click = Button(By.XPATH, Locator.LINKS_MENU)
    __validate_links_form = Text(By.XPATH, Locator.VALIDATE_LINKS)
    __link_home_click = Link(By.XPATH, Locator.HOME_LINK)

    def button_new_tab_click(self):
        self.__button_new_tab_click.click_on_button()

    def is_validate_text_on_sample_page(self):
        return self.__validate_text_on_sample_page.validate_text_on_page()

    def button_elements_click(self):
        self.__button_elements_click.click_on_button()

    def is_validate_browser_windows_form(self):
        return self.__validate_browser_windows_form.validate_text_on_page()

    def button_links_click(self):
        self.__button_links_click.click_on_button()

    def link_home_click(self):
        self.__link_home_click.click_on_link()

    def switch_to_window_sample(self):
        Driver().switch_to_window(-1)

    def switch_to_new_window(self):
        Driver().switch_to_window(-1)

    def switch_to_window_main(self):
        Driver().switch_to_window(0)

    def close_sample_window(self):
        Driver().close()

    def switch_to_links_window(self):
        Driver().switch_to_window(0)

    def is_validate_new_window_sample(self):
        value = Utils().read_data_json('test_data.json', 'SAMPLE_WINDOW')
        if value in Driver().get_current_url():
            return True
        else:
            return False

    def links_click(self):
        Button(By.XPATH, Locator.LINKS_MENU).click_on_button_if_clickable()
