from task3.framework.base.BaseElement import BaseElement
import logging

class Form(BaseElement):
    logging.basicConfig(filename='logs.log', format='%(asctime)s %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    def entering_data_in_field(self, value):
        self.logger.info(f'The data is entered in the field')
        field = self._find_element_wait()
        field.send_keys(value)

    def get_fields(self):
        self.logger.info(f'Getting fields')
        elements = self._find_elements()
        return elements
