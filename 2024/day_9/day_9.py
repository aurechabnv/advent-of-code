# Day 9: Disk Fragmenter

import itertools
from functools import partial

import aoc


def get_data(source):
    data = aoc.get_data(src=source, day=9)
    return data


def get_checksum(liste):
    return sum([size * name for size, name in enumerate(liste) if name != '.'])


def part1(data):
    disk_grid = [[int(n), (i//2 if not i % 2 else '.')] for i, n in enumerate(data)]
    disk = []
    files_to_move = disk_grid[::2][::-1]
    max_length = len(disk_grid)

    for i, (n, val) in enumerate(disk_grid):
        if i == max_length:
            break
        if val == '.':
            while n > 0:
                if files_to_move[0][0] == 0:
                    files_to_move = files_to_move[1:]
                    max_length -= 2
                spaces, nb = files_to_move[0]
                disk.extend(itertools.repeat(nb, min(spaces, n)))
                files_to_move[0][0] = max(spaces - n, 0)
                n = n - min(spaces, n)
        else:
            disk.extend(itertools.repeat(val, n))

    return get_checksum(disk)


def part2(data):
    disk_dict = {i: [(int(n), (i // 2 if not i % 2 else '.'))] for i, n in enumerate(data)}
    files = {k: v for k, v in disk_dict.items() if not k % 2}
    spaces = {k: v for k, v in disk_dict.items() if k % 2}

    for k_file in list(files.keys())[::-1]:
        file = files[k_file][0]
        f_size = file[0]

        for k_space, items in spaces.items():
            s_size = items[-1][0]
            if f_size <= s_size and k_file > k_space:
                spaces[k_space].pop(-1)
                spaces[k_space].extend([file, (s_size - f_size, '.')])
                files[k_file] = [(f_size, '.')]
                break

    disk_dict = { **disk_dict, **files, **spaces }
    disk_grid = itertools.chain(*disk_dict.values())
    disk = itertools.chain.from_iterable([itertools.repeat(name, size) for size, name in disk_grid])
    return get_checksum(disk)

if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
