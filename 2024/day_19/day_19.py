# Day 19: Linen Layout

from functools import partial
import re

import aoc


def get_data(source):
    data = aoc.get_data(src=source, day=19).split('\n\n')
    return data[0].split(', '), data[1].splitlines()


def part1(data):
    towels, patterns = data
    regex = re.compile(rf'^(?:{'|'.join(towels)})+$')
    return sum(pattern == ''.join(regex.findall(pattern)) for pattern in patterns)


def part2(data):
    return 0


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
