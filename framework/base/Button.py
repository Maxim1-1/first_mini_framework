from task3.framework.base.BaseElement import BaseElement
import logging

class Button(BaseElement):
    logging.basicConfig(filename='logs.log', format='%(asctime)s %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    def click_on_button(self):
        self.logger.info(f'Click on button')
        element = self._find_element_wait()
        element.click()

    def button_get_text(self):
        self.logger.info(f'Getting text on button')
        element = self._find_element_wait()
        return element.text

    def click_on_button_if_clickable(self):
        self.logger.info(f'Click on button')
        self._element_to_be_clickable_click()

