import unittest
from hello import say_hello
import os


class TestExtensionModule(unittest.TestCase):
    def test_extension_module(self):
        self.assertEqual(say_hello(), 'Hello from C!')


def run_tests():
    loader = unittest.TestLoader()
    start_dir = os.path.dirname(__file__)
    suite = loader.discover(start_dir, pattern='test*.py')
    runner = unittest.TextTestRunner()

    return runner.run(suite)


if __name__ == '__main__':
    run_tests()