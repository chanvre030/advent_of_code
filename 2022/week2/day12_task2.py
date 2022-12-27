import os

from pathlib import Path
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

import numpy as np


def conv_indexes(row_indexes, col_indexes, n_cols):
    indexes = (row_indexes * n_cols) + col_indexes
    return indexes


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
    end = np.where(data_map == alphabet.index("E"))
    data_map = np.where(data_map == alphabet.index("S"), alphabet.index("S") + 1, data_map)
    data_map = np.where(data_map == alphabet.index("E"), alphabet.index("E") - 1, data_map)

    pad = 1
    data_map = np.pad(data_map, pad, mode='constant', constant_values=data_map.size)
    n_rows_pad = data_map.shape[0]
    n_cols_pad = data_map.shape[1]

    end = conv_indexes(end[0]+pad, end[1]+pad, n_cols_pad)
    indices = np.where(data_map == alphabet.index("a"))
    indices = conv_indexes(indices[0], indices[1], n_cols_pad)

    connections = np.zeros((data_map.size, data_map.size))
    for r in range(pad, n_rows_pad - pad):
        for c in range(pad, n_cols_pad - pad):
            for nbr, nbc in zip([r-1, r+1, r, r], [c, c, c-1, c+1]):
                dif = data_map[nbr, nbc] - data_map[r, c]
                if dif <= 1:
                    connections[r*data_map.shape[1] + c, nbr*data_map.shape[1] + nbc] = 1

    graph = csr_matrix(connections)
    dist_matrix = dijkstra(csgraph=graph, directed=True, indices=indices, min_only=True)
    n_steps = int(dist_matrix[end])

    print(f"answer is {n_steps}")


if __name__ == "__main__":
    main()
