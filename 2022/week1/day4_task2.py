import numpy as np
import os

from pathlib import Path


def main():
    parent = Path(__file__).parent.resolve()
    txt = "input_day4.txt"
    path = os.path.join(parent, txt)
    with open(path) as file:
        raw_data = file.read().split("\n")
    lines = [line.split(",") for line in raw_data]
    pairs = [pair.split("-") for line in lines for pair in line]
    pair_array = np.array(pairs, int)
    firsts = pair_array[::2]
    seconds = pair_array[1::2]

    overlap_counter = 0
    for first, second in zip(firsts, seconds):
        if second[0] <= first[0] <= second[1]:
            overlap_counter += 1
        elif first[0] <= second[0] <= first[1]:
            overlap_counter += 1

    print(f"total number of overlaps is: {overlap_counter}")


if __name__ == "__main__":
    main()
