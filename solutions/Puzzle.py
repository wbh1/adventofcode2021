class Puzzle:
    def __init__(self, filename):
        with open(f"inputs/{filename}.txt") as f:
            self.data = [int(i) for i in f.read().splitlines()]

    def part1(self) -> int:
        pass

    def part2(self) -> int:
        pass

    def solve(self):
        print("Part 1:", self.part1())
        print("Part 2:", self.part2())
