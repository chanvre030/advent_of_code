import numpy as np

openers = ["(", "[", "{", "<"]
closers = [")", "]", "}", ">"]
costs = np.array([3, 57, 1197, 25137])
errors = np.array([0, 0, 0, 0])

data = list(str(line) for line in open("input_day10.txt", "r").read().split("\n"))
for line in data:
    states = []
    for char in line:
        if char in openers:
            states.append([0, 0, 0, 0])
            states[-1][openers.index(char)] += 1
        elif char in closers:
            states[-1][closers.index(char)] -= 1
            if min(states[-1]) == 0:
                states.pop(-1)
            else:
                errors[closers.index(char)] += 1
                break
total_cost = np.sum(errors * costs)
print("final result:", total_cost)
