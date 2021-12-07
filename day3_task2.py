import numpy as np
import re

cleared_diagnostics = []
diagnostics = np.loadtxt("input_day3.txt", dtype=str, delimiter="\n")
for line in diagnostics:
    separated = np.array(re.findall(".", line), dtype=int)
    cleared_diagnostics.append(separated)
oxygen_numbers = np.array(cleared_diagnostics)
co2_numbers = np.array(cleared_diagnostics)

for c in range(oxygen_numbers.shape[1]):
    if oxygen_numbers.shape[0] > 1:
        col = oxygen_numbers[:, c]
        summed = np.sum(col)
        most_appearing = summed >= 0.5 * col.shape[0]      # equal amount gives 1
        oxygen_numbers = oxygen_numbers[np.where(oxygen_numbers[:, c] == most_appearing)]
    oxygen_rating = ''.join(map(str, oxygen_numbers[0]))

for c in range(co2_numbers.shape[1]):
    if co2_numbers.shape[0] > 1:
        col = co2_numbers[:, c]
        summed = np.sum(col)
        least_appearing = not (summed >= 0.5 * col.shape[0])      # equal amount gives 0
        co2_numbers = co2_numbers[np.where(co2_numbers[:, c] == least_appearing)]
    co2_rating = ''.join(map(str, co2_numbers[0]))

oxygen_rating = int(oxygen_rating, 2)
co2_rating = int(co2_rating, 2)
print("\n oxygen rating:", oxygen_rating, "\n co2 rating:", co2_rating)
multiplication = oxygen_rating * co2_rating
print("multiplication result:", multiplication)
