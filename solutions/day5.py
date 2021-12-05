from solutions.Puzzle import Puzzle
import re
from itertools import repeat


class Day5(Puzzle):
    def __init__(self, filename):
        self.coords = []
        self.grid = []
        data = None
        matcher = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")
        with open(f"inputs/{filename}.txt") as f:
            data = f.read()

        for m in matcher.finditer(data):
            self.coords.append(
                (
                    (
                        (int(m.group(1)), int(m.group(2))),
                        (int(m.group(3)), int(m.group(4))),
                    )
                )
            )

        for i in range(0, 1001):
            self.grid.append(list(repeat(0, 1000)))

    def part1(self) -> int:
        grid = self.grid
        for coord in self.coords:
            start, end = coord
            x1, y1 = (start[0], start[1])
            x2, y2 = (end[0], end[1])

            if x1 != x2 and y1 != y2:
                continue

            if x1 == x2:
                for point in range(min(y1, y2), max(y1, y2) + 1):
                    if grid[point][x1]:
                        grid[point][x1] += 1
                    else:
                        grid[point][x1] = 1

            elif y1 == y2:
                for point in range(min(x1, x2), max(x1, x2) + 1):
                    if grid[y1][point]:
                        grid[y1][point] += 1

                    else:
                        grid[y1][point] = 1

        res = 0
        for row in grid:
            for c in row:
                if c > 1:
                    res += 1

        self.grid = grid

        return res

    def part2(self) -> int:
        grid = self.grid
        for coord in self.coords:
            start, end = coord
            if start[0] > end[0]:
                start, end = coord[1], coord[0]

            x1, y1 = (start[0], start[1])
            x2, y2 = (end[0], end[1])

            if x1 != x2 and y1 != y2:
                y = y1
                slope = int((y2 - y1) / (x2 - x1))
                for x in range(x1, x2 + 1):
                    grid[y][x] += 1
                    y += slope

        res = 0
        for row in grid:
            for c in row:
                if c > 1:
                    res += 1

        return res
