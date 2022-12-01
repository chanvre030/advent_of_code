import numpy as np
import os

from pathlib import Path


def main():
    openers = ["(", "[", "{", "<"]
    closers = [")", "]", "}", ">"]
    costs = np.array([3, 57, 1197, 25137])
    errors = np.array([0, 0, 0, 0])

    parent = Path(__file__).parent.resolve()
    txt = "input_day10.txt"
    path = os.path.join(parent, txt)
    data = list(str(line) for line in open(path, "r").read().split("\n"))
    for line in data:
        states = []
        for char in line:
            if char in openers:
                states.append([0, 0, 0, 0])
                states[-1][openers.index(char)] += 1
            elif char in closers:
                states[-1][closers.index(char)] -= 1
                if min(states[-1]) == 0:
                    states.pop(-1)
                else:
                    errors[closers.index(char)] += 1
                    break
    total_cost = np.sum(errors * costs)
    print("final result:", total_cost)


if __name__ == "__main__":
    main()
