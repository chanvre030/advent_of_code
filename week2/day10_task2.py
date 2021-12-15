import numpy as np

openers = ["(", "[", "{", "<"]
closers = [")", "]", "}", ">"]
values = np.array([1, 2, 3, 4])
additions = np.array([0, 0, 0, 0])
scores = []

data = list(str(line) for line in open("input_day10.txt", "r").read().split("\n"))
for line in data:
    skip_completion = False
    states = []
    for char in line:
        if char in openers:
            states.append(openers.index(char))
        elif char in closers:
            if states[-1] == closers.index(char):
                states.pop(-1)
            else:
                skip_completion = True
                break
    if not skip_completion:
        score = np.array([0], dtype='int64')
        for i in states[::-1]:
            score = (score * 5) + values[i]
        scores.append(score[0])
scores.sort()
final_score = scores[int((len(scores) - 1) / 2)]
print("final score:", final_score)
