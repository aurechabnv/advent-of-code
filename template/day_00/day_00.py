# Day

from functools import partial

import aoc


def get_data(source):
    data = aoc.get_data(src=source, day=0)
    return data


def part1(data):
    return 0


def part2(data):
    return 0


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.EXAMPLE)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
