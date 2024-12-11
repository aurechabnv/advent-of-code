# Day 11: Plutonian Pebbles

from functools import partial

import aoc


def get_data(source):
    if source == aoc.SOURCE.EXAMPLE:
        data = '125 17'
    else:
        data = aoc.get_data(src=source, day=11)
    return data.split()


def count_pebbles(data, turns):
    pebbles = list(map(int, data))
    # print(pebbles)
    for _ in range(turns):
        for stone in pebbles.copy():
            index = pebbles.index(stone)
            if stone == 0:
                pebbles[index] = 1
            elif not len(string := str(stone)) % 2:
                pebbles[index] = int(string[:len(string)//2])
                pebbles.insert(index + 1, int(string[len(string)//2:]))
            else:
                pebbles[index] = stone * 2024
        # print('turn', _ + 1, len(pebbles))
    return len(pebbles)


def part1(data):
    return count_pebbles(data, turns=25)


def part2(data):
    return count_pebbles(data, turns=75)


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.EXAMPLE)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
