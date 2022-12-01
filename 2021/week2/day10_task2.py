import numpy as np
import os

from pathlib import Path


def main():
    openers = ["(", "[", "{", "<"]
    closers = [")", "]", "}", ">"]
    values = np.array([1, 2, 3, 4])
    scores = []

    parent = Path(__file__).parent.resolve()
    txt = "input_day10.txt"
    path = os.path.join(parent, txt)
    data = list(str(line) for line in open(path, "r").read().split("\n"))
    for line in data:
        skip_completion = False
        states = []
        for char in line:
            if char in openers:
                states.append(openers.index(char))
            elif char in closers:
                if states[-1] == closers.index(char):
                    states.pop(-1)
                else:
                    skip_completion = True
                    break
        if not skip_completion:
            score = np.array([0], dtype='int64')
            for i in states[::-1]:
                score = (score * 5) + values[i]
            scores.append(score[0])
    scores.sort()
    final_score = scores[int((len(scores) - 1) / 2)]
    print("final score:", final_score)


if __name__ == "__main__":
    main()
