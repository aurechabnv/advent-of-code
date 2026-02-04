# Day 7: Bridge Repair

import itertools
import operator
from functools import partial

import aoc


def get_data(source):
    data = aoc.get_data(src=source, year=2024, day=7)
    data = data.splitlines()
    data = [[int(eq.split(':')[0]), tuple(map(int, eq.split(':')[1].strip().split()))] for eq in data]
    return data


def sum_up_valid_results(data, operators):
    results = []
    for number, sequence in data:
        combinations = list(itertools.product(operators.keys(), repeat=len(sequence)-1))
        for combination in combinations:
            result = sequence[0]
            for symbol, nb in zip(combination, sequence[1:]):
                result = operators[symbol](result, nb)
            if result == number:
                results.append(number)
                break
    return sum(results)


def part1(data):
    operators = {
        '+': operator.add,
        '*': operator.mul
    }
    return sum_up_valid_results(data, operators)


def part2(data):
    operators = {
        '+': operator.add,
        '*': operator.mul,
        '||': lambda a, b: int(f'{a}{b}')
    }
    return sum_up_valid_results(data, operators)


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
