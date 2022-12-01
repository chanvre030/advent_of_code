import numpy as np

from scipy.sparse.dok import dok_matrix
from scipy.sparse.csgraph import dijkstra

raw_data = np.array([list(line) for line in open("input_day15.txt", "r").read().split("\n")], dtype=int)
full_data = np.empty((0, 5 * raw_data.shape[1]))
for r in range(5):
    data = raw_data + r
    data = np.where(data > 9, data - 9, data)
    row = data
    for d in range(5-1):
        data = data + 1
        data = np.where(data > 9, 1, data)
        row = np.hstack((row, data))
    full_data = np.vstack((full_data, row))

nr = full_data.shape[0]
nc = full_data.shape[1]

graph = dok_matrix((nr * nc, nr * nc), dtype=int)
for i in range(nr):
    for j in range(nc):
        n = i * full_data.shape[1] + j
        for x in [n - nc, n - 1, n + 1, n + nc]:
            x_first_of_row = x % nc == 0
            x_last_of_row = (x + 1) % nc == 0
            n_first_of_row = n % nc == 0
            n_last_of_row = (n + 1) % nc == 0
            line_jump = (x_first_of_row and n_last_of_row) or (x_last_of_row and n_first_of_row)
            if 0 <= x < nr * nc and not line_jump:
                z = full_data[i, j]
                graph[x, n] = z

risk_matrix = dijkstra(csgraph=graph, directed=True, indices=0, min_only=True)
final_risk = int(risk_matrix[nr * nc - 1])
print("lowest risk is:", final_risk)
