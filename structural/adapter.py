import math


class RoundHole:

    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def fits(self, peg):
        return self.get_radius() >= peg.get_radius()


class RoundPeg:

    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius


class SquarePeg:

    def __init__(self, width):
        self.width = width

    def get_width(self):
        return self.width


class SquareAdapter(RoundPeg):
    def __init__(self, peg):
        super(RoundPeg, self).__init__()
        self.peg = peg

    def get_radius(self):
        return self.peg.get_width() * math.sqrt(2)/2

if __name__ == '__main__':
    round_peg = RoundPeg(5)
    round_hole = RoundHole(4)
    print(round_hole.fits(round_peg))
    square_peg = SquarePeg(3)
    # round_hole.fits(square_peg)  Mistake
    adapter = SquareAdapter(square_peg)
    print(round_hole.fits(adapter))  # Work
