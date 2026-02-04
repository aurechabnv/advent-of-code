# Day 17: Chronospatial Computer

from functools import partial
from re import compile

import aoc


def get_data(source, offset=0):
    data = aoc.get_data(src=source, year=2024, day=17, offset=offset)
    data = data.split('\n\n')
    regex = compile(r'-?\d+')
    return [list(map(int, regex.findall(line))) for line in data]


class Computer:
    def __init__(self, data):
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
            4: None,
            5: None,
            6: None,
            7: 7
        }
        self.original_values, self.commands = data
        self.set_abc()

    def set_abc(self, a=None):
        self.operands[4] = a if a else self.original_values[0]
        self.operands[5] = self.original_values[1]
        self.operands[6] = self.original_values[2]

    def start(self):
        self.outputs = []
        self.pointer = 0
        while self.pointer < len(self.commands):
            instruction = self.commands[self.pointer]
            operand = self.commands[(self.pointer + 1)]
            jump = self.instructions[instruction](operand)
            if jump:
                self.pointer += 2
        return ','.join(self.outputs)

    def find_copy(self):
        compare_list = list(map(str, self.commands))
        possible_a = [0]
        for i in range(1, len(self.commands) + 1):
            found = []
            for p in possible_a:
                for j in range(8):
                    a_value = p * (2 ** 3) + j
                    self.set_abc(a=a_value)
                    self.start()
                    if self.outputs == compare_list[-i:]:
                        found.append(a_value)
            possible_a = found
        return min(possible_a)

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
        return self.operands[4] // (2 ** self.operands[operand])



def part1(data):
    computer = Computer(data)
    return computer.start()


def part2(data):
    computer = Computer(data)
    return computer.find_copy()


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
