from solutions.Puzzle import Puzzle


class Day4(Puzzle):
    def __init__(self, filename):
        with open(f"inputs/{filename}.txt") as f:
            self.order = [int(i) for i in f.readline().split(",")]
            self.boards = []

            boards = [b.split("\n") for b in f.read().split("\n\n")]
            for i, board in enumerate(boards):
                nb = []
                for line in board:
                    nl = [int(n) for n in line.split(" ") if n]
                    if len(nl):
                        nb.append(nl)
                self.boards.append(nb)

    def play(self, action="win"):
        boards = self.boards

        for num in self.order:
            new_set = boards.copy()

            for board in boards:
                for line in board:
                    if num in line:
                        line[line.index(num)] = -1
                if check_winner(board):
                    if action == "win":
                        return (num, board)
                    else:
                        new_set.remove(board)
                        if len(new_set) == 0:
                            return (num, board)
            boards = new_set

        raise Exception("No winner!")

    def part1(self) -> int:
        winning_number, winning_board = self.play()
        bsum = sum(sum(c for c in row if c > 0) for row in winning_board)
        return bsum * winning_number

    def part2(self) -> int:
        losing_number, losing_board = self.play(action="lose")
        bsum = sum(sum(c for c in row if c > 0) for row in losing_board)

        return bsum * losing_number


def check_winner(board: list):
    return check_vertical(board) or check_horizontal(board)


def check_horizontal(board: list):
    for row in board:
        if sum(row) == -5:
            return True
    return False


def check_vertical(board: list):
    for i in range(0, len(board[0])):
        if sum([row[i] for row in board]) == -5:
            return True
    return False
