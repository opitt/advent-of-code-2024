# https://adventofcode.com/2024/day/1
import os
import re

def solve(lines):

    list1=[]
    list2=[]

    for l in lines:
        a,b = map(int,re.findall("\d+",l))
        list1.append(a)
        list2.append(b)
    list1.sort()
    list2.sort()
    return sum([abs(a-b) for a,b in zip(list1,list2)]), sum(a*list2.count(a) for a in list1)



def main(test):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8") as input:
        lines = input.readlines()
    lines = list(map(str.strip, lines))

    result1, result2 = solve(lines)
    print(
        f"The result for part 1 is {result1}",
        f"The result for part 2 is {result2}", sep="\n"
    )
    # 2367773, 21271939


#main(test=True)
main(test=False)
