# Day 2: Red-Nosed Reports

from utils import utils


def get_data(source):
    data = utils.get_data(src=source, day=2)
    data = data.splitlines()
    return [list(map(int, item.split())) for item in data]


def analysis(report: list) -> bool:
    increase = None
    for i in range(len(report)):
        if i == len(report) - 1:
            return True

        # check whether the pattern has changed
        if report[i] < report[i + 1]:
            if increase is None:
                increase = True
            elif not increase:
                return False
        elif report[i] > report[i + 1]:
            if increase is None:
                increase = False
            elif increase:
                return False

        # check whether diff is within accepted limits
        diff = abs(report[i] - report[i + 1])
        if not 0 < diff <= 3:
            return False
    return True


def part1(data):
    results = []
    for report in data:
        results.append(analysis(report))
    return results.count(True)


def part2(data: list[list]):
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
    aoc_data = get_data(utils.SRC_INPUT)
    print(part1(aoc_data))
    print(part2(aoc_data))
