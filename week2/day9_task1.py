import numpy as np

raw_map = np.array([list(line) for line in open("input_day9.txt", "r").read().split("\n")], dtype=int)
heightmap = np.pad(raw_map, 1, constant_values=np.max(raw_map))
low_map = np.empty_like(raw_map)
for i in range(1, raw_map.shape[0]+1):
    for j in range(1, raw_map.shape[1]+1):
        low_list = []
        for k in range(i - 1, i + 2, 2):
            low_list.append(heightmap[i, j] < heightmap[k, j])
        for m in range(j - 1, j + 2, 2):
            low_list.append(heightmap[i, j] < heightmap[i, m])
        low_map[i - 1, j - 1] = all(low_list)
total_risk = np.sum(np.multiply(low_map, raw_map) + low_map)
print("total risk:", total_risk)
