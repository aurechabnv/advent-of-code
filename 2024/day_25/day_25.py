# Day 25: Code Chronicle

from functools import partial

import aoc


def get_data(source):
    data = aoc.get_data(src=source, year=2024, day=25).split('\n\n')
    return data


def part1(data):
    locks, keys = [], []

    for element in data:
        schematic = element.splitlines()
        pattern = '#' * len(schematic[0])

        is_lock = True if schematic[0] == pattern else False
        if not is_lock:
            schematic.reverse()

        heights = [0 for _ in range(len(schematic[0]))]
        for i in range(1, len(schematic)):
            for j in range(len(schematic[0])):
                if schematic[i][j] == '#':
                    heights[j] += 1

        if is_lock:
            locks.append(heights)
        else:
            keys.append(heights)

    count_pairs = 0
    for lock in locks:
        for key in keys:
            valid = True
            for i in range(len(lock)):
                if lock[i] + key[i] > 5:
                    valid = False
            if valid:
                count_pairs += 1

    return count_pairs


def part2(data):
    return 0


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
