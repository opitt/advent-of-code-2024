# https://adventofcode.com/2024/day/6
from copy import deepcopy
import os
import itertools as it


def solve1(maze):
    max_x = len(maze[0])
    max_y = len(maze)

    for y, line in enumerate(maze):
        try:
            x = line.index("^")
            pos_y = y
            pos_x = x
            break
        except:
            pass

    visited = []

    DIR = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    DIRS = it.cycle("^>v<")
    dir = next(DIRS)
    dy, dx = DIR[dir]
    while True:
        visited.append((pos_y, pos_x, dir))
        if (
            pos_y + dy < 0
            or pos_y + dy >= max_y
            or pos_x + dx < 0
            or pos_x + dx >= max_x
        ):
            break
        if maze[pos_y + dy][pos_x + dx] == "#":
            dir = next(DIRS)
            visited.append((pos_y, pos_x, dir))
            dy, dx = DIR[dir]
        pos_y += dy
        pos_x += dx
    res = len(set((y, x) for y, x, _ in visited))
    return res


def solve2(maze):
    max_x = len(maze[0])
    max_y = len(maze)
    res=0
    for y, line in enumerate(maze):
        try:
            x = line.index("^")
            pos_y = y
            pos_x = x
            break
        except:
            pass

    visited = []

    DIR = {"^":(-1, 0), ">":(0, 1), "v":(1, 0), "<":(0, -1)}
    NEXT_DIR = {"^":">",">":"v","v":"<","<":"^"}

    dir = "^"
    dy,dx=DIR[dir]
    while True:
        visited.append((pos_y,pos_x,dir))
        if (
            pos_y + dy < 0
            or pos_y + dy >= max_y
            or pos_x + dx < 0
            or pos_x + dx >= max_x
        ):
            break

        if maze[pos_y + dy][pos_x + dx] == "#":
            dir = NEXT_DIR[dir]
            visited.append((pos_y,pos_x,dir))
            dy,dx=DIR[dir]
        else:
            what_if_dir = NEXT_DIR[dir]
            what_if_dy, what_if_dx = DIR[what_if_dir]
            if (
                pos_y + what_if_dy,
                pos_x + what_if_dx,
                what_if_dir,
            ) in visited:  # loop opportunity
                res += 1

        pos_y += dy
        pos_x += dx

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
