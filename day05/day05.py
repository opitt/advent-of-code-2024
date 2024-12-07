# https://adventofcode.com/2024/day/5
import os
from functools import cmp_to_key
from collections import defaultdict

def validate_pages(pages, pages_after, pages_before):
    # 75,47,61,53,29


    ok = True
    pos = 0
    while ok and pos < len(pages):
        page = pages[pos]
        i = 0
        while ok and i < len(pages):
            if i < pos:
                try:
                    ok = pages[i] in pages_after[page]
                except:
                    ok = False
            elif i > pos:
                try:
                    ok = pages[i] in pages_before[page]
                except:
                    ok = False
            i += 1
        pos += 1
    return ok


def solve1(updates, pages_before, pages_after, find_wrong=True):
    wrong = []
    res = 0
    for pages in updates:
        ok = validate_pages(pages, pages_after, pages_before)
        if ok:
            res += int(pages[len(pages) // 2])
        elif find_wrong:
            wrong.append(pages)
    return res, wrong


def solve2(wrong_pages, pages_before, pages_after):

    def custom_compare(x, y):
        # Return a negative number if x < y, zero if x == y, positive if x > y
        if x in pages_after and y in pages_after[x]:  # x > y:
            return 1
        elif x in pages_before and y in pages_before[x]:  # x < y:
            return -1
        else:
            return 0
    
    res=0
    pages_fixed = []
    for wrong in wrong_pages:
        fixed = sorted(wrong, key=cmp_to_key(custom_compare))
        pages_fixed.append(fixed)
    for pages in pages_fixed:
        ok = validate_pages(pages, pages_after, pages_before)
        if ok:
            res += int(pages[len(pages) // 2])

    return res


def main(test):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.readlines()
    lines = list(map(str.strip, lines))

    # find the rules and the pages
    pages = []
    PAGES_LARGER = defaultdict(list)
    PAGES_SMALLER = defaultdict(list)
    read_pages = False
    for line in lines:
        if line == "":
            read_pages = True
            continue
        if read_pages:
            pages.append(line.split(","))
        else:
            # rules.append(line)
            p1, p2 = line.split("|")
            PAGES_LARGER[p1].append(p2)
            PAGES_SMALLER[p2].append(p1)

    result1, wrong_pages = solve1(pages, PAGES_LARGER, PAGES_SMALLER)
    result2 = solve2(wrong_pages, PAGES_LARGER, PAGES_SMALLER)
    print(
        f"The result for part 1 is {result1}",
        f"The result for part 2 is {result2}",
        sep="\n",
    )


print("Test")
main(test=True)

print("Real")
main(test=False)
