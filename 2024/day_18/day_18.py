# Day 18: RAM Run

from functools import partial
import heapq

import aoc
from aoc import CARDINALS, TILE


def get_data(source):
    data = aoc.get_data(src=source, day=18)
    obstacles = [list(map(int, line.split(','))) for line in data.splitlines()]
    dimensions = (71, 71) if source == aoc.SOURCE.INPUT else (7, 7)
    limit = 12 if source == aoc.SOURCE.EXAMPLE else 1024
    return dimensions, obstacles, limit


class Grid:
    grid: dict
    width: int
    height: int
    obstacles: list[tuple[int, int], tuple[int, int]]
    start: tuple[int, int]
    end: tuple[int, int]
    queue = []
    visited = dict()
    previous = dict()
    path: set

    def __init__(self, dimensions: tuple[int, int], obstacles, limit) -> None:
        self.width, self.height = dimensions
        self.obstacles = obstacles
        self.grid = {(y, x): TILE.EMPTY for x in range(self.width) for y in range(self.height)}
        self.set_start()
        self.set_end()
        self.add_obstacles(limit)

    def add_obstacles(self, limit):
        for i in range(min(limit, len(self.obstacles))):
            x, y = self.obstacles[i]
            self.grid[(y, x)] = TILE.WALL

    def set_start(self, start=None):
        self.start = (0, 0)

    def set_end(self, end=None):
        self.end = (self.width - 1, self.height - 1)

    def heuristic(self, a):
        # Manhattan distance on a square grid
        return abs(self.end[0] - a[0]) + abs(self.end[1] - a[1])

    def find_path(self):
        initial_state = (0, self.start)
        self.queue = [initial_state]
        self.visited[self.start] = 0

        while self.queue:
            score, cur_tile = heapq.heappop(self.queue)

            if cur_tile == self.end:
                break

            next_tiles = [(cur_tile[0] + d.value[0], cur_tile[1] + d.value[1]) for d in CARDINALS]
            for next_tile in next_tiles:
                if next_tile in self.grid and next_tile != cur_tile and self.grid[next_tile] != TILE.WALL:
                    new_cost = self.visited[cur_tile] + 10
                    if next_tile not in self.visited or new_cost < self.visited[next_tile]:
                        self.visited[next_tile] = new_cost
                        priority = new_cost + self.heuristic(next_tile)
                        heapq.heappush(self.queue, (priority, next_tile))
                        self.previous[next_tile] = cur_tile

        return self.trace_path()

    def trace_path(self):
        tile = [coords for coords in self.previous if coords == self.end][0]
        self.path = {tile}
        while tile != self.start:
            tile = self.previous[tile]
            self.path.add(tile)

        for el in self.path:
            self.grid[el] = 'O'

        return self.path


def part1(data):
    dimensions, obstacles, limit = data
    grid = Grid(dimensions=dimensions, obstacles=obstacles, limit=limit)
    grid.find_path()
    aoc.print_grid(grid.grid)
    return len(grid.path) - 1


def part2(data):
    return 0


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
