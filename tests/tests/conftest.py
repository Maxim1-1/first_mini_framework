import pytest

from task3.framework.base.Driver import Driver
from task3.framework.utils import Utils

url = 'url'
config = 'config.ini'
key = 'urls'


@pytest.fixture
def conditions():
    driver = Driver().get_instance()
    driver.maximize_window()
    driver.get(Utils().read_config_ini(config, key, url))
    yield
    driver.quit()
    Driver.clear()