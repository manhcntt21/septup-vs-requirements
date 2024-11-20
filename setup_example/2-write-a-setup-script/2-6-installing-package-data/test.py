import os
import pkg_resources
import unittest


class TestPackageData(unittest.TestCase):
    def test_package_data(self):
        data_path = pkg_resources.resource_filename('mypkg', 'data/test.dat')
        with open(data_path, 'r') as f:
            data = f.read()

        self.assertEqual(data, 'HELLO!')

def run_tests():
    loader = unittest.TestLoader()
    start_dir = os.path.dirname(__file__)
    suite = loader.discover(start_dir, pattern='test*.py')
    runner = unittest.TextTestRunner()

    return runner.run(suite)


if __name__ == '__main__':
    run_tests()