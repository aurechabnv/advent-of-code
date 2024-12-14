# Day 13: Claw Contraption

from re import compile
from functools import partial

import numpy as np

import aoc


def get_data(source):
    data = aoc.get_data(src=source, day=13)
    regex = compile(r'(\d+)')
    machines = []
    for specs in data.split('\n\n'):
        machines.append([tuple(map(int, regex.findall(spec))) for spec in specs.split('\n')])
    return machines


def count_presses_to_prize(btn_a, btn_b, prize, correction):
    ax, ay = btn_a
    bx, by = btn_b
    px, py = prize
    solution = np.linalg.solve([[ax, bx], [ay, by]], [[px + correction], [py + correction]])
    a, b = (el[0] for el in np.round(solution, decimals=2))
    return (0, 0) if a % 1 or b % 1 else (a, b)


def count_tokens(machines, correction = 0):
    tokens = 0
    for btn_a, btn_b, prize in machines:
        a, b = count_presses_to_prize(btn_a, btn_b, prize, correction)
        if correction or a <= 100 and b <= 100: # my dataset doesn't even require this check
            tokens += a * 3 + b
    return tokens


def part1(data):
    return count_tokens(data)


def part2(data):
    return count_tokens(data, correction=10000000000000)


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
