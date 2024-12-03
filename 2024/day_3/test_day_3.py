import pytest

import aoc
from aoc import utils
from day_3 import part1, part2, get_data


def test_example_part1():
    data = get_data(utils.SRC_EXAMPLE)
    assert part1(data) == 161

def test_example_part2():
    data = aoc.get_data(utils.SRC_EXAMPLE, day=3, offset=1)
    assert part2(data) == 48

def test_input_part1():
    data = get_data(utils.SRC_INPUT)
    assert part1(data) == 188116424

def test_input_part2():
    data = get_data(utils.SRC_INPUT)
    assert part2(data) == 104245808

if __name__ == '__main__':
    pytest.main()