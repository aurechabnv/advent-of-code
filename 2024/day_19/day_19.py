# Day 19: Linen Layout

from functools import partial, cache
import re

import aoc


def get_data(source):
    data = aoc.get_data(src=source, day=19).split('\n\n')
    return tuple(data[0].split(', ')), data[1].splitlines()


def part1(data):
    towels, designs = data
    regex = re.compile(rf'^(?:{'|'.join(towels)})+$')
    return sum(design == ''.join(regex.findall(design)) for design in designs)


def part2(data):
    towels, designs = data

    @cache
    def count_arrangements(design, towels):
        count = 0
        for towel in towels:
            if design.startswith(towel):
                if len(design) == len(towel):
                    count += 1
                else:
                    count += count_arrangements(design[len(towel):], towels)
        return count

    count = 0
    for design in designs:
        count += count_arrangements(design, towels)

    return count


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
