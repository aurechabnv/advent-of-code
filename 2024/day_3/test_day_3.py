import pytest

import aoc
from aoc import utils
from day_3 import get_data, part1, part2, part2_alt


def test_example_part1():
    data = get_data(utils.SOURCE.EXAMPLE)
    assert part1(data) == 161

def test_input_part1():
    data = get_data(utils.SOURCE.INPUT)
    assert part1(data) == 188116424

def test_example_part2():
    data = get_data(utils.SOURCE.EXAMPLE, offset=1)
    assert part2(data) == 48

def test_input_part2():
    data = get_data(utils.SOURCE.INPUT)
    assert part2(data) == 104245808

def test_example_part2_alt():
    data = get_data(utils.SOURCE.EXAMPLE, offset=1)
    assert part2_alt(data) == 48

def test_input_part2_alt():
    data = get_data(utils.SOURCE.INPUT)
    assert part2_alt(data) == 104245808

if __name__ == '__main__':
    pytest.main()