# Day 18: RAM Run

from functools import partial
import heapq

import aoc
from aoc import CARDINALS, TILE


def get_data(source):
    data = aoc.get_data(src=source, day=18)
    obstacles = [tuple(map(int, line.split(','))) for line in data.splitlines()]
    dimensions = (71, 71) if source == aoc.SOURCE.INPUT else (7, 7)
    limit = 1024 if source == aoc.SOURCE.INPUT else 12
    return dimensions, obstacles, limit


class Grid:
    def __init__(self, dimensions: tuple[int, int], obstacles: list[tuple], limit: int) -> None:
        self.width, self.height = dimensions
        self.obstacles = obstacles
        self.grid = {(y, x): TILE.EMPTY for x in range(self.width) for y in range(self.height)}
        self.start = (0, 0)
        self.end = (self.width - 1, self.height - 1)
        self.queue = []
        self.visited = dict()
        self.previous = dict()
        self.path = set()
        self.last_obstacle_index = 0
        self._add_obstacles(limit)

    def _add_obstacles(self, limit):
        for i in range(min(limit, len(self.obstacles))):
            self._add_obstacle(i)

    def _add_obstacle(self, index):
        x, y = self.obstacles[index]
        if (coords := (y, x)) in self.grid:
            self.grid[coords] = TILE.WALL
            self.last_obstacle_index = index

    def add_next_obstacle(self):
        self._add_obstacle(self.last_obstacle_index + 1)
        return self.obstacles[self.last_obstacle_index]

    def find_path(self, draw=False):
        self._prepare_search(draw)
        found_path = False

        while self.queue:
            score, cur_tile = heapq.heappop(self.queue)

            if cur_tile == self.end:
                found_path = True
                break

            next_tiles = [(cur_tile[0] + d.value[0], cur_tile[1] + d.value[1]) for d in CARDINALS]
            for next_tile in next_tiles:
                if next_tile in self.grid and next_tile != cur_tile and self.grid[next_tile] != TILE.WALL:
                    new_cost = self.visited[cur_tile] + 1
                    if next_tile not in self.visited or new_cost < self.visited[next_tile]:
                        self.visited[next_tile] = new_cost
                        priority = new_cost + self._heuristic(next_tile)
                        heapq.heappush(self.queue, (priority, next_tile))
                        self.previous[next_tile] = cur_tile

        if found_path:
            self._trace_path(draw)

        return found_path

    def _heuristic(self, coords):
        # Manhattan distance on a square grid
        return abs(self.end[0] - coords[0]) + abs(self.end[1] - coords[1])

    def _prepare_search(self, draw):
        if draw:
            for key, value in self.grid.items():
                if value == TILE.PATH:
                    self.grid[key] = TILE.EMPTY
        self.path = set()
        self.previous, self.visited = dict(), dict()
        self.queue = [(0, self.start)]
        self.visited[self.start] = 0

    def _trace_path(self, draw):
        tile = [coords for coords in self.previous if coords == self.end][0]
        self.path = {tile}
        while tile != self.start:
            tile = self.previous[tile]
            self.path.add(tile)

        if draw:
            for el in self.path:
                self.grid[el] = TILE.PATH
            aoc.print_grid(self.grid)

        return self.path


def part1(data):
    grid = Grid(*data)
    grid.find_path()
    return len(grid.path) - 1


def part2(data):
    grid = Grid(*data)
    found = grid.find_path()
    while found:
        x, y = grid.add_next_obstacle()
        if (y, x) in grid.path:
            found = grid.find_path()
    x, y = grid.obstacles[grid.last_obstacle_index]
    return f'{x},{y}'


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
