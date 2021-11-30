from argparse import ArgumentParser

from solutions.Puzzle import Puzzle
from importlib import import_module


def dynamicimport(day: str):
    mod = import_module(f"solutions.{day}")
    solution = getattr(mod, day.title())
    return solution(day)


parser = ArgumentParser()
parser.add_argument("day", help="which day to run")
args = parser.parse_args()

day: Puzzle = dynamicimport(args.day)

day.solve()
