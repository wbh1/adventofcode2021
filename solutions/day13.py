from solutions.Puzzle import Puzzle


class Day13(Puzzle):
    def __init__(self, filename):
        with open(f"inputs/{filename}.txt") as f:
            data = f.read().split("\n\n")
            self.points = {
                (int(x), int(y)) for x, y in [p.split(",") for p in data[0].split("\n")]
            }
            self.folds = [fold.split("fold along ")[1] for fold in data[1].split("\n")]

    def part1(self) -> int:
        fold1 = self.folds[0].split("=")
        if fold1[0] == "x":
            self._fold_vertical(int(fold1[1]))
        else:
            self._fold_horizontal(int(fold1[1]))

        return len(self.points)

    def part2(self) -> int:
        for fold in self.folds[1:]:
            fold = fold.split("=")
            if fold[0] == "x":
                self._fold_vertical(int(fold[1]))
            else:
                self._fold_horizontal(int(fold[1]))

        X_MAX, Y_MAX = (0, 0)
        for x, y in self.points:
            if x > X_MAX:
                X_MAX = x
            if y > Y_MAX:
                Y_MAX = y
        grid = [list([" "]) * (X_MAX + 1) for i in range(0, Y_MAX + 1)]
        for x, y in self.points:
            grid[y][x] = "▒"
        for row in grid:
            print("".join(row))
        return "^ ^ ^"

    def _fold_horizontal(self, y_div: int):
        new_set = self.points.copy()
        for x, y in self.points:
            if y > y_div:
                y_delta = y - y_div
                new_set.remove((x, y))
                new_set.add((x, y_div - y_delta))
        self.points = new_set

    def _fold_vertical(self, x_div: int):
        new_set = self.points.copy()
        for x, y in self.points:
            if x > x_div:
                x_delta = x - x_div
                new_set.remove((x, y))
                new_set.add((x_div - x_delta, y))
        self.points = new_set
