# https://adventofcode.com/2024/day/6
from collections import namedtuple
from copy import deepcopy
import os
import itertools as it

Point = namedtuple("Point",["y","x"])

def solve1(maze):

    # find the staring position
    for y, line in enumerate(maze):
        try:
            guard=Point(y = y,x=line.index("^"))
            break
        except:
            pass

    visited = []
    DIR = {"^":(-1, 0), ">":(0, 1), "v":(1, 0), "<":(0, -1)}
    NEXT_DIR = {"^":">",">":"v","v":"<","<":"^"}
    is_inside=lambda p: p.y >= 0 and p.y <= len(maze)-1 and p.x >= 0 and p.x <= len(maze[0])-1

    dir = "^"
    dy, dx = DIR[dir]
    while True:
        visited.append((guard, dir))
        new_pos = Point(y=guard.y+dy, x=guard.x+dx)
        if not is_inside(new_pos):
            # guard steped outside
            break

        if maze[new_pos.y][new_pos.x] == "#":
            dir = NEXT_DIR[dir]
            visited.append((guard, dir))
            dy, dx = DIR[dir]
            new_pos = Point(y=guard.y + dy, x=guard.x + dx)
        guard = new_pos

    res = len(set(p for p, _ in visited))
    return res


def solve2(maze):

    # find the staring position
    for y, line in enumerate(maze):
        try:
            guard = Point(y=y, x=line.index("^"))
            break
        except:
            pass

    visited = []
    DIR = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    NEXT_DIR = {"^": ">", ">": "v", "v": "<", "<": "^"}
    is_inside = (
        lambda p: p.y >= 0
        and p.y <= len(maze) - 1
        and p.x >= 0
        and p.x <= len(maze[0]) - 1
    )

    dir = "^"
    dy, dx = DIR[dir]
    while True:
        visited.append((guard, dir))
        new_pos = Point(y=guard.y + dy, x=guard.x + dx)
        if not is_inside(new_pos):
            # guard steped outside
            break

        if maze[new_pos.y][new_pos.x] == "#":
            dir = NEXT_DIR[dir]
            visited.append((guard, dir))
            dy, dx = DIR[dir]
            new_pos = Point(y=guard.y + dy, x=guard.x + dx)
        guard = new_pos

    res = len(set(p for p, _ in visited))
    return res


def main(test):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.readlines()
    lines = list(map(list, list(map(str.strip, lines))))

    result1 = solve1(deepcopy(lines))
    result2 = solve2(deepcopy(lines))
    print(
        f"The result for part 1 is {result1}",
        f"The result for part 2 is {result2}",
        sep="\n",
    )


print("Test")
main(test=True)

print("Real")
main(test=False)
