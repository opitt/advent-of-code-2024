# https://adventofcode.com/2024/day/2
import os


def solve(lines):
    def valid_diffs(d):
        test_inc = lambda x: 1<=x<= 3
        test_dec = lambda x: test_inc(x * -1)
        return all(map(test_inc, d)) or all(map(test_dec, d))

    def calc_diff(levels):
        d = [b - a for a, b in zip(levels[:-1], levels[1:])]
        return d

    safe1 = 0
    safe2 = 0
    for report in lines:
        (*levels,) = map(int, report.split())

        diffs = calc_diff(levels)
        if valid_diffs(diffs):
            safe1 += 1
        else:
            for i in range(len(levels)):
                l = levels.copy()
                del l[i]
                if valid_diffs(calc_diff(l)):
                    safe2 += 1
                    break
    return safe1, safe2 + safe1


def main(test):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.readlines()
    lines = list(map(str.strip, lines))

    result1, result2 = solve(lines)
    print(
        f"The result for part 1 is {result1}",
        f"The result for part 2 is {result2}",
        sep="\n",
    )
    # 341, 404


# main(test=True)
main(test=False)
