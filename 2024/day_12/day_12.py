# Day 12: Garden Groups

from collections import defaultdict
from functools import partial

import aoc


def get_data(source):
    data = aoc.get_data(src=source, day=12, offset=3)
    return data.splitlines()


COMPASS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def find_neighbors(grid, regions, plant, coords):
    if grid[coords].get('area'):
        return

    (y, x) = coords
    area = 0
    fences = 4
    neighbors = []

    for dy, dx in COMPASS:
        if (n_coords := (y + dy, x + dx)) in grid:
            if grid[n_coords]['plant'] == plant:
                neighbors.append(n_coords)
                fences -= 1
                if plot_area := grid[n_coords].get('area'):
                    area = plot_area
    if area == 0:
        area = len(regions[plant]) + 1
        regions[plant].append([])

    grid[(y, x)].update({'area': area, 'fences': fences})
    regions[plant][area - 1].append(((y, x), fences))

    if neighbors:
        for neighbor in neighbors:
            find_neighbors(grid, regions, plant, neighbor)


def part1(data):
    grid = {(y, x): {'plant': item} for y, line in enumerate(data) for x, item in enumerate(line)}
    regions = defaultdict(list)

    for (y, x), specs in grid.items():
        find_neighbors(grid, regions, specs.get('plant'), (y, x))

    full_price = 0
    for plant, cultures in regions.items():
        for region in cultures:
            full_price += len(region) * sum([fences for coords, fences in region])

    return full_price


def part2(data):
    return 0


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
