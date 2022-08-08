from selenium.webdriver.common.by import By
from task3.framework.base.BasePage import BasePage
from task3.framework.base.Button import Button
from task3.framework.base.Text import Text
from task3.framework.base.Driver import Driver
from task3.framework.base.Link import Link
from task3.framework.utils import Utils


class Nested_frame(BasePage):
    PARENT_FRAME = "//*[@id='frame1']"
    GET_TEXT_IN_FRAME = "//html"
    NASTED_FRAMES_VALIDATE = "//*[contains(@id,'Wrapper')]"
    CHILD_FRAME = "iframe"
    BUTTON_FRAMES_MENU = "//*[contains(@class,'accordion')]//span[text()='Frames']"

    __child_frame = CHILD_FRAME
    __element_frames_click = Button(By.XPATH, BUTTON_FRAMES_MENU)
    __text_in_frame = Text(By.XPATH, GET_TEXT_IN_FRAME)
    __parent_frame = PARENT_FRAME

    def switch_to_parent_frame(self):
        Driver().switch_frame_by_locator(By.XPATH, self.__parent_frame)

    def switch_to_child_frame(self):
        Driver().switch_frame_by_locator(By.TAG_NAME, self.__child_frame)

    def exiting_the_frame(self):
        Driver().switch_to_default_content()

    def element_frames_click(self):
        self.__element_frames_click.click_on_button()

    def is_validate_parent_frame(self):
        value = Utils().read_data_json('test_data.json', 'PARENT_FRAME')
        if value in self.__text_in_frame.get_text():
            return True
        else:
            return False

    def is_validate_child_frame(self):
        value = Utils().read_data_json('test_data.json', 'CHILD_FRAME')
        if value in self.__text_in_frame.get_text():
            return True
        else:
            return False

    def is_validate_form_nested_frames(self):
        count_frames = Link(By.XPATH, self.NASTED_FRAMES_VALIDATE).get_links
        if len(count_frames()) == 2:
            return True
        else:
            return False
