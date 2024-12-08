# https://adventofcode.com/2024/day/8

from copy import deepcopy
import os
import re
import itertools as it
from collections import namedtuple

# Define a namedtuple type
Point = namedtuple("Point", ["y", "x"])

def solve(city,antennas):
    antinodes=[]
    max_y=len(city)-1
    max_x=len(city[0])-1

    for frequency, locations in antennas.items():
        in_line_locations = list(it.combinations(locations,2))
        for loc1, loc2 in in_line_locations:
            dy = loc1.y-loc2.y
            dx = loc1.x-loc2.x
            anti1 = Point(y=loc1.y + dy, x=loc1.x + dx)
            anti2 = Point(y=loc2.y - dy, x=loc2.x - dx)

            is_valid = lambda loc: loc.x>=0 and loc.x<=max_x and loc.y>=0 and loc.y<=max_y and loc not in antinodes
            for anti in [anti1, anti2]:
                if is_valid(anti):
                    antinodes.append(anti)

    return len(antinodes)

def main(test):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.readlines()

    city = [line.strip() for line in lines]

    antennas = {}
    for y, street in enumerate(city):
        # Find all matches and their positions
        matches = [(match.group(), match.start()) for match in re.finditer("[^.]", street)]
        for char, x in matches:
            p = Point(y=y, x=x)
            if char in antennas:
                antennas[char].append(p)
            else:
                antennas[char] = [p]

    result1 = solve(deepcopy(city),antennas)

    result2 = solve(deepcopy(city), antennas)

    print(
        f"The result for part 1 is {result1}",
        f"The result for part 2 is {result2}",
        sep="\n",
    )


print("Test")
main(test=True)

print("Real")
main(test=False)
