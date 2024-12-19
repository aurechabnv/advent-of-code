# Day 9: Disk Fragmenter

import itertools
from functools import partial

import aoc


def get_data(source):
    data = aoc.get_data(src=source, day=9)
    return data


def get_checksum(array):
    return sum([size * name for size, name in enumerate(array) if name != '.'])


def part1(data):
    disk_grid = [[int(n), (i//2 if not i % 2 else '.')] for i, n in enumerate(data)]
    files = disk_grid[::2][::-1]
    disk = []

    for blocks, item in disk_grid:
        if item != '.':
            disk.extend(itertools.repeat(item, blocks))
        else:
            while blocks > 0:
                # if the file has no block left, discard it
                if files[0][0] == 0:
                    files.pop(0)      # remove first file
                    disk_grid.pop(-1) # remove file item from the end
                    disk_grid.pop(-1) # remove space item

                # use first file from reverse list
                file_size, file_id = files[0]

                disk.extend(itertools.repeat(file_id, min(file_size, blocks)))

                # update remaining nb of blocks for current spot and the size of the file we used
                files[0][0] = max(file_size - blocks, 0)
                blocks = blocks - min(file_size, blocks)

    return get_checksum(disk)


def part2(data):
    disk_dict = {i: [(int(n), (i // 2 if not i % 2 else '.'))] for i, n in enumerate(data)}
    file_locations = {k: v for k, v in disk_dict.items() if not k % 2}
    space_locations = {k: v for k, v in disk_dict.items() if k % 2}

    # for each file in reverse order
    for f_key in reversed(file_locations.keys()):
        file = file_locations[f_key][0]
        f_size = file[0]

        # check if a free space is available starting from the left
        # last item of a location defines current free space
        for s_key, items in space_locations.items():
            s_size = items[-1][0]

            # if file size is ok and file is after selected location
            if f_size <= s_size and f_key > s_key:
                space_locations[s_key].pop(-1)                                 # remove last item from current free location
                space_locations[s_key].extend([file, (s_size - f_size, '.')])  # append file item and set remaining space
                file_locations[f_key] = [(f_size, '.')]                        # update original file location to free space
                break

    disk_dict = { **disk_dict, **file_locations, **space_locations }
    disk_grid = itertools.chain(*disk_dict.values())
    disk = itertools.chain(*[itertools.repeat(name, size) for size, name in disk_grid])

    return get_checksum(disk)


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
