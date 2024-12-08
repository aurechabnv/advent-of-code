# Day 8: Resonant Collinearity

from functools import partial

import aoc


def get_data(source):
    data = aoc.get_data(src=source, day=8)
    return [list(item) for item in data.splitlines()]


def show_map(data):
    print('\n'.join([''.join(row) for row in data]))


def get_antennas(data):
    antennas = {}
    for row in data:
        for cell in row:
            if cell != '.':
                if cell not in antennas:
                    antennas[cell] = []
                antennas[cell].append((data.index(row), row.index(cell)))
    print(antennas)
    return antennas


def get_antinodes(a: tuple, b: tuple):
    node_y, node_x = a[0], a[1]
    y, x = b[0], b[1]
    diff_y, diff_x = node_y - y, node_x - x
    node_1 = y - diff_y, x - diff_x
    node_2 = y + diff_y * 2, x + diff_x * 2
    return node_1, node_2


def is_valid_antinode(antinode: tuple, bounds: tuple):
    return 0 <= antinode[0] < bounds[0] and 0 <= antinode[1] < bounds[1]


def part1(data):
    bounds = (len(data), len(data[0]))
    antennas = get_antennas(data)
    antinodes = set()

    for antenna in antennas:
        positions = antennas[antenna]
        for i in range(len(positions)):
            next_antennas = positions[i+1:]
            for node in next_antennas:
                antinodes.update([el for el in get_antinodes(positions[i], node) if is_valid_antinode(el, bounds)])

    # show_map(data)
    return len(antinodes)


def part2(data):
    return 0


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.EXAMPLE)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
