from argparse import ArgumentParser

from solutions.Puzzle import Puzzle
from importlib import import_module


def dynamicimport(day: str, test=False):
    mod = import_module(f"solutions.{day}")
    solution = getattr(mod, day.title())
    if test:
        return solution(day+"test")
    else:
        return solution(day)


parser = ArgumentParser()
parser.add_argument("day", help="which day to run")
parser.add_argument("--test", action="store_true", help="Use {day}test.txt for input")
args = parser.parse_args()

day: Puzzle = dynamicimport(args.day, args.test)

day.solve()
