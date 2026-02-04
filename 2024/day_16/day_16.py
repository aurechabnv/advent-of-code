# Day 16: Reindeer Maze

import heapq
from functools import partial

import aoc
from aoc import COMPASS, CARDINALS, TILE


def get_data(source, offset=0):
    data = aoc.get_data(src=source, year=2024, day=16, offset=offset)
    return data


class Maze:
    def __init__(self, data) -> None:
        self.grid = aoc.init_grid(data)
        self.start = list(filter(lambda v: self.grid[v] == TILE.START, self.grid))[0]
        self.end = list(filter(lambda v: self.grid[v] == TILE.END, self.grid))[0]
        self.queue = []
        self.visited = dict()
        self.prev = dict()
        self.path = set()
        self.best_score = None
        self.paths = []

    def _prepare_search(self, draw):
        if draw:
            for key, value in self.grid.items():
                if value == TILE.PATH:
                    self.grid[key] = TILE.EMPTY
        self.path = set()
        self.paths = []
        self.visited = dict()

        start_tile = (self.start, COMPASS.EAST.value)
        self.queue = [(0, start_tile, [start_tile])]
        self.visited[start_tile] = 0

    def find_path(self, draw=False, find_all=False):
        self._prepare_search(draw)
        found_path = False

        while self.queue:
            score, cur_tile, cur_path = heapq.heappop(self.queue)
            cur_coords, cur_direction = cur_tile

            if cur_coords == self.end:
                if not found_path:
                    self.best_score = score
                if score == self.best_score:
                    self.paths.append(cur_path)
                found_path = True
                if find_all:
                    continue
                break

            if cur_tile in self.visited and self.visited[cur_tile] < score:
                continue

            self.visited[cur_tile] = score

            d_index = CARDINALS.index(COMPASS(cur_direction))
            directions = [CARDINALS[d_index], CARDINALS[d_index - 1], CARDINALS[(d_index + 1) % len(CARDINALS)]]
            next_tiles = [((cur_coords[0] + d.value[0], cur_coords[1] + d.value[1]), d.value) for d in directions]

            for next_tile in next_tiles:
                coords, direction = next_tile
                if self.grid[coords] != TILE.WALL:
                    new_cost = self.visited[cur_tile] + (1 if direction == cur_direction else 1001)
                    new_path = cur_path[:]
                    new_path.append(next_tile)
                    heapq.heappush(self.queue, (new_cost, next_tile, new_path))

        if found_path:
            self._trace_path(draw)

        return found_path

    def _trace_path(self, draw):
        for path in self.paths:
            self.path.update([coords for coords, direction in path])

        if draw:
            for coords in self.path:
                self.grid[coords] = TILE.PATH
            aoc.print_grid(self.grid)

        return self.path


def part1(data):
    maze = Maze(data)
    maze.find_path()
    return maze.best_score


def part2(data):
    maze = Maze(data)
    maze.find_path(find_all=True)
    return len(maze.path)


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
