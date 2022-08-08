from task3.framework.base.BaseElement import BaseElement
import logging

class Link(BaseElement):
    logging.basicConfig(filename='logs.log', format='%(asctime)s %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    def click_on_link(self):
        self.logger.info(f'Click on link')
        element = self._find_element_wait()
        element.click()

    def get_links(self):
        self.logger.info(f'Getting links')
        links = self._find_elements()
        return links
