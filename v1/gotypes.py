import enum
from collections import namedtuple

# Representation of the two players of a go game (Black & White)
class Player(enum.Enum):
    black = 1
    white = 2

    @property
    def other(self):
        return Player.black if self == Player.white else Player.white

# Representation of the points on a go board (9x9)
# Named tuple for readability so that points can be accessed as point.row and point.col.
class Point(namedtuple('point', 'row col')):
    def neighbours(self):
        return [
            Point(self.row - 1, self.col),
            Point(self.row + 1, self.col), 
            Point(self.row, self.col - 1),
            Point(self.row, self.col + 1),
        ]
