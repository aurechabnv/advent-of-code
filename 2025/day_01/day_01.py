# Day 1: Secret Entrance

from functools import partial

import aoc


def get_data(source):
    data = aoc.get_data(src=source, day=1)
    data = data.split('\n')
    shifts = []
    for el in data:
        nb = int(el[1:])
        shifts.append(-nb if 'L' in el else nb)
    return shifts


def part1(data):
    dial = 50
    counter = 0
    for shift in data:
        dial += shift
        if not dial % 100:
            counter += 1

    return counter


def part2(data):
    dial = 50
    counter = 0

    for shift in data:
        start = dial
        shift_index = dial + shift
        dial = shift_index % 100

        # resulting dial differs from the computed shift, so full turns must have been performed
        if shift_index != dial:
            nb_turns = 0

            # positive shift
            if shift > 0:
                nb_turns = shift_index // 100

                # remove one turn if dial points at 0 at the end
                if dial == 0:
                    nb_turns -= 1

            # negative shift
            if shift < 0:
                shift = abs(shift)

                # get basic number of turns of big rotation (>100)
                nb_turns += (nb_of_full_turns := shift // 100)

                # add a rotation if the remainder is still larger than starting point
                if (shift - nb_of_full_turns * 100) > start > 0:
                    nb_turns += 1

            counter += nb_turns

        # count 1 if dial is on 0 at the end of the rotation
        if not dial:
            counter += 1

    return counter


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
