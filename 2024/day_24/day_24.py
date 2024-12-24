# Day 24: Crossed Wires

from functools import partial

import aoc


def get_data(source):
    data = aoc.get_data(src=source, day=24, offset=1).split('\n\n')
    values, operations = dict(), dict()
    for line in data[0].splitlines():
        v = line.split(':')
        values[v[0]] = v[1]
    for line in data[1].splitlines():
        v = line.replace('&gt;','>').split('->')
        operations[v[1].strip()] = v[0].strip().lower().replace('xor', '!=')
    return values, operations


def part1(data):
    values, operations = data

    while operations:
        for new_var, op in list(operations.items())[:]:
            val = op.split()[::2]
            if all(o in values for o in val):
                values[new_var] = str(int(eval(op.replace(val[0], values[val[0]]).replace(val[1], values[val[1]]))))
                del operations[new_var]

    z_values = [v for k, v in reversed(sorted(values.items())) if k.startswith('z')]
    return int(''.join(z_values), 2)


def part2(data):
    return 0


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
