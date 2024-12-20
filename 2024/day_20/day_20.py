# Day 20: Race Condition

from functools import partial

import aoc
from aoc import TILE, CARDINALS


def get_data(source):
    data = aoc.get_data(src=source, day=20)
    return data.replace('<em>', '').replace('</em>', '')


class RaceTrack:
    def __init__(self, data) -> None:
        self.grid = aoc.init_grid(data)
        self.start = [coords for coords, value in self.grid.items() if value == TILE.START][0]
        self.end = [coords for coords, value in self.grid.items() if value == TILE.END][0]
        self.queue = []
        self.previous = dict()
        self.path = []
        self.cheats = dict()

    def find_cheats(self, draw=False):
        for start_cheat in self.path:
            sides = [((start_cheat[0] + d.value[0], start_cheat[1] + d.value[1]), d.value) for d in CARDINALS]
            for side in sides:
                possible_wall, direction = side
                if self.grid[possible_wall] == TILE.WALL:
                    end_cheat = (possible_wall[0] + direction[0], possible_wall[1] + direction[1])
                    if end_cheat in self.grid and self.grid[end_cheat] != TILE.WALL and possible_wall not in self.cheats:
                        excluded_path = self.path[self.path.index(start_cheat):self.path.index(end_cheat)]
                        self.cheats[possible_wall] = len(excluded_path) - 2

    def find_path(self, draw=False, cheating=False):
        self._prepare_search(draw)

        while self.queue:
            cur_tile = self.queue.pop(0)

            if cur_tile == self.end:
                break

            next_tiles = [(cur_tile[0] + d.value[0], cur_tile[1] + d.value[1]) for d in CARDINALS]
            for next_tile in next_tiles:
                if self.grid[next_tile] != TILE.WALL and next_tile not in self.previous:
                    self.queue.append(next_tile)
                    self.previous[next_tile] = cur_tile

        path = self._trace_path(draw)
        if not cheating:
            self.path = path

        return path

    def _prepare_search(self, draw):
        if draw:
            for key, value in self.grid.items():
                if value == TILE.PATH:
                    self.grid[key] = TILE.EMPTY
        self.path = []
        self.previous = dict()
        self.queue = [self.start]
        self.previous[self.start] = None

    def _trace_path(self, draw):
        tile = self.end
        path = []
        while tile != self.start:
            path.append(tile)
            tile = self.previous[tile]
        path.append(self.start)

        if draw:
            for el in path:
                self.grid[el] = TILE.PATH
            aoc.print_grid(self.grid)

        return path


def part1(data):
    race_track = RaceTrack(data)
    race_track.find_path()
    race_track.find_cheats()
    return len([value for value in race_track.cheats.values() if value >= 100])


def part2(data):
    return 0


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
