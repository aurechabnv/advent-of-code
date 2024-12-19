# Day 5: Print Queue

from functools import partial

import aoc


def get_data(source):
    data = aoc.get_data(src=source, day=5).split('\n\n')
    rules = [tuple(map(int, rule.split('|'))) for rule in data[0].splitlines()]
    updates = [list(map(int, update.split(','))) for update in data[1].splitlines()]
    return rules, updates


def get_applicable_rules(update: list[int], rules: list[tuple]):
    return [rule for rule in rules if rule[0] in update and rule[1] in update]


def is_valid(update: list[int], rules: list[tuple]):
    for rule in rules:
        if update.index(rule[0]) > update.index(rule[1]):
            return False
    return True


def fix_order(update: list[int], rules: list[tuple]):
    update = update.copy()
    for rule in rules:
        index_left, index_right = update.index(rule[0]), update.index(rule[1])
        if index_left > index_right:
            el = update.pop(index_left)
            update.insert(index_right, el)
    if not is_valid(update, rules):
        update = fix_order(update, rules)
    return update


def sum_up_middle_values(updates):
    return sum([update[len(update) // 2] for update in updates])


def part1(rules: list[tuple], updates: list[list]):
    valid_updates = [update for update in updates if is_valid(update, get_applicable_rules(update, rules))]
    return sum_up_middle_values(valid_updates)


def part2(rules: list[tuple], updates: list[list]):
    invalid_updates = [update for update in updates if not is_valid(update, get_applicable_rules(update, rules))]
    fixed_updates = [fix_order(update, get_applicable_rules(update, rules)) for update in invalid_updates]
    return sum_up_middle_values(fixed_updates)


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, *aoc_data))
    aoc.benchmark('Part 2', partial(part2, *aoc_data))
