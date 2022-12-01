import numpy as np
import os

from pathlib import Path


def main():
    parent = Path(__file__).parent.resolve()
    txt = "input_day6.txt"
    path = os.path.join(parent, txt)

    n_days = 80

    # first try
    fish_ages_today = np.loadtxt(path, dtype=int, delimiter=",")
    for day in range(n_days):
        # print("day", day, len(fish_ages_today), "fishes")
        next_day = []
        for fish_age in fish_ages_today:
            if fish_age > 0:
                next_day.append(fish_age - 1)
            elif fish_age == 0:
                next_day.extend([6, 8])
        fish_ages_today = next_day
    print("final number of fishes:", len(fish_ages_today))

    # second try
    fish_ages_today = np.loadtxt(path, dtype=int, delimiter=",")
    for day in range(n_days):
        # print("day", day, len(fish_ages_today), "fishes")
        try:
            unique, counts = np.unique(fish_ages_today, return_counts=True)
            occurences = dict(zip(unique, counts))
            fish_ages_today = np.append(fish_ages_today, 9*np.ones(occurences[0]))
        except KeyError:
            pass
        fish_ages_today = np.where(fish_ages_today > 0, fish_ages_today - 1, 6)
    print("final number of fishes:", len(fish_ages_today))

    # third try
    starting_fishes = np.loadtxt(path, dtype=int, delimiter=",")
    fish_ages_today = np.array([0])
    n_fish = np.empty((9, 1))
    for day in range(n_days):
        # print("day", day, len(fish_ages_today), "fishes")
        try:
            unique, counts = np.unique(fish_ages_today, return_counts=True)
            occurences = dict(zip(unique, counts))
            fish_ages_today = np.append(fish_ages_today, 9*np.ones(occurences[0]))
        except KeyError:
            pass
        fish_ages_today = np.where(fish_ages_today > 0, fish_ages_today - 1, 6)
        n_fish = np.append(n_fish[1:], len(fish_ages_today))

    n_fish = np.flip(n_fish)
    unique, counts = np.unique(starting_fishes, return_counts=True)
    occurences = dict(zip(unique, counts))
    final_n_fishes = 0
    for key in occurences:
        final_fishes_key = int(n_fish[key] * occurences[key])
        final_n_fishes += final_fishes_key
    print("final number of fishes:", final_n_fishes)


if __name__ == "__main__":
    main()
