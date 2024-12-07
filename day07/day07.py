# https://adventofcode.com/2024/day/7

from copy import deepcopy
import os
import itertools as it
import operator as op

def solve(calculations,OPS):
    # 3267 81 40 27
    res = 0
    for nums in calculations:
        result = nums.pop(0)
        ops = list(map(list, it.product(OPS.keys(), repeat=len(nums) - 1)))
        for o in ops:
            a = nums[0]
            for b in nums[1:]:
                a = OPS[o.pop(0)](a, b)
            if a == result:
                res += result
                break
    return res

def main(test):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.readlines()

    lines = [list(map(int, line.strip().replace(":", "").split())) for line in lines]

    OPS = {"*": op.mul, "+": op.add}
    result1 = solve(deepcopy(lines),OPS)

    OPS["||"]=lambda a, b: int(str(a) + str(b))
    result2 = solve(deepcopy(lines),OPS)

    print(
        f"The result for part 1 is {result1}",
        f"The result for part 2 is {result2}",
        sep="\n",
    )


print("Test")
main(test=True)

print("Real")
main(test=False)
