# Day 7: Bridge Repair

import itertools
import operator
from functools import partial

import aoc


def get_data(source):
    data = aoc.get_data(src=source, day=7)
    data = data.splitlines()
    data = [[int(eq.split(':')[0]), tuple(map(int, eq.split(':')[1].strip().split()))] for eq in data]
    return data


def part1(data):
    operators = {
        '+': operator.add,
        '*': operator.mul
    }
    equations = []

    for target, numbers in data:
        nb_operations = len(numbers) - 1
        combinations = list(itertools.product(operators.keys(), repeat=nb_operations))
        nb_valid = 0

        for combination in combinations:
            operations = [(combination[i], numbers[i + 1]) for i in range(len(combination))]
            result = numbers[0]
            for cur_op, number in operations:
                result = operators[cur_op](result, number)
            nb_valid += result == target

        equations.append((target, nb_valid))

    return sum([k for k, v in equations if v > 0])


def part2(data):
    return 0


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
