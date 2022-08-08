import random
import string
from configparser import ConfigParser
import json


class Utils():
    def generate_random_string(self, length=5):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(length))
        return rand_string

    def read_config_ini(self, fail_name, key, read_value=None):
        config = ConfigParser()
        config.read(fail_name,encoding='utf-8')
        return config.get(key, read_value)

    def read_data_json(self, fail, value):
        with open(fail, "r", encoding='utf-8') as file:
            text = json.load(file)
        return text[value]
