# Day 11: Plutonian Pebbles

import math
from collections import defaultdict
from functools import partial

import aoc


def get_data(source):
    if source == aoc.SOURCE.EXAMPLE:
        data = '125 17'
    else:
        data = aoc.get_data(src=source, year=2024, day=11)
    return data.split()


def apply_rules(stone):
    pebbles = []
    if stone == 0:
        pebbles.append(1)
    elif not (length := math.ceil(math.log10(stone + 1))) % 2:
        divider = 10 ** (length // 2)
        pebbles.extend([stone // divider, stone % divider])
    else:
        pebbles.append(stone * 2024)
    return pebbles


def count_pebbles(data, blinks):
    pebbles = defaultdict(int)
    pebbles.update({int(nb): 1 for nb in data})

    for _ in range(blinks):
        for pebble, count in pebbles.copy().items():
            pebbles[pebble] -= count
            blinked_pebbles = apply_rules(pebble)
            for p in blinked_pebbles:
                pebbles[p] += count

    return sum(pebbles.values())


def part1(data):
    return count_pebbles(data, blinks=25)


def part2(data):
    return count_pebbles(data, blinks=75)


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
