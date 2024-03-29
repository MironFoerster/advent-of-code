from aocd import get_data
from aocd import submit
import sys
import argparse
from datetime import datetime, timedelta, timezone



#from oliver-ni's aoc GitHub repo
now = datetime.now(timezone(timedelta(hours=-5)))
parser = argparse.ArgumentParser(description="Run Advent of Code solutions.")
parser.add_argument("--year", "-y", type=int, help="The year to run.", default=now.year)
parser.add_argument("--day", "-d", type=int, help="The day to run.", default=now.day)
parser.add_argument("--extra", "-e", help="Choose a different solution to run.", default="")
args = parser.parse_args()

try:
    exec(f"import y{args.year}.d{args.day:02}{args.extra} as day")
except ModuleNotFoundError:
    print(f"The module y{args.year}.d{args.day:02}{args.extra} does not exist! exiting" )
    sys.exit(1)

print(f"{args.year} - {args.day:02}")

data = get_data(day=args.day, year=args.year)


test = day.solution(day.test)

if test == day.val[len(day.val)-1]:
    print("Test valid: ", test)
    answer = day.solution(data)

    # submit handles if part a/b
    submit(answer, day=args.day, year=args.year)
else:
    print("BAD TEST: ", test, "-->", day.val[len(day.val)-1])
