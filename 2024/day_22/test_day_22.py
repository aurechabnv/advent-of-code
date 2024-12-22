import pytest

import aoc
from day_22 import get_data, part1, part2


def test_example_part1():
    data = get_data(aoc.SOURCE.EXAMPLE, offset=1)
    assert part1(data) == 37327623

def test_input_part1():
    data = get_data(aoc.SOURCE.INPUT)
    assert part1(data) == 14180628689

def test_example_part2():
    data = get_data(aoc.SOURCE.EXAMPLE, offset=5)
    assert part2(data) == 23

def test_input_part2():
    data = get_data(aoc.SOURCE.INPUT)
    assert part2(data) == 1690

if __name__ == '__main__':
    pytest.main()