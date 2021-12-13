from collections import defaultdict
from solutions.Puzzle import Puzzle


class Day12(Puzzle):
    def __init__(self, filename):
        with open(f"inputs/{filename}.txt") as f:
            data = [
                (a, b) for a, b in [line.split("-") for line in f.read().splitlines()]
            ]
            self.connections = defaultdict(list)
            self.paths = []
            for pointA, pointB in data:
                self.connections[pointA].append(pointB)
                self.connections[pointB].append(pointA)

    def part1(self) -> int:
        return self.traverse("start")

    def part2(self) -> int:
        return self.traverse("start", visit_twice=True)

    def traverse(self, point: str, seen=set(), visit_twice=False):
        if point == "end":
            return 1
        if point in seen:
            if point == "start":
                return 0
            if point.islower():
                if not visit_twice:
                    return 0
                else:
                    # We've already seen this point once before,
                    # so after seeing it again, we need to stop visiting
                    # other lowercase points twice
                    visit_twice = False

        # `seen | {point}` is the same as `seen.union({point})`. Thanks Reddit.
        # https://www.reddit.com/r/adventofcode/comments/rehj2r/2021_day_12_solutions/ho7pawv/
        return sum(
            self.traverse(n, seen | {point}, visit_twice=visit_twice)
            for n in self.connections[point]
        )
