import numpy as np
import os

from pathlib import Path


def main():
    parent = Path(__file__).parent.resolve()
    txt = "input_day1.txt"
    path = os.path.join(parent, txt)
    nums = np.loadtxt(path, delimiter="\n")
    prev = nums[0]
    counter = 0
    for num in nums[1:]:
        if num > prev:
            counter += 1
        prev = num
    print(counter)


if __name__ == "__main__":
    main()
