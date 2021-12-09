from collections import deque
from solutions.Puzzle import Puzzle


class Day9(Puzzle):
    def __init__(self, filename):
        self.data = []
        self.DR = [0, 0, -1, 1]
        self.DC = [-1, 1, 0, 0]
        with open(f"inputs/{filename}.txt") as f:
            data = f.read().splitlines()
            self.data = [[int(x) for x in line] for line in data]

    def part1(self) -> int:
        low_points = []
        for ri in range(len(self.data)):
            for i, value in enumerate(self.data[ri]):
                passing = True
                for x in range(4):
                    nr = ri + self.DR[x]
                    nc = i + self.DC[x]
                    # If a neighbor is less than the value,
                    # then the value isn't a low point.
                    # Also, check that the neighbor is a valid coordinate
                    if (
                        0 <= nr < len(self.data)
                        and 0 <= nc < len(self.data[0])
                        and self.data[nr][nc] <= value
                    ):
                        passing = False
                if passing:
                    low_points.append((i, ri))
        self.low_points = low_points
        return sum([self.data[y][x] for x, y in low_points]) + len(low_points)

    def part2(self) -> int:
        rowLength = len(self.data)
        colLength = len(self.data[0])
        BASINS = []
        SEENT = set()

        # BFS (Breadth First Search) - https://www.youtube.com/watch?v=oDqjPvD54Ss
        for row in range(len(self.data)):
            for col in range(len(self.data[row])):
                if (row, col) not in SEENT and self.data[row][col] != 9:
                    basin_size = 0
                    q = deque()
                    q.append((row, col))
                    while q:
                        (r, c) = q.popleft()

                        if (r, c) in SEENT:
                            continue

                        SEENT.add((r, c))
                        basin_size += 1
                        for i in range(4):
                            nr = r + self.DR[i]
                            nc = c + self.DC[i]
                            if (
                                0 <= nr < rowLength
                                and 0 <= nc < colLength
                                and self.data[nr][nc] != 9
                            ):
                                q.append((nr, nc))
                    BASINS.append(basin_size)

        BASINS = sorted(BASINS)
        return BASINS[-3] * BASINS[-2] * BASINS[-1]
