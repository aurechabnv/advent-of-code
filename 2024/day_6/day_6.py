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


def print_map(floor_map):
    print('\n'.join([''.join(row) for row in floor_map]))


def get_next_direction(cur_direction: DIRECTION):
    index = DIR_SEQ.index(cur_direction)
    return DIR_SEQ[0] if index == len(DIR_SEQ) - 1 else DIR_SEQ[index + 1]


def get_cur_pos(floor_map, direction: DIRECTION):
    marker = direction.value
    return [(floor_map.index(row), row.index(col)) for row in floor_map for col in row if col == marker][0]


def move(floor_map, cur_direction: DIRECTION):
    move_y, move_x = DIR_VALUES.get(cur_direction)
    cur_y, cur_x = get_cur_pos(floor_map, cur_direction)
    next_marker = ''

    while next_marker != '#':
        floor_map[cur_y][cur_x] = 'x' # update current spot
        next_y = cur_y + move_y
        next_x = cur_x + move_x

        # out of boundaries
        if next_y >= len(floor_map) or next_y < 0 or next_x >= len(floor_map[0]) or next_x < 0:
            return True

        next_marker = floor_map[next_y][next_x]

        if next_marker != '#':
            floor_map[next_y][next_x] = cur_direction.value
            cur_y, cur_x = next_y, next_x
        else:
            new_direction = get_next_direction(cur_direction)
            floor_map[cur_y][cur_x] = new_direction.value

    return False


def part1(data):
    direction = DIRECTION.UP
    out_of_map = False
    while not out_of_map:
        out_of_map = move(data, direction)
        if not out_of_map:
            direction = get_next_direction(cur_direction=direction)
    # print_map(data)
    return sum([row.count('x') for row in data])


def part2(data):
    return 0


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.EXAMPLE)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
