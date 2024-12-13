# Day 13: Claw Contraption

import re
from functools import partial

import numpy as np

import aoc


def get_data(source):
    data = aoc.get_data(src=source, day=13)
    data = data.split('\n\n')
    regex = re.compile(r'(\d+)')
    equations = []
    for eq in data:
        equations.append([tuple(map(int, regex.findall(el))) for el in eq.split('\n')])
    return equations


def count_presses_to_prize(a, b, r):
    ax, ay = a
    bx, by = b
    rx, ry = r
    solution = np.linalg.solve([[ax, bx], [ay, by]], [[rx], [ry]])
    x, y = [el[0] for el in np.round(solution, decimals=2)]
    if not x % 1 and not y % 1:
        return x, y
    return 0, 0


def part1(data):
    price = 0
    for a, b, r in data:
        x, y = count_presses_to_prize(a, b, r)
        if x <= 100 and y <= 100:
            price += x * 3 + y * 1
    return price


def part2(data):
    return 0


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
