# Day 14: Restroom Redoubt

from re import compile
from functools import partial

import aoc


def get_data(source):
    data = aoc.get_data(src=source, day=14).splitlines()
    regex = compile(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)')
    robots = []

    for robot in data:
        digits = regex.findall(robot)[0]
        position = digits[0], digits[1]
        speed = digits[2], digits[3]
        robots.append((tuple(map(int, position)), tuple(map(int, speed))))

    if source == aoc.SOURCE.EXAMPLE:
        width = 11
        height = 7
    else:
        width = 101
        height = 103

    return robots, (width, height)


def get_real_position(value, axis):
    if value >= axis:
        value = value - axis
    elif value < 0:
        value = axis + value
    return value


def move_robot(dimensions, position, speed, times):
    if times == 0:
        return position
    times -= 1
    position = tuple(get_real_position(position[i] + speed[i], dimensions[i]) for i in range(2))
    return move_robot(dimensions, position, speed, times)


def part1(data):
    robots, dimensions = data
    width, height = dimensions
    grid = {(x, y): 0 for x in range(width) for y in range(height)}

    for position, speed in robots:
        x, y = move_robot(dimensions, position, speed, 100)
        grid[(x, y)] += 1

    middle_x = width // 2
    middle_y = height // 2

    quadrant1 = [value for (x, y), value in grid.items() if x < middle_x and y < middle_y]
    quadrant2 = [value for (x, y), value in grid.items() if x > middle_x and y < middle_y]
    quadrant3 = [value for (x, y), value in grid.items() if x < middle_x and y > middle_y]
    quadrant4 = [value for (x, y), value in grid.items() if x > middle_x and y > middle_y]

    return sum(quadrant1) * sum(quadrant2) * sum(quadrant3) * sum(quadrant4)


def part2(data):
    return 0


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
