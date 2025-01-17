import pytest

import aoc
from day_19 import get_data, part1, part2


def test_example_part1():
    data = get_data(aoc.SOURCE.EXAMPLE)
    assert part1(data) == 6

def test_input_part1():
    data = get_data(aoc.SOURCE.INPUT)
    assert part1(data) == 238

def test_example_part2():
    data = get_data(aoc.SOURCE.EXAMPLE)
    assert part2(data) == 16

def test_input_part2():
    data = get_data(aoc.SOURCE.INPUT)
    assert part2(data) == 635018909726691

if __name__ == '__main__':
    pytest.main()