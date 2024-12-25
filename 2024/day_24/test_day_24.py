import pytest

import aoc
from day_24 import get_data, part1, part2


def test_example_part1():
    data = get_data(aoc.SOURCE.EXAMPLE, offset=1)
    assert part1(data) == 2024

def test_input_part1():
    data = get_data(aoc.SOURCE.INPUT)
    assert part1(data) == 61886126253040

# def test_example_part2():
#     data = get_data(aoc.SOURCE.EXAMPLE, offset=5)
#     assert part2(data) == 'z00,z01,z02,z05'

def test_input_part2():
    data = get_data(aoc.SOURCE.INPUT)
    assert part2(data) == 'fgt,fpq,nqk,pcp,srn,z07,z24,z32'

if __name__ == '__main__':
    pytest.main()