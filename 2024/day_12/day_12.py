# Day 12: Garden Groups

from enum import Enum
from functools import partial

import aoc


class CARDINALS(Enum):
    NORTH = (-1, 0)
    SOUTH = (1, 0)
    EAST = (0, 1)
    WEST = (0, -1)

COMPASS = [CARDINALS.NORTH, CARDINALS.EAST, CARDINALS.SOUTH, CARDINALS.WEST]

GO_ALONG = {
    CARDINALS.NORTH: [CARDINALS.EAST, CARDINALS.WEST],
    CARDINALS.EAST: [CARDINALS.NORTH, CARDINALS.SOUTH],
    CARDINALS.SOUTH: [CARDINALS.EAST, CARDINALS.WEST],
    CARDINALS.WEST: [CARDINALS.NORTH, CARDINALS.SOUTH]
}


def get_data(source):
    data = aoc.get_data(src=source, day=12, offset=3)
    return data.splitlines()


def find_neighbors(plant: str, coords: tuple, land, regions: list):
    if land[coords].get('region'):
        return

    y, x = coords
    fences = COMPASS.copy()
    region = None
    neighbors = []

    for direction in COMPASS:
        dy, dx = direction.value
        if (n_coords := (y + dy, x + dx)) in land:
            if land[n_coords].get('plant') == plant:
                neighbors.append(n_coords)
                fences.remove(direction)
                if plot_region := land[n_coords].get('region'):
                    region = plot_region

    if not region:
        region = len(regions) + 1
        regions.append([])

    land[(y, x)].update({'region': region})
    regions[region - 1].append(((y, x), fences))

    if neighbors:
        for neighbor in neighbors:
            find_neighbors(plant, neighbor, land, regions)


def map_land(data):
    land = {(y, x): {'plant': plant} for y, line in enumerate(data) for x, plant in enumerate(line)}
    regions = []
    for coords, plot in land.items():
        find_neighbors(plot.get('plant'), coords, land, regions)
    return regions


def build_fences(coords, fences, borders):
    consolidated_fences = []
    for fence in fences.copy():
        y, x = coords
        directions = GO_ALONG[fence]
        new_fence = set()

        new_fence.add(coords)
        fences.pop(fences.index(fence))

        for direction in directions:
            dy, dx = direction.value
            while (next_coords := (y + dy, x + dx)) in borders:
                if fence in (plot := borders[next_coords]):
                    new_fence.add(next_coords)
                    plot.pop(plot.index(fence))
                    y, x = next_coords
                else:
                    break

        if new_fence:
            consolidated_fences.append(new_fence)
    return consolidated_fences


def part1(data):
    regions = map_land(data)
    full_price = 0

    for region in regions:
        full_price += len(region) * sum([len(fences) for coords, fences in region])

    return full_price


def part2(data):
    regions = map_land(data)
    full_price = 0

    for region in regions:
        borders = {coords: fences for coords, fences in region if len(fences) > 0}
        perimeter = sum([len(build_fences(coords, fences, borders)) for coords, fences in sorted(borders.items())])
        full_price += len(region) * perimeter

    return full_price


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))