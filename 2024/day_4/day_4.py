# Day 4: Ceres Search

from functools import partial

import aoc


def get_data(source) -> []:
    data = aoc.get_data(src=source, day=4, offset=1)
    return data.splitlines()


def part1(data):
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
    diag_1 = {
        'up-left': (-1,-1),
        'down-right': (1,1)
    }
    diag_2 = {
        'up-right': (-1,1),
        'down-left': (1,-1)
    }
    count = 0
    nb_col = len(data[0])
    nb_row = len(data)
    for row in range(nb_row):
        for col in range(nb_col):
            if data[row][col] == "A": # avoid processing unnecessary letters
                # for a given diagonal: get the two letters involved within range, order alphabetically and join for string comparison
                get_letters = lambda directions: "".join(sorted([data[row+h][col+v] for h, v in directions.values() if 0 <= row+h < nb_row and 0 <= col+v < nb_col]))
                if get_letters(diag_1) == get_letters(diag_2) == "MS":
                    count += 1
    return count


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
