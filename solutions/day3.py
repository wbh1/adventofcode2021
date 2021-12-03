from collections import Counter

from solutions.Puzzle import Puzzle


class Day3(Puzzle):
    def __init__(self, filename):
        with open(f"inputs/{filename}.txt") as f:
            self.data = f.read().splitlines()

    def part1(self) -> int:
        positions = []

        # Create a list of Counters corresponding to the frequency of
        # each number in each position
        for i in range(0, len(self.data[0])):
            positions.append(Counter([n[i] for n in self.data]))

        gamma = "".join([p.most_common(1)[0][0] for p in positions])
        episilon = "".join([p.most_common()[-1][0] for p in positions])

        return int(gamma, 2) * int(episilon, 2)

    def part2(self) -> int:
        oxygen = reduce(self.data.copy())
        co2 = reduce(self.data, gas="CO2")

        return int(oxygen, 2) * int(co2, 2)


def reduce(dataset, gas="O2"):
    for pos in range(0, len(dataset[0])):
        mc = Counter(n[pos] for n in dataset).most_common(2)

        if len(mc) == 2 and mc[0][1] == mc[1][1]:
            keep = "1" if gas == "O2" else "0"
        else:
            keep = mc[0][0] if gas == "O2" else mc[-1][0]

        dataset = [n for n in dataset if n[pos] == keep]

    if len(dataset) > 1:
        raise Exception("Didn't reduce properly!")

    return dataset[0]
