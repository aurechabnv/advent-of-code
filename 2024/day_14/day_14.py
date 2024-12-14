# Day 14: Restroom Redoubt

from re import compile
from functools import partial

import aoc


def get_data(source):
    data = aoc.get_data(src=source, day=14).splitlines()

    robots = []
    regex = compile(r'-?\d+')
    for robot in data:
        digits = list(map(int, regex.findall(robot)))
        robots.append([(digits[2], digits[3]), (digits[0], digits[1])])

    dimensions = (101, 103) if source == aoc.SOURCE.INPUT else (11, 7)

    return robots, dimensions


def create_grid(width, height):
    return {(x, y): 0 for x in range(width) for y in range(height)}


def move_robot(dimensions, coords, speed, seconds = 1):
    if seconds == 0:
        return coords
    x, y = coords
    vx, vy = speed
    max_x, max_y = dimensions
    coords = (x + vx) % max_x, (y + vy) % max_y
    return move_robot(dimensions, coords, speed, seconds - 1)


def get_quadrants(grid, width, height):
    mid_x = width // 2
    mid_y = height // 2

    q1 = q2 = q3 = q4 = 0
    for (x, y), v in grid.items():
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
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for x, y in grid:
        if grid[(x, y)] > 0:
            neighborhood.append(sum([1 for dx, dy in directions if (coords := (x + dx, y + dy)) in grid and grid[coords] > 0]))
    return sum([n >= 2 for n in neighborhood])


def show_grid(grid, width, height):
    grid_array = [['' for _ in range(width)] for _ in range(height)]
    for (x, y), value in grid.items():
        grid_array[y][x] = str(value) if value > 0 else '.'
    print('\n'.join([''.join(line) for line in grid_array]))


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
            show_grid(grid, *dimensions)

    return seconds


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
