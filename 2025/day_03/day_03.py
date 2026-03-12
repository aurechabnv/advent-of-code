# Day 3: Lobby

from functools import partial

import aoc


def get_data(source):
    data = aoc.get_data(src=source, year=2025, day=3)
    return data.splitlines()


def part1(data):
    joltages = []
    for line in data:
        start, end = 0, 0
        for idx, char in enumerate(line):
            char = int(char)
            if char > start and idx != len(line) - 1:
                start = char
                end = 0
            elif char > end:
                end = char
        joltages.append(int(f"{start}{end}"))
    return sum(joltages)


def part2(data):
    joltages = []

    for bank in data:
        required_batteries = 12
        batteries = []
        working_bank = bank

        while len(batteries) < required_batteries:
            cur_battery_idx = 0
            max_idx = len(working_bank) - (required_batteries - len(batteries))

            for idx in range(len(working_bank)):
                if working_bank[idx] > working_bank[cur_battery_idx] and idx <= max_idx:
                    cur_battery_idx = idx
                if idx == max_idx:
                    batteries.append(working_bank[cur_battery_idx])
                    working_bank = working_bank[cur_battery_idx + 1:]
                    break

        joltages.append(int(''.join(batteries)))

    return sum(joltages)


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
