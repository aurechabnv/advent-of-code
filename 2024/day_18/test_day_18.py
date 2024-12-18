import pytest

import aoc
from day_18 import get_data, part1, part2


def test_example_part1():
    data = get_data(aoc.SOURCE.EXAMPLE)
    assert part1(data) == 22

def test_input_part1():
    data = get_data(aoc.SOURCE.INPUT)
    assert part1(data) == 234

def test_example_part2():
    data = get_data(aoc.SOURCE.EXAMPLE)
    assert part2(data) == '6,1'

def test_input_part2():
    data = get_data(aoc.SOURCE.INPUT)
    assert part2(data) == '58,19'

if __name__ == '__main__':
    pytest.main()