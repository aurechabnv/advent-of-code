# Day 4: Ceres Search

import re
from functools import partial

import aoc


def get_data(source) -> []:
    data = aoc.get_data(src=source, day=4, offset=1)
    return data


def part1(data):
    data = data.splitlines()
    directions = {
        'left': (0,-1),
        'right': (0,1),
        'up': (-1,0),
        'down': (1,0),
        'up-left': (-1,-1),
        'down-left': (1,-1),
        'up-right': (-1,1),
        'down-right': (1,1)
    }
    count = 0
    nb_col = len(data[0])
    nb_row = len(data)
    for row in range(nb_row):
        for col in range(nb_col):
            if data[row][col] == "X": # avoid processing unnecessary letters
                for dir_h, dir_v in directions.values(): # check in every known direction
                    word = ""
                    # build missing part of the word by moving from current letter in the desired direction
                    for nb_step in range(1, 4):
                        y = row + (dir_h * nb_step)
                        x = col + (dir_v * nb_step)
                        if 0 <= y < nb_row and 0 <= x < nb_col: # check that we don't get out of range
                            word += data[y][x]
                    if word == "MAS": # check only the missing part since we always start from X
                        count += 1
    return count


def part2(data):
    return True


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.EXAMPLE)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
