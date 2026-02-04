# Day 22: Monkey Market

from collections import defaultdict
from functools import partial

import aoc


def get_data(source, offset=5):
    data = aoc.get_data(src=source, year=2024, day=22, offset=offset)
    return list(map(int, data.splitlines()))


def get_secret_number(number):
    secret_number = (number ^ (number * 64)) % 16777216
    secret_number = (secret_number ^ (secret_number // 32)) % 16777216
    secret_number = (secret_number ^ (secret_number * 2048)) % 16777216
    return secret_number


def part1(data):
    total = 0
    for buyer in data:
        secret_number = buyer
        for _ in range(2000):
            secret_number = get_secret_number(secret_number)
        total += secret_number
    return total


def part2(data):
    sequences = defaultdict(int)

    for buyer in data:
        secret_number = buyer
        buyer_numbers = [(secret_number % 10, 0)]
        known_sequences = set()

        # save price and price difference
        for i in range(2000):
            secret_number = get_secret_number(secret_number)
            price = secret_number % 10
            buyer_numbers.append((price, (price - buyer_numbers[-1][0])))

        # extract sequences and add the corresponding price in the dictionary
        # process only first occurrence of a sequence per buyer
        prices, changes = tuple(zip(*buyer_numbers))
        for i in range(len(buyer_numbers) - 3):
            seq = changes[i : i + 4]
            if seq not in known_sequences:
                sequences[seq] += prices[i + 3]
                known_sequences.add(seq)

    return max(sequences.values())


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
