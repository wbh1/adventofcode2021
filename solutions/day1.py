from solutions.Puzzle import Puzzle


class Day1(Puzzle):
    def part1(self) -> int:
        increases = 0

        for n in range(1, len(self.data)):
            if self.data[n] > self.data[n - 1]:
                increases += 1

        return increases

    def part2(self) -> int:
        # 171 + 154 + 155 + 170
        # 171 + 154 + 155 < 154 + 155 + 170
        # False, because a (171) is greater than d (170)
        # Only need to compare the number being swapped from the sliding scale
        return sum(y > x for x, y in zip(self.data, self.data[3:]))
