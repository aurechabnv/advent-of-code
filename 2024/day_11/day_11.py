# Day 11: Plutonian Pebbles

from functools import partial

import aoc


def get_data(source):
    if source == aoc.SOURCE.EXAMPLE:
        data = '125 17'
    else:
        data = aoc.get_data(src=source, day=11)
    return data.split()


def part1(data):
    pebbles = list(map(int, data))
    # print(pebbles)
    for _ in range(25):
        for stone in pebbles.copy():
            index = pebbles.index(stone)
            if stone == 0:
                pebbles[index] = 1
            elif not len(string := str(stone)) % 2:
                pebbles[index] = int(string[len(string)//2:])
                pebbles.insert(index, int(string[:len(string)//2]))
            else:
                pebbles[index] = stone * 2024
        # print('turn', _ + 1, len(pebbles))
    return len(pebbles)


def part2(data):
    return 0


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
