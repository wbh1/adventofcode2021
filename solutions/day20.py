from collections import defaultdict

import numpy
from scipy.ndimage import convolve

from solutions.Puzzle import Puzzle


# This is similar to day 17 of 2020, which I used convolution for
# I still don't fully understand how it works, but it do.
class Day20(Puzzle):
    def __init__(self, filename):
        self.grid = defaultdict(lambda: ".")
        with open(f"inputs/{filename}.txt") as f:
            data = f.read().split("\n\n")
            self.algo = numpy.array([int(p == "#") for p in data[0].strip()])
            image = data[1].splitlines()
            self.image = numpy.pad(
                [[int(p == "#") for p in row] for row in image],
                (50, 50),
            )

    def part1(self) -> int:
        # Array with decimal values corresponding
        # to binary value of a "1" in each position
        binary_weights = 2 ** numpy.arange(9).reshape(3, 3)

        for i in range(2):
            self.image = self.algo[convolve(self.image, binary_weights)]
        return self.image.sum()

    def part2(self) -> int:
        binary_weights = 2 ** numpy.arange(9).reshape(3, 3)

        for i in range(48):
            self.image = self.algo[convolve(self.image, binary_weights)]
        return self.image.sum()
