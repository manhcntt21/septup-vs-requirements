import json
import configparser
import os

HOME = os.path.expanduser('~')

CONFIG_PATH = os.path.join(HOME, '.config', 'mypkg', 'config.init')
DEFAULT_CONFIG = os.path.join(HOME, '.local', 'share', 'mypkg', 'default.json')
GUIDE = os.path.join(HOME, '.local', 'share', 'docs', 'mypkg', 'examples.txt')


class App:
    def __init__(self):
        # Đọc config.init
        self.config = configparser.ConfigParser()
        self.config.read(CONFIG_PATH)

        # Đọc default.json
        with open(DEFAULT_CONFIG) as f:
            self.settings = json.load(f)

        # Đọc examples.txt
        with open(GUIDE) as f:
            self.guide = f.read()

    def get_db_config(self):
        return {
            'host': self.config['Database']['host'],
            'port': self.config['Database'].getint('port'),
            'database': self.config['Database']['database'],
            'user': self.config['Database']['user'],
            'password': self.config['Database']['password']
        }

    def get_server_config(self):
        return {
            'host': self.config['Server']['host'],
            'port': self.config['Server'].getint('port'),
            'debug': self.config['Server'].getboolean('debug')
        }

    def get_feature_settings(self):
        return self.settings['features']

    def get_guide(self):
        return self.guide
