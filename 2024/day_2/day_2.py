# Day 2: Red-Nosed Reports

from functools import partial

import aoc


def get_data(source):
    data = aoc.get_data(src=source, day=2)
    data = data.splitlines()
    return [list(map(int, item.split())) for item in data]


def analysis(report: list) -> bool:
    cur_direction = None
    for i in range(len(report)-1):
        # check whether the direction has changed
        direction = 1 if report[i] < report[i + 1] else -1
        if cur_direction is None:
            cur_direction = direction
        changed_direction = direction != cur_direction

        # get the difference
        diff = abs(report[i] - report[i + 1])

        # should be within accepted limits and moving in the same direction
        # if any of these conditions is wrong, the report is deemed unsafe
        if not 0 < diff <= 3 or changed_direction:
            return False
    return True


def part1(data: list[list]) -> int:
    results = []
    for report in data:
        results.append(analysis(report))
    return results.count(True)


def part2(data: list[list]) -> int:
    results = []
    for report in data:
        safe = analysis(report)
        if not safe:
            for i in range(len(report)):
                modified_report = report.copy()
                del modified_report[i]
                safe = analysis(modified_report)
                if safe:
                    break
        results.append(safe)
    return results.count(True)


if __name__ == '__main__':
    aoc_data = get_data(aoc.SRC_INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
