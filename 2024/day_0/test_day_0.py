import unittest

from utils import utils
from day_0 import part1, part2, get_data


class MyTestCase(unittest.TestCase):
    def test_example_part1(self):
        data = get_data(utils.SRC_EXAMPLE)
        self.assertEqual(part1(data), True)

    def test_example_part2(self):
        data = get_data(utils.SRC_EXAMPLE)
        self.assertEqual(part2(data), True)

    def test_input_part1(self):
        data = get_data(utils.SRC_INPUT)
        self.assertEqual(part1(data), True)

    def test_input_part2(self):
        data = get_data(utils.SRC_INPUT)
        self.assertEqual(part2(data), True)


if __name__ == '__main__':
    unittest.main()
