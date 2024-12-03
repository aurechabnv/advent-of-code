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
    instruction = "do()"
    instructions = []
    for t in matches:
        if t[0] and t[0] != instruction:
            instruction = t[0]
        if instruction == "do()":
            instructions.append(t[1])
    return sum(map(eval, instructions))


if __name__ == '__main__':
    aoc_data = get_data(source=aoc.SRC_INPUT)
    print(part1(aoc_data))
    aoc_data = get_data(source=aoc.SRC_INPUT)
    print(part2(aoc_data))
