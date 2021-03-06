import numpy as np

input_data = np.loadtxt("input_day5.txt", dtype=str, delimiter=" -> ")
lines = np.array(list(list(np.fromstring(point, dtype=int, sep=",") for point in line) for line in input_data))
vents = np.empty((0, 2))
for line in lines:
    x1 = line[0][0]
    x2 = line[1][0]
    y1 = line[0][1]
    y2 = line[1][1]
    if x1 == x2:
        ys = np.arange(min(y1, y2), max(y1, y2) + 1)
        segment = np.transpose(np.vstack((x1 * np.ones_like(ys), ys)))
        vents = np.vstack((vents, segment))
    elif y1 == y2:
        xs = np.arange(min(x1, x2), max(x1, x2) + 1)
        segment = np.transpose(np.vstack((xs, y1 * np.ones_like(xs))))
        vents = np.vstack((vents, segment))

vents = np.array(list(str(vent) for vent in vents))     # slow
unique_results = np.unique(np.unique(vents, return_counts=True)[1], return_counts=True)
if unique_results[0][1] == 2:
    final_outcome = np.sum(unique_results[1][1:])
    print("final outcome:", final_outcome)
else:
    "seems like there are no lines that intersect once, so please check data"
