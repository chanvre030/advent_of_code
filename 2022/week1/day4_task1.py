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

    inclusion_counter = 0
    for first, second in zip(firsts, seconds):
        if first[0] >= second[0] and first[1] <= second[1]:
            inclusion_counter += 1
        elif second[0] >= first[0] and second[1] <= first[1]:
            inclusion_counter += 1

    print(f"total number of inclusions is: {inclusion_counter}")


if __name__ == "__main__":
    main()
