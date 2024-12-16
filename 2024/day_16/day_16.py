# Day 16: Reindeer Maze

from functools import partial
import heapq

import aoc
from aoc import COMPASS, CARDINALS, DIRECTIONS


def get_data(source):
    data = aoc.get_data(src=source, day=16, offset=0)
    return data


class TILE:
    START = 'S'
    END = 'E'
    WALL = '#'
    EMPTY = '.'


def part1(data):
    maze = aoc.init_grid(data)
    start = list(filter(lambda v: maze[v] == TILE.START, maze))[0]
    end = list(filter(lambda v: maze[v] == TILE.END, maze))[0]

    start_tile = (start, COMPASS.EAST.value)
    initial_state = (0, start_tile, None)
    queue = [initial_state]
    visited = {
        start: 0
    }
    prev = {
        start_tile: []
    }
    best_score = 500_000

    while queue:
        score, cur_tile, prev_tile = heapq.heappop(queue)
        coords, direction = cur_tile

        if cur_tile in visited and visited[cur_tile] < score:
            if cur_tile in prev:
                prev[cur_tile].append(prev_tile)
            continue
        visited[cur_tile] = score
        if cur_tile not in prev:
            prev[cur_tile] = [prev_tile]

        if coords == end:
            best_score = min(best_score, score)
            break

        y, x = coords
        cardinal = COMPASS(direction)
        dir_index = CARDINALS.index(cardinal)
        directions = [cardinal, CARDINALS[dir_index - 1], CARDINALS[(dir_index + 1) % len(CARDINALS)]]
        next_tiles = [((y + d.value[0], x + d.value[1]), d.value) for d in directions]

        for c, d in next_tiles:
            if maze[c] != TILE.WALL:
                new_score = score + (1 if d == direction else 1001)
                heapq.heappush(queue, (new_score, (c, d), cur_tile))

    tile = [(c,d) for c, d in prev if c == coords][0]
    while tile != start_tile:
        tile = prev[tile][0]
        coords, direction = tile
        maze[coords] = [k.value for k, v in DIRECTIONS.items() if v == COMPASS(direction)][0]

    aoc.print_grid(maze)
    return best_score


def part2(data):
    return 0


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
