import pytest

import aoc
from day_17 import get_data, part1, part2


def test_example_part1():
    data = get_data(aoc.SOURCE.EXAMPLE)
    assert part1(data) == '4,6,3,5,6,3,5,2,1,0'

def test_input_part1():
    data = get_data(aoc.SOURCE.INPUT)
    assert part1(data) == '7,1,5,2,4,0,7,6,1'

def test_example_part2():
    data = get_data(aoc.SOURCE.EXAMPLE, offset=1)
    assert part2(data) == 117440

def test_input_part2():
    data = get_data(aoc.SOURCE.INPUT)
    assert part2(data) == 37222273957364

if __name__ == '__main__':
    pytest.main()