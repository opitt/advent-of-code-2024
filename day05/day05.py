# https://adventofcode.com/2024/day/4
import os
import re


def solve1(page_updates, pages_before, pages_after):
    def validate_pages(pages):
        # 75,47,61,53,29
        ok = True
        pos = 0
        while ok and pos < len(pages):
            page = pages[pos]
            i=0
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
                i+=1
            pos+=1
        return ok, page

    wrong_updates = []
    res = 0
    for pages in page_updates:
        ok,wrong_page = validate_pages(pages)
        if ok:
            res += int(pages[len(pages) // 2])
        else:
            wrong_updates.append([pages, wrong_page])
    ## fix the wrong updates (puzzle 2)
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

    pages = []
    rules = []
    read_pages = False
    for line in lines:
        if line == "":
            read_pages = True
            continue
        if read_pages:
            pages.append(line)
        else:
            rules.append(line)

    rule_before = {}
    rule_after = {}
    for r in rules:
        p1, p2 = r.split("|")
        if p1 not in rule_before:
            rule_before[p1] = [p2]
        else:
            rule_before[p1].append(p2)
        if p2 not in rule_after:
            rule_after[p2] = [p1]
        else:
            rule_after[p2].append(p1)
    (*pages,) = (line.split(",") for line in pages)
    result1 = solve1(pages, rule_before, rule_after)
    result2 = 0  # solve2(lines)
    print(
        f"The result for part 1 is {result1}",
        f"The result for part 2 is {result2}",
        sep="\n",
    )


print("Test")
main(test=True)

print("Real")
main(test=False)
