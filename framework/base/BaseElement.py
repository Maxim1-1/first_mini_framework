from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from task3.framework.base.Driver import Driver
from task3.framework.utils import Utils


class BaseElement():
    logging.basicConfig(filename='logs.log', format='%(asctime)s %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    time = int(Utils().read_config_ini('config.ini', 'timeout', 'time'))

    def __init__(self, method, locator):
        self.method = method
        self.locator = locator
        self.logger.info(f'Webdriver create')

    def _find_element_wait(self, timeout=time):
        try:
            self.logger.info(f'Element with selector: {self.locator} was  found during {timeout} seconds')
            return WebDriverWait(Driver().get_instance(), timeout).until(
                EC.presence_of_element_located((self.method, self.locator)))
        except TimeoutError:
            self.logger.info(f'Element with selector: {self.locator} was not found during {timeout} seconds')

    def _element_to_be_clickable_click(self, timeout=time):
        self.logger.info(f'Element is visible')
        WebDriverWait(Driver().get_instance(), timeout=timeout).until(EC.element_to_be_clickable(
            (self.method, self.locator))).click()

    def _find_elements(self):
        self.logger.info(f'Elements with selector: {self.locator} was  found')
        elements = Driver().get_instance().find_elements(self.method, self.locator)
        return elements
