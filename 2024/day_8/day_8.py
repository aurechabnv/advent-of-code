# Day 8: Resonant Collinearity

from collections import defaultdict
from functools import partial

import aoc


def get_data(source):
    data = aoc.get_data(src=source, day=8)
    return [list(item) for item in data.splitlines()]


def get_antennas(data):
    antennas = defaultdict(list)
    for row in data:
        for cell in row:
            if cell != '.':
                antennas[cell].append((data.index(row), row.index(cell)))
    return antennas


def is_valid(antinode: tuple, bounds: tuple):
    return 0 <= antinode[0] < bounds[0] and 0 <= antinode[1] < bounds[1]


def get_antinodes(node_1: tuple, node_2: tuple, bounds: tuple, harmonic: bool):
    # shifts are made relative to first node, key is the start value for n
    shifts = {
        '0': lambda a, b, n: a - b * (2 + n),
        '1': lambda a, b, n: a + b * n
    }

    first_y, first_x = node_1
    second_y, second_x = node_2
    diff_y, diff_x = first_y - second_y, first_x - second_x

    antinodes = []
    if harmonic:
        antinodes.extend([node_1, node_2])

    for k, shift in shifts.items():
        i = int(k)
        while True:
            antinode = shift(first_y, diff_y, i), shift(first_x, diff_x, i)
            if is_valid(antinode, bounds):
                antinodes.append(antinode)
                if not harmonic:
                    break
                i += 1
            else:
                break

    return antinodes


def count_antinodes(data, harmonic: bool = False):
    bounds = len(data), len(data[0])
    antennas = get_antennas(data)
    antinodes = set()

    for positions in antennas.values():
        for i, n1 in enumerate(positions):
            antinodes.update(*[get_antinodes(n1, n2, bounds, harmonic) for n2 in positions[i+1:]])

    return len(antinodes)


def part1(data):
    return count_antinodes(data)


def part2(data):
    return count_antinodes(data, harmonic=True)


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
