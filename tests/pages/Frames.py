from selenium.webdriver.common.by import By
from task3.framework.base.BasePage import BasePage
from task3.framework.base.Text import Text
from task3.framework.base.Driver import Driver
from task3.framework.base.Link import Link


class Locator:
    TOP_FRAME = "//*[@id='frame1']"
    BOTTOM_FRAME = "//*[@id='frame2']"
    TEXT_FRAME = "/html/descendant::h1"
    FRAMES_VALIDATE = "//*[contains(@id,'Wrapper')]"


class Frames(BasePage):
    __top_frame = Locator.TOP_FRAME
    __get_text_top_frame = Text(By.XPATH, Locator.TEXT_FRAME)
    __switch_to_bottom_frame = Locator.BOTTOM_FRAME
    __get_text_bottom_frame = Text(By.XPATH, Locator.TEXT_FRAME)

    def switch_to_top_frame(self):
        Driver().switch_frame_by_locator(By.XPATH, self.__top_frame)

    def get_text_top_frame(self):
        self.__get_text_top_frame.get_text()

    def switch_to_bottom_frame(self):
        Driver().switch_frame_by_locator(By.XPATH, self.__switch_to_bottom_frame)

    def get_text_bottom_frame(self):
        self.__get_text_bottom_frame.get_text()

    def exiting_the_frame(self):
        Driver().switch_to_default_content()

    def is_validate_form_frames(self):
        count_frames = Link(By.XPATH, Locator.FRAMES_VALIDATE).get_links
        if len(count_frames()) == 3:
            return True
        else:
            return False
