import pytest

import aoc
from day_02 import get_data, part1, part2


def test_example_part1():
    data = get_data(aoc.SOURCE.EXAMPLE)
    assert part1(data) == 1227775554

def test_input_part1():
    data = get_data(aoc.SOURCE.INPUT)
    assert part1(data) == 28146997880

def test_example_part2():
    data = get_data(aoc.SOURCE.EXAMPLE)
    assert part2(data) == 4174379265

def test_input_part2():
    data = get_data(aoc.SOURCE.INPUT)
    assert part2(data) == 40028128307

if __name__ == '__main__':
    pytest.main()