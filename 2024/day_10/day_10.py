# Day 10: Hoof It

from collections import defaultdict
from functools import partial

import aoc


def get_data(source):
    data = aoc.get_data(src=source, day=10, offset=4)
    return data.splitlines()


def part1(data):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    grid = {(y, x): int(item) for y, line in enumerate(data) for x, item in enumerate(line)}
    paths = [[coords] for coords, height in grid.items() if not height]

    for i in range(1, 10):
        paths_to_check = [path for path in paths if len(path) == i]
        for path in paths_to_check:
            if len(path) == i:
                y, x = path[-1]
                next_steps = []
                for move_y, move_x in directions:
                    step = (y + move_y, x + move_x)
                    if step in grid and grid[step] == i:
                        next_steps.append(step)
                if len(next_steps) > 0:
                    path.append(next_steps[0])
                    if len(next_steps) > 1:
                        for step in next_steps[1:]:
                            new_path = path[:-1]
                            new_path.append(step)
                            paths.insert(paths.index(path)+1, new_path)
                else:
                    paths.pop(paths.index(path))

    count_paths = defaultdict(set)
    for path in paths:
        if len(path) == 10:
            count_paths[path[0]].add(path[9])
    # print(count_paths)

    return sum([len(score) for score in count_paths.values()])


def part2(data):
    return 0


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
