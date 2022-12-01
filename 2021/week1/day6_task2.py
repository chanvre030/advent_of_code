import numpy as np
import os

from pathlib import Path


def get_histogram(population):
    unique, counts = np.unique(population, return_counts=True)
    hist_in_dict = dict(zip(unique, counts))
    histogram = np.zeros(mfa)
    for k in range(mfa):
        try:
            histogram[k] = hist_in_dict[k]
        except KeyError:
            histogram[k] = 0
    return histogram


def histograms_after_n_days(days):
    fish_ages_today = np.array([0])
    histograms_last_days = np.identity(mfa)
    for day in range(days):
        # if day % 50 == 0:
        #     print("day", day)
        try:
            occurrences = get_histogram(fish_ages_today)
            fish_ages_today = np.append(fish_ages_today, mfa*np.ones(int(occurrences[0])))
        except KeyError:
            pass
        fish_ages_today = np.where(fish_ages_today > 0, fish_ages_today - 1, 6)
        histograms_last_days = np.vstack((histograms_last_days[1:], get_histogram(fish_ages_today)))
    histograms_last_days = np.flip(histograms_last_days, axis=0)
    return histograms_last_days


def combine_histograms(start_histogram, historical_histograms):
    key_histograms = np.zeros((mfa, mfa))
    for key in range(mfa):
        try:
            key_histogram = (start_histogram[key] * bar for bar in historical_histograms[key])
            key_histograms[key] = np.array(list(key_histogram))
        except IndexError:
            key_histograms[key] = np.array(list(0 for _ in historical_histograms[key]))
    final_histogram = np.sum(key_histograms, axis=0)
    return final_histogram


def main():
    parent = Path(__file__).parent.resolve()
    txt = "input_day6.txt"
    path = os.path.join(parent, txt)
    current_population = np.loadtxt(path, dtype=int, delimiter=",")
    population_histogram = get_histogram(current_population)
    age_histograms = histograms_after_n_days(max_calc_days)
    repetitions = n_days // max_calc_days
    rest = n_days % max_calc_days
    with np.printoptions(precision=0):
        for i in range(repetitions):
            print(f"population after {i * max_calc_days} days: {np.sum(population_histogram)} {population_histogram}")
            population_histogram = combine_histograms(population_histogram, age_histograms)
        print(f"population after {repetitions * max_calc_days} days: {np.sum(population_histogram)} {population_histogram}")
        final_histograms = histograms_after_n_days(rest)
        final_population = combine_histograms(population_histogram, final_histograms)
        print(f"population after {n_days} days: {np.sum(final_population)}, {final_population}")
        print("\n final population:", int(np.sum(final_population)))


if __name__ == "__main__":
    n_days = 256
    max_calc_days = 100
    max_fish_age = 8
    mfa = max_fish_age + 1

    main()
