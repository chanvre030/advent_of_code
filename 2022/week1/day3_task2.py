import numpy as np
import os

from pathlib import Path


def main():
    parent = Path(__file__).parent.resolve()
    txt = "input_day3.txt"
    path = os.path.join(parent, txt)
    letters = np.array(list("_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    with open(path) as file:
        raw_data = file.read()
    rucksacks = raw_data.split("\n")
    prios = []
    for i in range(0, len(rucksacks), 3):
        bag1 = set(rucksacks[i])
        bag2 = set(rucksacks[i+1])
        bag3 = set(rucksacks[i+2])
        common = list(bag1.intersection(bag2).intersection(bag3))
        prios.append(np.where(letters == common[0]))
    prios = np.array(prios)
    total_prio = np.sum(prios)
    print(f"sum of priorities is {total_prio}")


if __name__ == "__main__":
    main()
