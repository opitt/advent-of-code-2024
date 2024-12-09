# https://adventofcode.com/2024/day/8
from copy import deepcopy
import re
import os
import itertools as it
from collections import namedtuple
import time

# Define a namedtuple type
Point = namedtuple("Point", ["y", "x"])

def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Execute the function
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate the execution time
        # print(f"Execution time of {func.__name__}: {execution_time:.6f} seconds")
        print(f"Execution time: {execution_time:.4f} seconds")
        print(f"Execution time: {execution_time*1_000_000:.2f} microseconds")
        return result

    return wrapper


@execution_time_decorator
def solve(blocks):
    # 12345
    file_blocks=[]
    file_free=[]
    id=0
    file_pointer=0
    for pos in range(0,len(blocks),2):
        nof_blocks = int(blocks[pos])
        try:
            free = int(blocks[pos+1])
        except:
            free = 0
        file_blocks.extend([id] * nof_blocks)
        file_blocks.extend(["."] * free)
        file_pointer += nof_blocks
        file_free.extend([file_pointer+p for p in range(free)])
        file_pointer += free
        id+=1
    while len(file_free):
        b = file_blocks[-1]
        file_blocks = file_blocks[:-1]
        if b==".":
            file_free.pop()
        else:
            file_blocks[file_free[0]] = b
            file_free.pop(0)
    checksum = sum([pos*int(b) for pos, b in enumerate(file_blocks)])
    return checksum


@execution_time_decorator
def solve2(blocks):
    return 0


def main(test):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.readlines()

    blocks = lines[0].strip()

    print("PART 1")
    result = solve(blocks)
    print(f"The result is {result}")

    print("PART 2")
    result2 = solve2(blocks)
    print(f"The result is {result}")


print("####### TEST ###############################")
main(test=True)
print()
print("####### REAL ###############################")
main(test=False)
