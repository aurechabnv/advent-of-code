# Day 23: Lan Party

import itertools
from functools import partial

import aoc


def get_data(source):
    data = aoc.get_data(src=source, day=23)
    return [v.split('-') for v in data.splitlines()]


def find_network(networks, computers):
    for i, net in enumerate(networks):
        if all([c in net for c in computers]):
            return True
    return False


def get_networks(data):
    networks = []
    for i, computer_link in enumerate(data):
        network_updated = False
        for j, network in enumerate(networks):
            if any([c in network for c in computer_link]):
                check_value = [c for c in computer_link if c not in network]
                if check_value:
                    if all([find_network(data, [c, check_value[0]]) for c in network]):
                        networks[j].append(check_value[0])
                        network_updated = True
                        break
        if not network_updated:
            networks.append(computer_link)
    return networks


def part1(data):
    networks = get_networks(data)
    test_dict = dict()
    networks = [sorted(n) for n in networks]
    for n in networks:
        if len(n) > 3:
            networks.extend(list(itertools.combinations(n, 3)))
            continue
        n = tuple(n)
        if n not in test_dict:
            test_dict[n] = any([v.startswith('t') and len(n) > 2 for v in n])
    return sum(list(test_dict.values()))


def part2(data):
    networks = get_networks(data)
    max_value = max(networks, key=len)
    return ','.join(sorted(max_value))


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.EXAMPLE)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
