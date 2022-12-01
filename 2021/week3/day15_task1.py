import numpy as np

from scipy.sparse.dok import dok_matrix
from scipy.sparse.csgraph import dijkstra

data = np.array([list(line) for line in open("input_day15.txt", "r").read().split("\n")], dtype=int)
nr = data.shape[0]
nc = data.shape[1]

graph = dok_matrix((nr * nc, nr * nc))
for i in range(nr):
    for j in range(nc):
        n = i * data.shape[1] + j
        for x in [n - nc, n - 1, n + 1, n + nc]:
            x_first_of_row = x % nc == 0
            x_last_of_row = (x + 1) % nc == 0
            n_first_of_row = n % nc == 0
            n_last_of_row = (n + 1) % nc == 0
            line_jump = (x_first_of_row and n_last_of_row) or (x_last_of_row and n_first_of_row)
            if 0 <= x < nr * nc and not line_jump:
                z = data[i, j]
                graph[x, n] = z

risk_matrix = dijkstra(csgraph=graph, directed=True, indices=0, min_only=True)
final_risk = int(risk_matrix[nr * nc - 1])
print("lowest risk is:", final_risk)
