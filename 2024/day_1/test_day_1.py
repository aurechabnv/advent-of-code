import unittest

from utils import utils
from day_1 import part1, part2, get_lists


class MyTestCase(unittest.TestCase):
    def test_example_part1(self):
        list1, list2 = get_lists(utils.SRC_EXAMPLE)
        self.assertEqual(part1(list1, list2), 11)

    def test_example_part2(self):
        list1, list2 = get_lists(utils.SRC_EXAMPLE)
        self.assertEqual(part2(list1, list2), 31)

    def test_input_part1(self):
        list1, list2 = get_lists(utils.SRC_INPUT)
        self.assertEqual(part1(list1, list2), 1834060)

    def test_input_part2(self):
        list1, list2 = get_lists(utils.SRC_INPUT)
        self.assertEqual(part2(list1, list2), 21607792)


if __name__ == '__main__':
    unittest.main()
