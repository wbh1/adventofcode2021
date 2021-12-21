from solutions.Puzzle import Puzzle
import math
import json


class Day18(Puzzle):
    def __init__(self, filename):
        with open(f"inputs/{filename}.txt") as f:
            self.data = f.read().splitlines()
        self.value = self.data[0]

    def part1(self) -> int:
        for i in range(1, len(self.data), 1):
            self.value = "[" + self.value + "," + self.data[i] + "]"
            self.reduce()
        score = magnitude(json.loads(self.value))
        return score

    def reduce(self):
        new = boom(self.value)
        if new != self.value:
            self.value = new
            return self.reduce()

        new = split(new)
        if new != self.value:
            self.value = new
            return self.reduce()

    def part2(self) -> int:
        max_score = 0
        for x in self.data:
            for y in self.data:
                if x != y:
                    self.value = "[" + x + "," + y + "]"
                    self.reduce()
                    m = magnitude(json.loads(self.value))
                    if m > max_score:
                        max_score = m
        return max_score


def split(nums):
    parts = partify(nums)
    for i, p in enumerate(parts):
        if isinstance(p, int):
            if p >= 10:
                parts[i] = [math.floor(int(p) / 2.0), math.ceil(int(p) / 2.0)]
                return "".join([str(x) for x in parts])
    return nums


def magnitude(nums):
    # pop, pop!
    if isinstance(nums, list):
        return 3 * magnitude(nums[0]) + 2 * magnitude(nums[1])
    else:
        return nums


def partify(nums):
    parts = []
    i = 0

    while i < len(nums):
        if nums[i] in ["[", "]", ","]:
            parts.append(nums[i])
            i += 1
        # needed due to output of split()
        elif nums[i] == " ":
            # print("SPACE")
            i += 1
        else:
            assert nums[i].isdigit()
            num_end = i
            while num_end < len(nums) and nums[num_end].isdigit():
                num_end += 1
            parts.append(int(nums[i:num_end]))
            i = num_end
    return parts


def boom(nums: str):

    parts = partify(nums)

    depth = 0
    for i, char in enumerate(parts):
        if char == "]":
            depth -= 1
        if char == "[":
            depth += 1
            if depth == 5:
                pairLeft = parts[i + 1]
                # print(parts[i + 1 :])

                assert isinstance(pairLeft, int)

                assert parts[i + 2] == ","

                pairRight = parts[i + 3]
                assert isinstance(pairRight, int)

                left_index = None
                right_index = None

                for j in range(len(parts)):
                    if isinstance(parts[j], int):
                        if j < i:
                            left_index = j
                        elif j > i + 3 and right_index is None:
                            right_index = j
                if right_index:
                    parts[right_index] += pairRight
                if left_index:
                    parts[left_index] += pairLeft

                parts = parts[:i] + [0] + parts[i + 5 :]

                return "".join([str(x) for x in parts])
    return nums
