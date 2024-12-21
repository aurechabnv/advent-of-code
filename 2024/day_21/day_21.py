# Day 21: Keypad Conundrum

from functools import partial

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
    '<' :(1, 0),
    'v': (1, 1),
    '>': (1, 2)
}


def move(a, b, c):
    return a[0] + b[0] * c, a[1] + b[1] * c

def get_pad_sequence(code, pad):
    cur_pos = pad['A']
    sequence = []
    for char in code:
        target = pad[char]
        char_sequence = []

        if cur_pos == target:
            char_sequence.append('A')
            sequence.extend(char_sequence)
            continue

        directions = {
            ARROW.LEFT: COMPASS.WEST,
            ARROW.UP: COMPASS.NORTH,
            ARROW.DOWN: COMPASS.SOUTH,
            ARROW.RIGHT: COMPASS.EAST,
        }
        check_directions = []
        for a, d in directions.items():
            delta_y, delta_x = target[0] - cur_pos[0], target[1] - cur_pos[1]
            dy, dx = d.value
            shift_y, shift_x = abs(delta_y), abs(delta_x)
            moves = 0
            if shift_y * dy == delta_y and dy != 0:
                moves = shift_y
            elif shift_x * dx == delta_x and dx != 0:
                moves = shift_x

            if moves > 0:
                valid_move = move(cur_pos, d.value, moves) not in pad.values()
                check_directions.append((valid_move, moves, a.value))

        sorted_directions = sorted(check_directions, key=lambda x: x[0])
        for _, cost, arrow in sorted_directions:
            for i in range(cost):
                char_sequence.append(arrow)

        char_sequence.append('A')
        cur_pos = target
        sequence.extend(char_sequence)

    # print(''.join(sequence))
    return sequence


def part1(data):
    total = 0
    for code in data:
        first_sequence = get_pad_sequence(code, NUM_PAD)
        second_sequence = get_pad_sequence(first_sequence, DIR_PAD)
        last_sequence = get_pad_sequence(second_sequence, DIR_PAD)
        complexity = len(last_sequence) * int(code.replace('A', ''))
        print(code, int(code.replace('A', '')), len(last_sequence), complexity, ''.join(last_sequence))
        total += complexity
    return total


def part2(data):
    return 0


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))