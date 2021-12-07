from solutions.Puzzle import Puzzle
import statistics
import math


class Day7(Puzzle):
    def __init__(self, filename):
        with open(f"inputs/{filename}.txt") as f:
            self.crabs = [int(c) for c in f.read().strip().split(",")]

    def part1(self) -> int:
        med = statistics.median(self.crabs)
        fuel = 0
        for c in self.crabs:
            fuel += abs(c - med)
        return int(fuel)

    def part2(self) -> int:
        def calc_dist(crab, mean):
            moves = abs(crab - mean)
            # https://en.wikipedia.org/wiki/Triangular_number
            return ((moves ** 2) + moves) // 2

        # The answer should be within 1 int of the mean of the dataset
        # so we need to the check the floor and ceil of the mean to cover our bases.
        # I brute forced this when solving, but this solution should work
        # for any of the puzzle inputs.
        # https://www.reddit.com/r/adventofcode/comments/rars4g/2021_day_7_why_do_these_values_work_spoilers/hnkcyei/

        mean = statistics.mean(self.crabs)
        meanFloor, meanCeil = (math.floor(mean), math.ceil(mean))
        fuelFloor = fuelCeil = 0
        for c in self.crabs:
            fuelFloor += calc_dist(c, meanFloor)
            fuelCeil += calc_dist(c, meanCeil)

        return min(fuelFloor, fuelCeil)
