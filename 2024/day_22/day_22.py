# Day 22: Monkey Market

from functools import partial

import aoc


def get_data(source):
    data = aoc.get_data(src=source, day=22, offset=1)
    return list(map(int, data.splitlines()))


def get_secret_number(number):
    secret_number = (number ^ (number * 64)) % 16777216
    secret_number = (secret_number ^ (secret_number // 32)) % 16777216
    secret_number = (secret_number ^ (secret_number * 2048)) % 16777216
    return secret_number


def part1(data):
    total = 0
    for number in data:
        secret_number = number
        for _ in range(2000):
            secret_number = get_secret_number(secret_number)
        total += secret_number
    return total


def part2(data):
    return 0


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
