# Day 9: Disk Fragmenter

import itertools
from functools import partial

import aoc


def get_data(source):
    data = aoc.get_data(src=source, day=9)
    return data


def get_checksum(liste):
    return sum([i * nb for i, nb in enumerate(liste)])


def part1(data):
    disk_map = [[int(n), (i//2 if not i % 2 else '.')] for i, n in enumerate(data)]
    new_disk_map = []
    files_to_move = disk_map[::2][::-1]
    max_length = len(disk_map)

    for i, (n, val) in enumerate(disk_map):
        if i == max_length:
            break
        if val == '.':
            while n > 0:
                if files_to_move[0][0] == 0:
                    files_to_move = files_to_move[1:]
                    max_length -= 2
                spaces, nb = files_to_move[0]
                new_disk_map.extend(itertools.repeat(nb, min(spaces, n)))
                files_to_move[0][0] = max(spaces - n, 0)
                n = n - min(spaces, n)
        else:
            new_disk_map.extend(itertools.repeat(val, n))

    return get_checksum(new_disk_map)


def part2(data):
    return 0


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    # aoc_data = '2333133121414131402352134'
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
