# Day 21: Keypad Conundrum

from functools import partial, cache

import aoc
from aoc import ARROW, COMPASS


def get_data(source):
    data = aoc.get_data(src=source, day=21, offset=3)
    return data.splitlines()


NUM_PAD = {
    '7': (0, 0),
    '8': (0, 1),
    '9': (0, 2),
    '4': (1, 0),
    '5': (1, 1),
    '6': (1, 2),
    '1': (2, 0),
    '2': (2, 1),
    '3': (2, 2),
    '0': (3, 1),
    'A': (3, 2)
}

DIR_PAD = {
    '^': (0, 1),
    'A': (0, 2),
    '<': (1, 0),
    'v': (1, 1),
    '>': (1, 2)
}

DIR_OPTIMIZED = {
    ARROW.LEFT: COMPASS.WEST,
    ARROW.UP: COMPASS.NORTH,
    ARROW.DOWN: COMPASS.SOUTH,
    ARROW.RIGHT: COMPASS.EAST
}


def do_move(position: tuple, direction: tuple, nb_steps: int):
    return position[0] + direction[0] * nb_steps, position[1] + direction[1] * nb_steps


@cache
def get_char_sequence(pad_name: str, start: tuple, target: tuple):
    pad = eval(pad_name)
    sequence = ''

    if start != target:
        moves = []

        # we compute the number of steps required in any direction
        # this ensures all moves of a given direction are made together
        # direction order is optimized to generate fewer moves in later turns
        for arrow, direction in DIR_OPTIMIZED.items():
            delta_y, delta_x = target[0] - start[0], target[1] - start[1]
            dy, dx = direction.value

            nb_moves = 0
            if (shift_y := abs(delta_y)) * dy == delta_y and dy != 0:
                nb_moves = shift_y
            elif (shift_x := abs(delta_x)) * dx == delta_x and dx != 0:
                nb_moves = shift_x

            if nb_moves > 0:
                valid_first_move = do_move(start, direction.value, nb_moves) not in pad.values()
                moves.append((valid_first_move, nb_moves, arrow.value))

        # default order is based on direction
        # we also prioritize moves that can be performed first if some cannot (thus avoiding empty space in keypads)
        for _, cost, arrow in sorted(moves, key=lambda x: x[0]):
            for i in range(cost):
                sequence += arrow

    sequence += 'A'
    return sequence


@cache
def get_pad_sequence(code, pad_name, max_level, level=1):
    pad = eval(pad_name)
    seq_length = 0

    start_position = pad['A']
    for char in code:
        target_position = pad[char]
        char_sequence = get_char_sequence(pad_name, start_position, target_position)

        if level < max_level:
            char_seq_length = get_pad_sequence(char_sequence, 'DIR_PAD', max_level, level + 1)
        else:
            char_seq_length = len(char_sequence)

        seq_length += char_seq_length
        start_position = target_position

    return seq_length


def find_total_complexity(data, max_level):
    complexity = 0
    for code in data:
        seq_length = get_pad_sequence(code, 'NUM_PAD', max_level)
        complexity += seq_length * int(code[:-1])
    return complexity


def part1(data):
    return find_total_complexity(data, max_level=3)


def part2(data):
    return find_total_complexity(data, max_level=26)


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
