from solutions.Puzzle import Puzzle


class Day2(Puzzle):
    def __init__(self, filename):
        with open(f"inputs/{filename}.txt") as f:
            self.data = [
                (dir, int(distance))
                for dir, distance in (
                    tuple(i.split(" ")) for i in f.read().splitlines()
                )
            ]

        self.location = {"x": 0, "y": 0, "aim": 0}

    def part1(self) -> int:
        loc = self.location

        for dir, distance in self.data:
            if dir == "down":
                loc["y"] += distance
            elif dir == "forward":
                loc["x"] += distance
            elif dir == "up":
                loc["y"] -= distance
            else:
                print(f"Unknown direction {dir}")

        # Puzzle expects depth (y) to be positive
        return loc["x"] * loc["y"]

    def part2(self) -> int:
        loc = self.location
        loc = {"x": 0, "y": 0, "aim": 0}

        for dir, distance in self.data:
            if dir == "down":
                loc["aim"] += distance
            elif dir == "up":
                loc["aim"] -= distance
            elif dir == "forward":
                loc["x"] += distance
                loc["y"] += distance * loc["aim"]
            else:
                print(f"Unknown direction {dir}")

        return loc["x"] * loc["y"]
