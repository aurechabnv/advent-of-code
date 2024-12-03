# Day 3: Mull It Over
import re

import aoc


def get_data(source) -> str:
    data = aoc.get_data(src=source, day=3)
    return data


def mul(a, b):
    return a * b


def part1(data):
    return sum(map(eval, re.findall(r"mul\(\d{1,3},\d{1,3}\)", data)))


def part2(data):
    matches = re.findall(r"(?:(do(?:n't)?\(\)).*?)?(mul\(\d{1,3},\d{1,3}\))", data)
    cur_cond = "do()"
    ops = []
    for cond, op in matches:
        cur_cond = cond if cond and cond != cur_cond else cur_cond
        if cur_cond == "do()":
            ops.append(op)
    return sum(map(eval, ops))


def part2_alt(data):
    matches = re.findall(r"(?:(do(?:n't)?\(\)).*?)?(mul\(\d{1,3},\d{1,3}\))", data)
    class _:
        cur_cond = "do()"
        @classmethod
        def check(cls, cond):
            cls.cur_cond = cond if cond and cond != cls.cur_cond else cls.cur_cond
            return cls.cur_cond == "do()"
    return sum(map(eval, [op for cond, op in matches if _.check(cond)]))


if __name__ == '__main__':
    aoc_data = get_data(source=aoc.SRC_INPUT)
    print(part1(aoc_data))
    aoc_data = get_data(source=aoc.SRC_INPUT)
    print(part2(aoc_data))
