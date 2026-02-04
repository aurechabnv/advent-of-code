# Day 20: Race Condition

from functools import partial

import aoc
from aoc import TILE, CARDINALS


def get_data(source):
    data = aoc.get_data(src=source, year=2024, day=20)
    threshold = 100 if source == aoc.SOURCE.INPUT else 50
    return threshold, data.replace('<em>', '').replace('</em>', '')


class RaceTrack:
    def __init__(self, data) -> None:
        self.grid = aoc.init_grid(data)
        self.start = [coords for coords, value in self.grid.items() if value == TILE.START][0]
        self.end = [coords for coords, value in self.grid.items() if value == TILE.END][0]
        self.queue = []
        self.previous = dict()
        self.path = []
        self.cheats = dict()

    def find_cheats(self, max_cheat_time, threshold):
        self.find_path()
        for start_index, cheat_start in enumerate(self.path):
            for end_index, cheat_end in enumerate(self.path):
                distance = abs(cheat_end[0] - cheat_start[0]) + abs(cheat_end[1] - cheat_start[1])
                saved_picoseconds = end_index - start_index - distance
                if saved_picoseconds >= threshold and distance <= max_cheat_time and (cheat_start, cheat_end) not in self.cheats:
                    self.cheats[(cheat_start, cheat_end)] = saved_picoseconds

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
        path.reverse()

        if draw:
            for el in path:
                self.grid[el] = TILE.PATH
            aoc.print_grid(self.grid)

        return path


def get_number_of_cheats(data, picoseconds):
    threshold, data = data
    race_track = RaceTrack(data)
    race_track.find_cheats(picoseconds, threshold)
    return len(race_track.cheats)


def part1(data):
    return get_number_of_cheats(data, picoseconds=2)


def part2(data):
    return get_number_of_cheats(data, picoseconds=20)


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.INPUT)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
