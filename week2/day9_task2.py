import numpy as np

raw_map = np.array([list(line) for line in open("input_day9.txt", "r").read().split("\n")], dtype=int)
heightmap = np.pad(raw_map, 1, constant_values=9)
basin_map = np.zeros_like(heightmap)
for i in range(1, raw_map.shape[0]+1):
    for j in range(1, raw_map.shape[1]+1):
        if heightmap[i, j] < 9:
            top = heightmap[i - 1, j] < 9
            left = heightmap[i, j - 1] < 9
            top_basin = basin_map[i - 1, j]
            left_basin = basin_map[i, j - 1]
            if top and left:
                basin_map[np.where(basin_map == left_basin)] = top_basin
                basin_map[i, j] = top_basin
            elif top:
                basin_map[i, j] = top_basin
            elif left:
                basin_map[i, j] = left_basin
            else:
                basin_map[i, j] = np.max(basin_map) + 1
basin_map = basin_map[1:raw_map.shape[0]+1, 1:raw_map.shape[1]+1]
unique, counts = np.unique(basin_map, return_counts=True)
if unique[0] == 0:
    unique = unique[1:]
    counts = counts[1:]
order = np.argsort(-counts)
unique = unique[order]
counts = counts[order]
final_result = 1
for n in range(3):
    final_result *= counts[n]
print("final result:", final_result)
