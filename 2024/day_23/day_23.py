# Day 23: LAN Party

import itertools
from collections import defaultdict
from functools import partial

import aoc


def get_data(source):
    data = aoc.get_data(src=source, year=2024, day=23)
    return [tuple(sorted(v.split('-'))) for v in data.splitlines()]


def find_cliques(graph, candidates, potential_clique=None, processed=None):
    candidates = set(candidates)
    potential_clique = potential_clique or set()
    processed = processed or set()
    if not candidates and not processed and len(potential_clique) > 2:
        yield potential_clique
    while candidates:
        c = candidates.pop()
        yield from find_cliques(graph, candidates.intersection(graph[c]), potential_clique.union([c]), processed.intersection(graph[c]))
        processed.add(c)


def get_networks(data):
    graph = defaultdict(set)
    for a, b in data:
        graph[a].add(b)
        graph[b].add(a)
    networks = list(find_cliques(graph, graph.keys()))
    return networks


def part1(data):
    networks = [sorted(n) for n in get_networks(data)]
    search_party = set()
    for n in networks:
        if len(n) > 3:
            search_party.update(map(tuple, map(sorted, itertools.combinations(n, 3))))
        else:
            search_party.add(tuple(n))
    result = [any(v.startswith('t') for v in n) for n in search_party]
    return sum(result)


def part2(data):
    networks = get_networks(data)
    max_value = max(networks, key=len)
    return ','.join(sorted(max_value))


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
