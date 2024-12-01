# Day

from utils import utils


def get_data(source) -> str:
    data = utils.get_data(src=source, day=0)
    return data


def part1(data):
    return True


def part2(data):
    return True


aoc_data = get_data(utils.SRC_EXAMPLE)
print(part1(aoc_data))
print(part2(aoc_data))
