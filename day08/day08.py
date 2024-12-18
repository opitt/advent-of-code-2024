# https://adventofcode.com/2024/day/8
from copy import deepcopy
import re
import os
import itertools as it
from collections import namedtuple
import time

# Define a namedtuple type
Point = namedtuple("Point", ["y", "x"])

def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Execute the function
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate the execution time
        # print(f"Execution time of {func.__name__}: {execution_time:.6f} seconds")
        print(f"Execution time: {execution_time:.4f} seconds")
        print(f"Execution time: {execution_time*1_000_000:.2f} microseconds")
        return result

    return wrapper


@execution_time_decorator
def solve(city, antennas):
    antinodes = set()
    is_inside = (
        lambda loc: loc.x >= 0
        and loc.x <= len(city[0]) - 1
        and loc.y >= 0
        and loc.y <= len(city) - 1
    )
    for locations in antennas.values():
        in_line_locations = list(it.combinations(locations, 2))
        for loc1, loc2 in in_line_locations:
            dy = loc1.y - loc2.y
            dx = loc1.x - loc2.x
            anti1 = Point(y=loc1.y + dy, x=loc1.x + dx)
            anti2 = Point(y=loc2.y - dy, x=loc2.x - dx)

            for anti in [anti1, anti2]:
                if is_inside(anti):
                    antinodes.add(anti)

    return len(antinodes)


@execution_time_decorator
def solve2(city, antennas):
    antinodes = set()
    is_inside = (
        lambda loc: loc.x >= 0
        and loc.x <= len(city[0]) - 1
        and loc.y >= 0
        and loc.y <= len(city) - 1
    )
    for antenna_locations in antennas.values():
        in_line_locations = list(it.combinations(antenna_locations, 2))
        for loc1, loc2 in in_line_locations:
            dy, dx = loc1.y - loc2.y, loc1.x - loc2.x

            anti = loc1
            while is_inside(anti):
                antinodes.add(anti)
                anti = Point(y=anti.y + dy, x=anti.x + dx)

            anti = loc2
            while is_inside(anti):
                antinodes.add(anti)
                anti = Point(y=anti.y - dy, x=anti.x - dx)

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
        matches = [
            (match.group(), match.start()) for match in re.finditer("[^.]", street)
        ]
        for char, x in matches:
            p = Point(y=y, x=x)
            if char in antennas:
                antennas[char].append(p)
            else:
                antennas[char] = [p]

    print("PART 1")
    result = solve(deepcopy(city), antennas)
    print(f"The result is {result}")

    print("PART 2")
    result2 = solve2(deepcopy(city), antennas)
    print(f"The result is {result}")


print("####### TEST ###############################")
main(test=True)
print()
print("####### REAL ###############################")
main(test=False)
