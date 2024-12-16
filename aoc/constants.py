from enum import Enum


class SOURCE(Enum):
    EXAMPLE = 1
    INPUT = 2


class COMPASS(Enum):
    NORTH = (-1, 0)
    NORTH_EAST = (-1, 1)
    EAST = (0, 1)
    SOUTH = (1, 0)
    SOUTH_EAST = (1, 1)
    SOUTH_WEST = (1, -1)
    WEST = (0, -1)
    NORTH_WEST = (-1, -1)


CARDINALS = [COMPASS.NORTH, COMPASS.EAST, COMPASS.SOUTH, COMPASS.WEST]


class ARROW(Enum):
    UP = '^'
    DOWN = 'v'
    LEFT = '<'
    RIGHT = '>'


DIRECTIONS = {
    ARROW.UP: COMPASS.NORTH,
    ARROW.RIGHT: COMPASS.EAST,
    ARROW.DOWN: COMPASS.SOUTH,
    ARROW.LEFT: COMPASS.WEST
}
