# Day 14: Restroom Redoubt

from functools import partial
from re import compile

import aoc
from aoc import COMPASS


def get_data(source):
    data = aoc.get_data(src=source, day=14).splitlines()

    robots = []
    regex = compile(r'-?\d+')
    for robot in data:
        digits = list(map(int, regex.findall(robot)))
        robots.append([(digits[3], digits[2]), (digits[1], digits[0])])

    dimensions = (101, 103) if source == aoc.SOURCE.INPUT else (11, 7)

    return robots, dimensions


def create_grid(width, height):
    return {(y, x): 0 for x in range(width) for y in range(height)}


def move_robot(dimensions, coords, speed, seconds=1):
    if seconds == 0:
        return coords
    y, x = coords
    vy, vx = speed
    max_x, max_y = dimensions
    coords = (y + vy) % max_y, (x + vx) % max_x
    return move_robot(dimensions, coords, speed, seconds - 1)


def get_quadrants(grid, width, height):
    mid_x = width // 2
    mid_y = height // 2

    q1 = q2 = q3 = q4 = 0
    for (y, x), v in grid.items():
        if x < mid_x and y < mid_y:
            q1 += v
        elif x > mid_x and y < mid_y:
            q2 += v
        elif x < mid_x and y > mid_y:
            q3 += v
        elif x > mid_x and y > mid_y:
            q4 += v

    return q1, q2, q3, q4


def check_neighbors(grid):
    neighborhood = []
    compass_values = [d.value for d in COMPASS]
    for y, x in grid:
        if grid[(y, x)] > 0:
            neighborhood.append(sum([1 for dy, dx in compass_values if (coords := (y + dy, x + dx)) in grid and grid[coords] > 0]))
    return sum([n >= 2 for n in neighborhood])


def part1(data):
    robots, dimensions = data
    grid = create_grid(*dimensions)

    for speed, coords in robots:
        new_coords = move_robot(dimensions, coords, speed, 100)
        grid[new_coords] += 1

    q1, q2, q3, q4 = get_quadrants(grid, *dimensions)
    return q1 * q2 * q3 * q4


def part2(data):
    robots, dimensions = data
    seconds = 0
    christmas_tree = False

    while not christmas_tree:
        if seconds == dimensions[0] * dimensions[1]:
            print("Tree should have been reached by now.")
            break

        seconds += 1

        grid = create_grid(*dimensions)
        for index, (speed, coords) in enumerate(robots):
            new_coords = move_robot(dimensions, coords, speed)
            robots[index][1] = new_coords
            grid[new_coords] += 1

        # Method 0: find iteration where no robots overlap (narrows the search)
        possible_tree = len(robots) == list(grid.values()).count(1)

        if possible_tree:
            neighbors = check_neighbors(grid)               # Method 1: find how many robots have 2+ neighbors
            christmas_tree = neighbors >= len(robots) // 2
            # quadrants = get_quadrants(grid, *dimensions)  # Method 2: find iteration where one quadrant holds half the robots
            # christmas_tree = max(quadrants) > len(robots) // 2

        if christmas_tree:
            aoc.print_grid(grid, lambda value: str(value) if value > 0 else '.')

    return seconds


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
