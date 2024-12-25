# Day 24: Crossed Wires

import itertools
from functools import partial

import aoc


def get_data(source, offset=1):
    data = aoc.get_data(src=source, day=24, offset=offset).split('\n\n')
    return data


def init_dicts(data):
    values, operations = dict(), dict()
    for line in data[0].splitlines():
        v = line.split(':')
        values[v[0]] = v[1].strip()
    for line in data[1].splitlines():
        v = line.replace('&gt;','>').split('->')
        operations[v[1].strip()] = v[0].strip().lower().replace('xor', '!=')
    return values, operations


def perform_operations(values, operations):
    while operations:
        for new_var, op in list(operations.items())[:]:
            val = op.split()[::2]
            if all(o in values for o in val):
                values[new_var] = str(int(eval(op.replace(val[0], values[val[0]]).replace(val[1], values[val[1]]))))
                del operations[new_var]


def get_bin_value(values, name):
    return int(''.join([v for k, v in reversed(sorted(values.items())) if k.startswith(name)]), 2)


def part1(data):
    values, operations = init_dicts(data)
    perform_operations(values, operations)
    return get_bin_value(values, 'z')


def part2(data):
    values, operations = init_dicts(data)
    inverse_values = [
        ('z24', 'fpq'), # z24 supposed to be set after z23
        ('nqk', 'z07'), # z07 to be set before z08
        ('srn', 'z32'), # z32 to be set with xor
        ('fgt', 'pcp')  # OR operation requires previous AND in init values
    ]
    for a, b in inverse_values:
        op_a, op_b = operations[a], operations[b]
        operations[a] = op_b
        operations[b] = op_a

    perform_operations(values, operations)

    return ','.join(sorted(list(itertools.chain(*inverse_values))))


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
