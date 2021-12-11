from solutions.Puzzle import Puzzle

# up, down, left, right, upright, downright, downleft, upleft
DR = [0, 0, -1, 1, 1, -1, -1, 1]

DC = [1, -1, 0, 0, 1, 1, -1, -1]


class Day11(Puzzle):
    def __init__(self, filename):
        with open(f"inputs/{filename}.txt") as f:
            self.grid = [[int(i) for i in row] for row in f.read().splitlines()]
        self.FLASHED = set()

    def part1(self) -> int:
        flashes = 0

        for round in range(0, 100):
            CONTINUE_ROUND = True
            self.FLASHED = set()
            for ri in range(0, len(self.grid)):
                for ci, octo in enumerate(self.grid[ri]):
                    self.grid[ri][ci] += 1
            while CONTINUE_ROUND:
                _flashes = self.flash()
                flashes += _flashes
                if _flashes == 0:
                    CONTINUE_ROUND = False
            for ri, ci in self.FLASHED:
                self.grid[ri][ci] = 0
        return flashes

    def part2(self) -> int:
        # we already did 100 rounds
        rounds = 100
        CONTINUE = True
        total_octopusses = len(self.grid) * len(self.grid[0])
        while CONTINUE:
            rounds += 1
            CONTINUE_ROUND = True
            self.FLASHED = set()
            for ri in range(0, len(self.grid)):
                for ci, octo in enumerate(self.grid[ri]):
                    self.grid[ri][ci] += 1

            while CONTINUE_ROUND:
                if not self.flash():
                    CONTINUE_ROUND = False
            for ri, ci in self.FLASHED:
                self.grid[ri][ci] = 0
            if len(self.FLASHED) == total_octopusses:
                CONTINUE = False

        return rounds

    def flash(self):
        flashes = 0
        for ri in range(0, len(self.grid)):
            for ci, octo in enumerate(self.grid[ri]):
                if octo > 9 and (ri, ci) not in self.FLASHED:
                    flashes += 1
                    self.FLASHED.add((ri, ci))
                    for i in range(8):
                        rr = ri + DR[i]
                        cc = ci + DC[i]
                        if 0 <= rr < len(self.grid) and 0 <= cc < len(self.grid[0]):
                            self.grid[rr][cc] += 1
        return flashes
