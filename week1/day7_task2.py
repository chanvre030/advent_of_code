import numpy as np

positions = np.loadtxt("input_day7.txt", dtype=int, delimiter=",")
costs = {}
for line in range(np.min(positions), np.max(positions)):
    if line % 100 == 0:
        print(f"calculated costs of {line}/{abs(np.max(positions) - np.min(positions))} locations")
    costs[line] = sum(sum(range(1, abs(line - pos)+1)) for pos in positions)
optimum = min(costs, key=costs.get)
print(f"\noptimal location: {optimum} \n costs: {costs[optimum]}")
