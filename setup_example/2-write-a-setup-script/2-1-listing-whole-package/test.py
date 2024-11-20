import sys

from animals import make_sound
from animals.dog import get_breed
import unittest
import os


class TestCat(unittest.TestCase):
    def test_make_sound(self):
        self.assertEqual(make_sound(), 'Meow')

    def test_make_sound_type(self):
        self.assertIsInstance(make_sound(), str)


class TestDog(unittest.TestCase):
    def test_get_breed(self):
        breed = get_breed()
        self.assertIsInstance(breed, list)
        self.assertTrue(len(breed) > 0)
        self.assertIn('Husky', breed)


def run_tests():
    loader = unittest.TestLoader()
    start_dir = os.path.dirname(__file__)
    suite = loader.discover(start_dir, pattern='test*.py')

    runner = unittest.TextTestRunner()
    return runner.run(suite)


if __name__ == '__main__':
    result = run_tests()
    sys.exit(not result.wasSuccessful())
