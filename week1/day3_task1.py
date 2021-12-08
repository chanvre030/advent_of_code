import numpy as np
import re

cleared_diagnostics = []
diagnostics = np.loadtxt("input_day3.txt", dtype=str, delimiter="\n")
for line in diagnostics:
    separated = np.array(re.findall("..", line), dtype=int)
    cleared_diagnostics.append(separated)
cleared_diagnostics = np.array(cleared_diagnostics)

gamma = ""
epsilon = ""

for c in range(cleared_diagnostics.shape[1]):
    col = cleared_diagnostics[:, c]
    summed = np.sum(col)
    check = summed > 0.5 * col.shape[0]      # equal amount gives False, so 0
    gamma += str(int(check))
    epsilon += str(int(not check))

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print("\n gamma:", gamma, "\n epsilon:", epsilon)
multiplication = gamma * epsilon
print("multiplication result:", multiplication)
