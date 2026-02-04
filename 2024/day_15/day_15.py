# Day 15: Warehouse Woes

from functools import partial

import aoc
from aoc import DIRECTIONS, ARROW


def get_data(source):
    data = aoc.get_data(src=source, year=2024, day=15, offset=0).split('\n\n')
    warehouse = data[0]
    steps = data[1]
    if source == aoc.SOURCE.EXAMPLE:
        steps = steps.replace('&lt;', '<').replace('&gt;', '>')
    return warehouse, steps.replace('\n', '')


class TILE:
    ROBOT = '@'
    CRATE = 'O'
    CRATE_L = '['
    CRATE_R = ']'
    WALL = '#'
    EMPTY = '.'
    BIG_CRATE = [CRATE_L, CRATE_R]
    CRATES = [CRATE, CRATE_L, CRATE_R]


def get_big_crate_coords(tile_type, t1_coords):
    dy, dx = DIRECTIONS.get(ARROW.RIGHT if tile_type == TILE.CRATE_L else ARROW.LEFT).value
    t2_coords = t1_coords[0] + dy, t1_coords[1] + dx
    return sorted([t1_coords, t2_coords])


def move_tile(warehouse, position, direction, tiles_to_move=None):
    if tiles_to_move is None:
        tiles_to_move = set()

    dy, dx = direction.value
    cur_tile = warehouse[position]
    is_crate = (cur_tile in TILE.CRATES)
    new_position = None

    # get next tiles
    if cur_tile in TILE.BIG_CRATE:
        big_crate_coords = get_big_crate_coords(cur_tile, position)
        tiles_to_move.update(big_crate_coords)
        next_tiles = {c: warehouse[c] for y, x in big_crate_coords if (c := (y + dy, x + dx)) not in tiles_to_move}
    else:
        tiles_to_move.add(position)
        new_position = position[0] + dy, position[1] + dx
        next_tiles = {new_position: warehouse[new_position]}

    # check next tiles
    if TILE.WALL in next_tiles.values():
        return False if is_crate else position

    elif any([t in TILE.CRATES for t in next_tiles.values()]):
        moving = [move_tile(warehouse, c, direction, tiles_to_move) for c, t in next_tiles.items() if t in TILE.CRATES]

        if not all(moving):
            return False if is_crate else position
        elif is_crate:
            return True

    elif all([t == TILE.EMPTY for t in next_tiles.values()]) and is_crate:
        return True

    # move identified tiles
    if cur_tile == TILE.ROBOT:
        cur_state = {c: warehouse[c] for c in tiles_to_move}
        tiles_moved = set()
        for c in tiles_to_move:
            tiles_moved.add(new_coords := (c[0] + dy, c[1] + dx))
            warehouse[new_coords] = cur_state[c]

        tiles_freed = tiles_to_move - tiles_moved
        for c in tiles_freed:
            warehouse[c] = TILE.EMPTY

    return new_position


def expand_warehouse(config):
    expand = {
        TILE.WALL: '##',
        TILE.CRATE: '[]',
        TILE.EMPTY: '..',
        TILE.ROBOT: '@.'
    }
    for key in expand.keys():
        config = config.replace(key, expand[key])
    return config


def get_crates_gps_total(data, expand=False):
    config, steps = data
    if expand:
        config = expand_warehouse(config)
    warehouse = aoc.init_grid(config)
    robot = [coords for coords, piece in warehouse.items() if piece == TILE.ROBOT][0]

    for step in steps:
        direction = DIRECTIONS.get(ARROW(step))
        robot = move_tile(warehouse, robot, direction)

    aoc.print_grid(warehouse)
    crates = [100 * y + x for (y, x), tile in warehouse.items() if tile in [TILE.CRATE, TILE.CRATE_L]]
    return sum(crates)


def part1(data):
    return get_crates_gps_total(data)


def part2(data):
    return get_crates_gps_total(data, expand=True)


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
