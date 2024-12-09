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
    disk_map = {i: [(int(n), (i // 2 if not i % 2 else '.'))] for i, n in enumerate(data)}
    files = {k: v for k, v in disk_map.items() if not k % 2}
    spaces = {k: v for k, v in disk_map.items() if k % 2}

    for k in list(files.keys())[::-1]:
        size, name = files.get(k)[0]

        for h, values in spaces.items():
            s_size, s_name = values[-1]
            if size <= s_size and k > h:
                spaces.get(h).pop(-1)
                spaces[h].append(files.get(k)[0])
                spaces[h].append((s_size - size, '.'))
                files[k] = [(size, '.')]
                break

    disk_map.update(files)
    disk_map.update(spaces)
    array = []
    for values in disk_map.values():
        array.extend(values)
    new_disk_map = list(itertools.chain.from_iterable([list(itertools.repeat(name, size)) for size, name in array]))
    return get_checksum(new_disk_map)

if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
