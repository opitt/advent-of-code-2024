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

    def get_diagonal_with_offset(matrix, offset=0):
        rows = len(matrix)
        cols = len(matrix[0])
        diagonal = []
        start_row = max(0, -offset)
        start_col = max(0, offset)

        row, col = start_row, start_col
        while row < rows and col < cols:
            diagonal.append(matrix[row][col])
            row += 1
            col += 1
        return "".join(diagonal)

    res = 0
    # horizontal
    found = count_xmasamx(lines)
    res += found
    # vertical
    lines_rotated = ["".join(c) for c in zip(*lines)]
    found = count_xmasamx(lines_rotated)
    res += found

    # diagonal left right
    lines_diag1 = []
    max_col, max_row = len(lines[0]), len(lines)
    row = col = 0
    for _ in range(max_row + max_col - 1):
        y, x = row, col
        d = ""
        while y >= 0 and x < max_col:
            d += lines[y][x]
            y -= 1
            x += 1
        lines_diag1.append(d)

        if row + 1 < max_row:
            row += 1
        else:
            col += 1
    found = count_xmasamx(lines_diag1)
    res += found

    # diagonal right left
    lines_rev = ["".join(line[::-1]) for line in lines]
    lines_diag2 = []
    row = col = 0
    for _ in range(max_row + max_col - 1):
        y, x = row, col
        d = ""
        while y >= 0 and x < max_col:
            d += lines_rev[y][x]
            y -= 1
            x += 1
        lines_diag2.append(d)

        if row + 1 < max_row:
            row += 1
        else:
            col += 1
    found = count_xmasamx(lines_diag2)
    res += found

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
