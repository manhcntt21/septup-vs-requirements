import unittest
import os
from mypkg.app import App

app = App()


class TestInstallAdditionalFiles(unittest.TestCase):
    def test_config_database(self):
        # Test that the additional files are installed
        self.assertEqual(app.get_db_config(), {
            'host': 'localhost',
            'port': 5432,
            'database': 'mydb',
            'user': 'admin',
            'password': 'secret'})

    def test_config_server(self):
        self.assertEqual(app.get_server_config(), {
            'host': '0.0.0.0',
            'port': 8000,
            'debug': True})

    def test_guide(self):
        self.assertEqual(app.get_guide(), 'THIS IS A EXAMPLE GUIDE')


def run_tests():
    loader = unittest.TestLoader()
    start_dir = os.path.dirname(__file__)
    suite = loader.discover(start_dir, pattern='test*.py')
    runner = unittest.TextTestRunner()

    return runner.run(suite)


if __name__ == '__main__':
    run_tests()