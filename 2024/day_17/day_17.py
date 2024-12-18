# Day 17: Chronospatial Computer

from functools import partial
from math import trunc
from re import compile

import aoc


def get_data(source, offset=0):
    data = aoc.get_data(src=source, day=17, offset=offset)
    data = data.split('\n\n')
    regex = compile(r'-?\d+')
    return [list(map(int, regex.findall(line))) for line in data]


class Computer:
    def __init__(self, data):
        variables, self.commands = data
        self.pointer = 0
        self.outputs = []
        self.instructions = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv
        }
        self.operands = {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: variables[0],
            5: variables[1],
            6: variables[2],
            7: 7
        }

    def start(self):
        while self.pointer < len(self.commands):
            instruction = self.commands[self.pointer]
            operand = self.commands[(self.pointer + 1)]
            jump = self.instructions[instruction](operand)
            if jump:
                self.pointer += 2
        return ','.join(self.outputs)

    def adv(self, operand):
        self.operands[4] = self._dv(operand)
        return True

    def bxl(self, operand):
        self.operands[5] = self.operands[5] ^ operand
        return True

    def bst(self, operand):
        self.operands[5] = self.operands[operand] % 8
        return True

    def jnz(self, operand):
        if self.operands[4] != 0:
            self.pointer = operand
            return False
        return True

    def bxc(self, operand):
        self.operands[5] = self.operands[5] ^ self.operands[6]
        return True

    def out(self, operand):
        self.outputs.append(str(self.operands[operand] % 8))
        return True

    def bdv(self, operand):
        self.operands[5] = self._dv(operand)
        return True

    def cdv(self, operand):
        self.operands[6] = self._dv(operand)
        return True

    def _dv(self, operand):
        return trunc(self.operands[4] / (2 ** self.operands[operand]))



def part1(data):
    computer = Computer(data)
    return computer.start()


def part2(data):
    return 0


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
