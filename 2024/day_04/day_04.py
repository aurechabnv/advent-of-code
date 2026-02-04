# Day 4: Ceres Search

from functools import partial

import aoc
from aoc import COMPASS


def get_data(source) -> []:
    data = aoc.get_data(src=source, year=2024, day=4, offset=1)
    return data.splitlines()


def part1(data):
    count = 0
    max_x = len(data[0])
    max_y = len(data)
    for y in range(max_y):
        for x in range(max_x):
            if data[y][x] == 'X':  # avoid processing unnecessary letters
                for direction in COMPASS:  # check in every known direction
                    dy, dx = direction.value
                    word = ''
                    # build missing part of the word by moving from current letter in the desired direction
                    for nb_step in range(1, 4):
                        ny = y + (dy * nb_step)
                        nx = x + (dx * nb_step)
                        if 0 <= ny < max_y and 0 <= nx < max_x:  # check that we don't get out of range
                            word += data[ny][nx]
                    if word == 'MAS':  # check only the missing part since we always start from X
                        count += 1
    return count


def part2(data):
    diag_1 = [COMPASS.NORTH_WEST.value, COMPASS.SOUTH_EAST.value]
    diag_2 = [COMPASS.NORTH_EAST.value, COMPASS.SOUTH_WEST.value]
    count = 0
    max_x = len(data[0])
    max_y = len(data)
    for y in range(max_y):
        for x in range(max_x):
            if data[y][x] == 'A':  # avoid processing unnecessary letters
                # for a given diagonal: get the two letters involved within range, order alphabetically and join for string comparison
                get_letters = lambda d: ''.join(
                    sorted([data[y + dy][x + dx] for dy, dx in d if 0 <= y + dy < max_y and 0 <= x + dx < max_x]))
                if get_letters(diag_1) == get_letters(diag_2) == 'MS':
                    count += 1
    return count


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
