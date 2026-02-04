# Day 10: Hoof It

from collections import defaultdict
from functools import partial

import aoc
from aoc import CARDINALS


def get_data(source):
    data = aoc.get_data(src=source, year=2024, day=10, offset=4)
    return data


def get_trails(data):
    grid = aoc.init_grid(data, lambda v: int(v))
    trails = [[coords] for coords, height in grid.items() if not height]

    for height in range(1, 10):
        for trail in trails.copy():
            y, x = trail[-1]
            next_steps = []
            for direction in CARDINALS:
                move_y, move_x = direction.value
                position = (y + move_y, x + move_x)
                if position in grid and grid[position] == height:
                    next_steps.append(position)

            if len(next_steps) == 0:
                trails.pop(trails.index(trail))
            else:
                trail.append(next_steps[0])
                if len(next_steps) > 1:
                    for step in next_steps[1:]:
                        new_trail = trail[:-1]
                        new_trail.append(step)
                        trails.append(new_trail)
    return trails


def part1(data):
    trails = get_trails(data)
    trailheads = defaultdict(set)
    for trail in trails:
        trailheads[trail[0]].add(trail[9])
    return sum([len(summits) for summits in trailheads.values()])


def part2(data):
    trails = get_trails(data)
    return len(trails)


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
