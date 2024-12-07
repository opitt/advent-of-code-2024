# https://adventofcode.com/2024/day/6
import os
import itertools as it


def solve1(maze):
    max_x = len(maze[0])
    max_y = len(maze)
    pos_x, pos = y = 0, 0
    for y, line in enumerate(maze):
        try:
            x = line.index("^")
            pos_y = y
            pos_x = x
            break
        except:
            pass

    DIRS = it.cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])
    dy,dx = next(DIRS)
    while True:
        maze[pos_y][pos_x] = "X"
        if pos_y+dy < 0 or pos_y+dy >= max_y or  pos_x+dx < 0 or pos_x+dx >= max_x:
            break
        if maze[pos_y+dy][pos_x+dx]=="#":
            dy,dx = next(DIRS)
        pos_y+=dy
        pos_x+=dx
    res=sum(line.count("X") for line in maze)
    return res


def solve2(maze):

    res = 0
    return res


def main(test):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.readlines()
    lines = list(map(list, list(map(str.strip, lines))))

    result1 = solve1(lines)
    result2 = solve2(lines)
    print(
        f"The result for part 1 is {result1}",
        f"The result for part 2 is {result2}",
        sep="\n",
    )


print("Test")
main(test=True)

print("Real")
main(test=False)
