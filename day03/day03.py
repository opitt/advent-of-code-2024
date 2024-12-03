# https://adventofcode.com/2024/day/3
import os
import re


def solve1(lines):
    res = 0
    for memory in lines:
        muls = re.findall("mul\((\d+,\d+)\)", memory)
        res += sum(map(lambda s: int(s.split(",")[0]) * int(s.split(",")[1]), muls))
    return res


def solve2(lines):
    res = 0
    mul_on=True
    for memory in lines:
        muls = re.findall("mul\((\d+,\d+)\)|(don't)\(\)|(do)\(\)", memory)
        for m in muls:
            d,off,on = m
            if d and mul_on:
                a,b = map(int,d.split(","))
                res+=a*b
            elif off:
                mul_on=False
            elif on:
                mul_on=True

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


# main(test=True)
main(test=False)
