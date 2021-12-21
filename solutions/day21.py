from solutions.Puzzle import Puzzle
from dataclasses import dataclass
from functools import lru_cache

# Roll die 3x, sum results
# move fwd that result
# circular board 1-10
# increase score by value of space landed on
# ends when player reach >=1000
# you use a deterministic die 1-100i

# Player 1 starting position: 5
# Player 2 starting position: 8


@dataclass
class Player:
    position: int
    score: int


class Day21(Puzzle):
    def __init__(self, filename):
        self.Player1 = Player(5, 0)
        self.Player2 = Player(8, 0)

        self.turn = self.Player1

        self.die_rolls = 0

        self.die = 1

    def part1(self) -> int:
        winner = self.play_deterministic()
        loser = self.Player1 if winner is not self.Player1 else self.Player2

        return self.die_rolls * loser.score

    def part2(self) -> int:
        # reset players
        self.__init__("ignoreme")
        return max(
            self.play_quantum(
                self.Player1.score,
                self.Player2.score,
                self.Player1.position,
                self.Player2.position,
            )
        )

    def play_deterministic(self):
        while self.Player1.score < 1000 and self.Player2.score < 1000:
            player = self.turn

            rolls = sum([wrap(x, 100) for x in range(self.die, self.die + 3)])

            self.die = wrap(self.die + 3, 100)
            self.die_rolls += 3

            player.position = wrap(player.position + rolls, 10)
            player.score += player.position

            self.turn = self.Player1 if player is not self.Player1 else self.Player2
        return self.Player1 if self.Player1.score >= 1000 else self.Player2

    @lru_cache(maxsize=None)
    def play_quantum(self, score1, score2, start1, start2):
        """
        Modified based on coolness from
        https://www.reddit.com/r/adventofcode/comments/rl6p8y/2021_day_21_solutions/hpe8pmy/
        """
        if score1 >= 21:
            return 1, 0
        elif score2 >= 21:
            return 0, 1

        wins1, wins2 = 0, 0
        # moves = possible sums of die rolls
        # ways = number of ways to acheive that sum
        for move, ways in (3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1):
            player1_pos = wrap(start1 + move, 10)
            # switch turns by switching order of inputs
            subwins2, subwins1 = self.play_quantum(
                score2, score1 + player1_pos, start2, player1_pos
            )
            wins1, wins2 = wins1 + ways * subwins1, wins2 + ways * subwins2
        return wins1, wins2


def wrap(num, max, min=1):
    while num > max:
        num = num - max
    if num < min:
        raise ValueError(f"{num} is less than {min}")

    return num
