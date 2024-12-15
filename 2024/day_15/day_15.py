# Day 15: Warehouse Woes

from functools import partial

import aoc


def get_data(source):
    data = aoc.get_data(src=source, day=15, offset=0).split('\n\n')
    warehouse = {(y, x): el for y, line in enumerate(data[0].split('\n')) for x, el in enumerate(line)}
    steps = data[1].replace('&lt;','<').replace('&gt;','>').replace('\n','')
    return warehouse, steps


class PIECE:
    ROBOT = '@'
    CRATE = 'O'
    WALL = '#'
    EMPTY = '.'


DIRECTIONS = {
    '<': (0, -1),
    '>': (0, 1),
    '^': (-1, 0),
    'v': (1, 0)
}


def move_piece(grid, start, direction):
    y, x = start
    dy, dx = direction

    coords = y + dy, x + dx
    if coords in grid:
        if grid[coords] == PIECE.WALL:
            # do nothing
            return start
        elif grid[coords] == PIECE.CRATE:
            # see if it can move
            moving = move_piece(grid, coords, direction)
            if moving == coords:
                return start

        # move piece
        grid[coords] = grid[start]
        if grid[coords] == PIECE.ROBOT:
            grid[start] = PIECE.EMPTY
        return coords


def show_warehouse(warehouse):
    array = []
    for (y, x), value in warehouse.items():
        if y >= len(array):
            array.append([])
        array[y].append(str(value))
    print('\n'.join([''.join(line) for line in array]))


def part1(data):
    warehouse, steps = data
    robot = [coords for coords, piece in warehouse.items() if piece == PIECE.ROBOT][0]

    for step in steps:
        direction = DIRECTIONS[step]
        robot = move_piece(warehouse, robot, direction)

    show_warehouse(warehouse)
    crates = [100 * y + x for (y, x), el in warehouse.items() if el == PIECE.CRATE]
    return sum(crates)


def part2(data):
    return 0


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
