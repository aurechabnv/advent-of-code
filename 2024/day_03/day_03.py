# Day 3: Mull It Over

from functools import partial
import re

import aoc


def get_data(source, offset=0) -> str:
    data = aoc.get_data(src=source, day=3, offset=offset)
    return data


regex_part1 = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
regex_part2 = re.compile(r"(?:(do(?:n't)?\(\)).*?)?(mul\(\d{1,3},\d{1,3}\))")

def mul(a, b):
    return a * b


def part1(data):
    return sum(map(eval, regex_part1.findall(data)))


def part2(data):
    matches = regex_part2.findall(data)
    cur_cond = "do()"
    ops = []
    for cond, op in matches:
        cur_cond = cond if cond and cond != cur_cond else cur_cond
        if cur_cond == "do()":
            ops.append(op)
    return sum(map(eval, ops))


def part2_alt(data):
    matches = regex_part2.findall(data)
    class _:
        cur_cond = "do()"
        @classmethod
        def check(cls, cond):
            cls.cur_cond = cond if cond and cond != cls.cur_cond else cls.cur_cond
            return cls.cur_cond == "do()"
    return sum(map(eval, [op for cond, op in matches if _.check(cond)]))


if __name__ == '__main__':
    aoc_data = get_data(source=aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
    aoc.benchmark('Part 2 alt', partial(part2_alt, aoc_data))
