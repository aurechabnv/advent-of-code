# Day 6: Guard Gallivant

from enum import Enum
from functools import partial

import aoc


def get_data(source):
    data = aoc.get_data(src=source, day=6)
    return [list(item) for item in data.splitlines()]


class DIRECTION(Enum):
    UP = '^'
    RIGHT = '>'
    DOWN = 'v'
    LEFT = '<'

DIR_SEQ = [DIRECTION.UP, DIRECTION.RIGHT, DIRECTION.DOWN, DIRECTION.LEFT]

DIR_VALUES = {
    DIRECTION.UP: (-1, 0),
    DIRECTION.RIGHT: (0, 1),
    DIRECTION.DOWN: (1, 0),
    DIRECTION.LEFT: (0, -1)
}


def get_next_direction(cur_direction: DIRECTION):
    index = DIR_SEQ.index(cur_direction)
    return DIR_SEQ[0] if index == len(DIR_SEQ) - 1 else DIR_SEQ[index + 1]


def get_cur_pos(floor_map, direction: DIRECTION):
    marker = direction.value
    return [(floor_map.index(row), row.index(col)) for row in floor_map for col in row if col == marker][0]


def map_patrol(floor_map, detect_loop=False):
    direction = DIRECTION.UP
    route = set()
    cur_y, cur_x = get_cur_pos(floor_map, direction)
    looping = False

    while True:
        move_y, move_x = DIR_VALUES.get(direction)
        cur_spot = (cur_y, cur_x, direction.value) if detect_loop else (cur_y, cur_x)

        if detect_loop and cur_spot in route:
            looping = True
            break

        route.add(cur_spot)

        next_y = cur_y + move_y
        next_x = cur_x + move_x

        # out of bounds
        if next_y >= len(floor_map) or next_y < 0 or next_x >= len(floor_map[0]) or next_x < 0:
            break

        next_marker = floor_map[next_y][next_x]
        if next_marker == '#' or next_marker == 'O':
            direction = get_next_direction(direction)
        else:
            cur_y, cur_x = next_y, next_x

    return route, looping


def part1(data):
    route, _ = map_patrol(data)
    return len(route)


def part2(data):
    route, _ = map_patrol(data)
    loops = 0
    for cur_y, cur_x in route:
        if data[cur_y][cur_x] != '^':
            data[cur_y][cur_x] = 'O'
            _, looping = map_patrol(data, detect_loop=True)
            loops += looping
            data[cur_y][cur_x] = '.'
    return loops


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
