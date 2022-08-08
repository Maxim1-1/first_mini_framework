from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from task3.framework.base.Singleton import MetaSingleton
from selenium.webdriver.common.alert import Alert
import logging


class Driver(metaclass=MetaSingleton):
    logging.basicConfig(filename='logs.log', format='%(asctime)s %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)
    driver = None

    def __init__(self):
        BROWSER_CHROME = 'chrome'
        BROWSER_FIREFOX = 'firefox'
        self.browser = BROWSER_CHROME
        self.inst = self.factory_browser()

    def factory_browser(self):

        if self.browser == 'chrome':
            self.logger.info(f'Chrome driver create')
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        if self.browser == 'firefox':
            self.logger.info(f'Firefox driver create')
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        return self.driver

    def get_instance(self):
        if self.driver is None:
            self.driver = self.inst
            self.logger.info(f'Instance driver create')
        return self.driver

    def open_page(self, url):
        self.logger.info(f'Main page open')
        self.driver.get(url)

    def switch_to_alert(self):
        self.logger.info(f'Switch to alert')
        alert = self.driver.switch_to.alert()

    def accept_alert(self):
        self.logger.info(f'Alert accept')
        Alert(self.driver).accept()

    def alert_get_text(self):
        self.logger.info(f'Getting text with alert')
        return Alert(self.driver).text

    def alert_send(self, value):

        s = self.driver.switch_to.alert
        self.logger.info(f'Input text in alert')
        s.send_keys(value)

    def switch_to_frame(self, locator):
        def wrapper(*args):
            self.logger.info(f'Switch to frame page')
            self.driver.switch_to.frame(locator)

        return wrapper

    def switch_frame_by_locator(self, method, locator):
        self.logger.info(f'Getting text with alert')
        element = self.driver.find_element(method, locator)
        self.driver.switch_to.frame(element)

    def switch_to_default_content(self):
        self.logger.info(f'Switch to content page ')
        self.driver.switch_to.default_content()

    def get_current_url(self):
        def wrapper(*args):
            self.logger.info(f'Getting current url')
            url = self.driver.current_url
            return url

        return wrapper()

    def switch_to_window(self, number_window):

        self.logger.info(f'Switch to window')
        window = self.driver.window_handles[number_window]
        self.driver.switch_to.window(window)

    def close(self):
        self.logger.info(f'Window close')
        self.driver.close()

    def quit(self):
        self.logger.info(f'The Browser Is Closed')
        self.driver.quit()
