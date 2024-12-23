import pytest

import aoc
from day_23 import get_data, part1, part2


def test_example_part1():
    data = get_data(aoc.SOURCE.EXAMPLE)
    assert part1(data) == 7

def test_input_part1():
    data = get_data(aoc.SOURCE.INPUT)
    assert part1(data) == 1119

def test_example_part2():
    data = get_data(aoc.SOURCE.EXAMPLE)
    assert part2(data) == 'co,de,ka,ta'

def test_input_part2():
    data = get_data(aoc.SOURCE.INPUT)
    assert part2(data) == 'av,fr,gj,hk,ii,je,jo,lq,ny,qd,uq,wq,xc'

if __name__ == '__main__':
    pytest.main()