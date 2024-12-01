# Day 1: Historian Hysteria

from utils import utils


def get_data(source) -> (list, list):
    list1, list2 = [], []

    data = utils.get_data(src=source, day=1).split('\n')

    for line in data:
        split_line = line.split()
        list1.append(int(split_line[0]))
        list2.append(int(split_line[1]))

    return list1, list2


def part1(list1, list2):
    list1.sort()
    list2.sort()

    total_distance = 0
    for i in range(len(list1)):
        total_distance += abs(list1[i] - list2[i])

    return total_distance


def part2(list1, list2):
    similarity_score = 0

    for n in list1:
        multiplier = list2.count(n)
        similarity_score += multiplier * n

    return similarity_score


list_one, list_two = get_data(utils.SRC_INPUT)
print(part1(list_one, list_two))
print(part2(list_one, list_two))
