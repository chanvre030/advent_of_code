import numpy as np
import re
import os

from pathlib import Path


def main():
    parent = Path(__file__).parent.resolve()
    txt = "input_day5.txt"
    path = os.path.join(parent, txt)
    with open(path) as file:
        raw_data = file.read().split("\n\n")

    # parse pile of crates
    state = raw_data[0].split("\n")[::-1][1:]
    state = [re.findall(r"\[.]|    ", line) for line in state]
    pile = []
    for c in range(len(state[0])):
        col = []
        for line in state:
            if len(line) > c:
                box = re.findall("[A-Z]", line[c])
                if len(box) > 0:
                    col.append(box[0])
        pile.append(col)

    # parse instructions
    raw_plan = raw_data[1].split("\n")
    plan = np.array([re.findall("[0-9]+", line) for line in raw_plan], int)

    for line in plan:
        steps, from_pile, to_pile = line
        from_pile -= 1
        to_pile -= 1
        for step in range(steps):
            pile[to_pile].append(pile[from_pile][-1])
            pile[from_pile].pop(-1)

    message = ""
    for col in pile:
        message += col[-1]

    print(f"answer is: {message}")


if __name__ == "__main__":
    main()
