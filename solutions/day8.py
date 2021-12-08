from solutions.Puzzle import Puzzle
from string import ascii_lowercase
from collections import Counter


class Day8(Puzzle):
    """Number mappings
    1 is the only # that uses 2 segments
    4 is the only # that 4 segments
    7 is the only # that 3 segments
    8 is the only # that 7 segments
    """

    possible_mappings = {2: [1], 4: [4], 3: [7], 7: [8], 5: [2, 3, 5], 6: [0, 6, 9]}
    desired_mappings = {
        "bc": 1,
        "abdeg": 2,
        "abcdg": 3,
        "bcfg": 4,
        "acdfg": 5,
        "acdefg": 6,
        "abc": 7,
        "abcdefg": 8,
        "abcdfg": 9,
        "abcdef": 0,
    }

    desired_mappings = {"".join(sorted(k)): v for k, v in desired_mappings.items()}

    # how many times a given segment is used across all possible numbers
    occurrences = Counter("".join(desired_mappings.keys()))

    def __init__(self, filename):
        self.data = {}
        self.mappings = {ltr: set([ltr]) for ltr in ascii_lowercase[:7]}

        with open(f"inputs/{filename}.txt") as f:
            lines = f.read().splitlines()
            for line in lines:
                patterns, output = line.split(" | ")
                patterns = [p for p in patterns.split(" ")]
                self.data[output] = patterns

    def part1(self) -> int:
        freq = 0
        for output in self.data.keys():
            vals = output.split(" ")
            for v in vals:
                if len(self.possible_mappings[len(v)]) == 1:
                    freq += 1
        return freq

    def part2(self) -> int:
        total = 0
        for output, input in self.data.items():
            mask = self.get_mask(input)
            total += self.get_value(output, mask)
        return total

    def get_value(self, output, mask):
        values = []
        output = output.split(" ")
        for signal in output:
            converted = ""
            for ltr in signal:
                converted += mask[ltr]
            values.append(str(self.desired_mappings["".join(sorted(converted))]))
        return int("".join(values))

    def get_mask(self, line):
        num_mapping = {k: "" for k in range(10)}
        letter_mapping = {k: "" for k in ascii_lowercase[:7]}
        line = ["".join(sorted(s)) for s in line]

        # Initial population of mapping with signals that only have 1 possible mapping
        for signals in line:
            if len(self.possible_mappings[len(signals)]) == 1:
                num_mapping[self.possible_mappings[len(signals)][0]] = signals

        # the mapping for "a" will be whatever digit is in 7 but not in 1
        a = [ltr for ltr in num_mapping[7] if ltr not in num_mapping[1]][0]
        letter_mapping[a] = "a"

        # additional mappings where there's only 1 possible mapping
        occurrences = Counter("".join(line))
        # TODO: Make cnt comparison not hardcoded
        for ltr, cnt in occurrences.items():
            if cnt == 9:
                letter_mapping[ltr] = "c"
            # 'a' is already found, so the unmapped letter that occurs
            # 8 times must be 'b'
            elif cnt == 8 and letter_mapping[ltr] == "":
                letter_mapping[ltr] = "b"
            elif cnt == 6:
                letter_mapping[ltr] = "f"
            elif cnt == 4:
                letter_mapping[ltr] = "e"

        # 'g' is the only letter that doesn't yet have a mapping
        # in the 4 letter signal
        for signals in line:
            if len(signals) == 4:
                for ltr in signals:
                    # if the letter's already mapped, it's not gonna be 'g'
                    if letter_mapping[ltr] != "":
                        continue
                    else:
                        letter_mapping[ltr] = "g"
                        break

        # the last remaining unmapped letter is d, so map it to whatever
        # is not mapped yet
        for k, v in letter_mapping.items():
            if v == "":
                letter_mapping[k] = "d"

        return letter_mapping
