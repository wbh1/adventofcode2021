from solutions.Puzzle import Puzzle


class Day10(Puzzle):
    ERROR_SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}
    AUTOCOMPLETE_SCORES = {")": 1, "]": 2, "}": 3, ">": 4}
    MATCHES = {"{": "}", "(": ")", "[": "]", "<": ">"}

    def __init__(self, filename):
        with open(f"inputs/{filename}.txt") as f:
            self.data = f.read().splitlines()
        self.incomplete_lines = []

    def part1(self) -> int:
        incomplete_lines = []
        syntaxerrors = []
        q = []
        for line in self.data:
            OK = True
            for punc in line:
                if punc in "([{<":
                    q.append(punc)
                else:
                    prev = q.pop()
                    if punc != self.MATCHES[prev]:
                        syntaxerrors.append(punc)
                        OK = False
            if OK:
                incomplete_lines.append(line)

        self.incomplete_lines = incomplete_lines
        res = 0
        for e in syntaxerrors:
            res += self.ERROR_SCORES[e]
        return res

    def part2(self) -> int:
        scores = []
        for line in self.incomplete_lines:
            completion_string = ""
            total_score = 0
            q = []

            for punc in line:
                # We already know it matches (from part 1) so skip that logic
                q.append(punc) if punc in "([{<" else q.pop()
            q.reverse()

            # whatever's left unmatched in the queue needs finished
            for ltr in q:
                completion_string += self.MATCHES[ltr]

            for ltr in completion_string:
                total_score *= 5
                total_score += self.AUTOCOMPLETE_SCORES[ltr]
            scores.append(total_score)

        scores.sort()
        return scores[(len(scores) - 1) // 2]
