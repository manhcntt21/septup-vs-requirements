import unittest
from introduction import introduction
from utils.add import add
from utils.subtract import subtract
import os


class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 2), 4)

    def test_subtraction(self):
        self.assertEqual(subtract(4, 2), 2)

    def test_introduction(self):
        self.assertEqual(introduction(), 'My Calculator')


def run_tests():
    loader = unittest.TestLoader()
    start_dir = os.path.dirname(__file__)
    suite = loader.discover(start_dir, pattern='test*.py')
    runner = unittest.TextTestRunner()

    return runner.run(suite)


if __name__ == '__main__':
    run_tests()