from solutions.Puzzle import Puzzle
from collections import Counter


class Day6(Puzzle):
    def __init__(self, filename):
        with open(f"inputs/{filename}.txt") as f:
            data = f.read().strip()
            self.fishes = Counter([int(fish) for fish in data.split(",")])

    def part1(self) -> int:
        return self.simulate_growth(80)

    def part2(self) -> int:
        return self.simulate_growth(256)

    def simulate_growth(self, rounds):
        fishes = self.fishes.copy()

        for n in range(0, rounds):
            new_fishes = Counter()
            for key, value in fishes.items():
                if key == 0:
                    # Fish at 0 reset to 6; newly spawned start at 8
                    new_fishes.update({6: value, 8: value})
                else:
                    k = key - 1
                    new_fishes.update({k: value})

            fishes = new_fishes.copy()

        return sum(fishes.values())
