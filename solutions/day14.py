from solutions.Puzzle import Puzzle
from collections import Counter


class Day14(Puzzle):
    def __init__(self, filename):
        with open(f"inputs/{filename}.txt") as f:
            data = f.read().split("\n\n")
            self.inital_polymer = data[0]
            self.rules = {
                rule.split(" -> ")[0]: rule.split(" -> ")[1]
                for rule in data[1].splitlines()
            }

    def part1(self) -> int:
        # Initialize a counter of the number of elements (for the answer)
        # and a counter of the number of pairs (for the iterating)
        self.elements = Counter(self.inital_polymer)
        self.pairs = Counter(
            [
                self.inital_polymer[i : i + 2]
                for i in range(len(self.inital_polymer) - 1)
            ]
        )
        for i in range(0, 10):
            self.pairs = self.grow(self.pairs)
        c = self.elements.most_common()
        return c[0][1] - c[-1][1]

    def part2(self) -> int:
        for i in range(0, 30):
            self.pairs = self.grow(self.pairs)
        c = self.elements.most_common()
        return c[0][1] - c[-1][1]

    def grow(self, pairs: Counter):
        new_pairs = Counter()
        for pair, freq in pairs.items():
            # distinguish btwn each letter of the pair
            pairA, pairB = pair

            # find which letter gets inserted between the pair
            insertion = self.rules[pair]

            # new pairs are present as a result of the insertion
            # (and the old pair is no longer there)
            new_pairs[pairA + insertion] += freq
            new_pairs[insertion + pairB] += freq

            # don't forget to increment the frequency of this element's appearance
            self.elements[insertion] += freq
        return new_pairs
