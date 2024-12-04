# https://adventofcode.com/2024/day/4
import os
from pyexpat.errors import XML_ERROR_ASYNC_ENTITY
import re


def solve1(lines):

    def count_xmasamx(lines):
        found = 0
        for line in lines:
            found += len(re.findall("XMAS", line))
            found += len(re.findall("SAMX", line))
        return found

    def get_diagonals(lines):
        lines_diag = []
        max_col, max_row = len(lines[0]), len(lines)
        row = col = 0
        for _ in range(max_row + max_col - 1):
            y, x = row, col
            d = ""
            while y >= 0 and x < max_col:
                d += lines[y][x]
                y -= 1
                x += 1
            lines_diag.append(d)

            if row + 1 < max_row:
                row += 1
            else:
                col += 1
        return lines_diag

    res = 0
    # horizontal
    res+= count_xmasamx(lines)
    # vertical
    lines_rotated = ["".join(c) for c in zip(*lines)]
    res += count_xmasamx(lines_rotated)

    # diagonal left right
    res += count_xmasamx(get_diagonals(lines))

    # diagonal right left
    lines_rev = ["".join(line[::-1]) for line in lines]
    res += count_xmasamx(get_diagonals(lines_rev))
 
    return res


def solve2(lines):
    res = 0
    return res


def main(test):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.readlines()
    lines = list(map(str.strip, lines))

    result1, result2 = solve1(lines), solve2(lines)
    print(
        f"The result for part 1 is {result1}",
        f"The result for part 2 is {result2}",
        sep="\n",
    )
    # 166905464,72948684

print("Test")
main(test=True)

print("Real")
main(test=False)