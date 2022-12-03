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
    for rucksack in rucksacks:
        comp_split = int(0.5 * len(rucksack))
        comps = [set(rucksack[:comp_split]), set(rucksack[comp_split:])]
        common = list(comps[0].intersection(comps[1]))
        prios.append(np.where(letters == common[0]))
    prios = np.array(prios)
    total_prio = np.sum(prios)
    print(f"sum of priorities is {total_prio}")


if __name__ == "__main__":
    main()
