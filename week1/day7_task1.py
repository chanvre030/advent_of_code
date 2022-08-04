import numpy as np
import os

from pathlib import Path


def main():
    parent = Path(__file__).parent.resolve()
    txt = "input_day7.txt"
    path = os.path.join(parent, txt)
    positions = np.loadtxt(path, dtype=int, delimiter=",")
    costs = {}
    for line in range(np.min(positions), np.max(positions)):
        if line % 100 == 0:
            print(f"calculated costs of {line}/{abs(np.max(positions) - np.min(positions))} locations")
        costs[line] = sum(abs(line - pos) for pos in positions)
    optimum = min(costs, key=costs.get)
    print(f"\noptimal location: {optimum} \n costs: {costs[optimum]}")


if __name__ == "__main__":
    main()
