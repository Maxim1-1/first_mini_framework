from task3.framework.base.BaseElement import BaseElement
import logging

class Text(BaseElement):
    logging.basicConfig(filename='logs.log', format='%(asctime)s %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    def get_text(self):
        self.logger.info(f'Getting text')
        text = self._find_element_wait()
        return text.text

    def validate_text_on_page(self):
        self.logger.info(f'Checking the text on the page')
        validate_text = self._find_element_wait()
        if validate_text:
            return True
        else:
            return False

