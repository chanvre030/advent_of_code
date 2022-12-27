import os

from pathlib import Path
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

import numpy as np


def main():
    parent = Path(__file__).parent.resolve()
    txt = "input_day12.txt"
    path = os.path.join(parent, txt)
    with open(path) as file:
        raw_data = file.read().split("\n")
    data = []
    alphabet = "SabcdefghijklmnopqrstuvwxyzE"
    for line in raw_data:
        data.append([alphabet.index(letter) for letter in line])
    data_map = np.array(data)
    start = np.where(data_map == alphabet.index("S"))
    end = np.where(data_map == alphabet.index("E"))
    data_map = np.where(data_map == alphabet.index("S"), alphabet.index("S") + 1, data_map)
    data_map = np.where(data_map == alphabet.index("E"), alphabet.index("E") - 1, data_map)

    pad = 1
    data_map = np.pad(data_map, pad, mode='constant', constant_values=np.max(data_map)+2)
    start = (start[0][0]+pad) * data_map.shape[1] + (start[1][0]+pad)
    end = (end[0][0]+pad) * data_map.shape[1] + (end[1][0]+pad)

    connections = np.zeros((data_map.size, data_map.size))
    for r in range(1, data_map.shape[0]-1):
        for c in range(1, data_map.shape[1]-1):
            for nbr, nbc in zip([r-1, r+1, r, r], [c, c, c-1, c+1]):
                dif = data_map[nbr, nbc] - data_map[r, c]
                if dif <= 1:
                    connections[r*data_map.shape[1] + c, nbr*data_map.shape[1] + nbc] = 1

    graph = csr_matrix(connections)
    dist_matrix, predecessors = dijkstra(csgraph=graph, directed=True, indices=start, return_predecessors=True)
    steps = int(dist_matrix[end])

    print(f"answer is {steps}")


if __name__ == "__main__":
    main()
