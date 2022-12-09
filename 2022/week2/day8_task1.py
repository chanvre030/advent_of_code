import os
import re
import numpy as np

from pathlib import Path


def main():
    parent = Path(__file__).parent.resolve()
    txt = "input_day8.txt"
    path = os.path.join(parent, txt)
    with open(path) as file:
        data = file.read()
    grid = np.array([re.findall("[0-9]", line) for line in data.split("\n")], int)
    sz = grid.shape
    visible_trees = np.zeros_like(grid)
    for r, row in enumerate(grid):
        for c, tree in enumerate(row):
            on_edge = r == 0 or r == sz[0]-1 or c == 0 or c == sz[1]-1
            if not on_edge:
                left = tree > np.max(row[:c])
                right = tree > np.max(row[c+1:])
                top = tree > np.max(grid[:, c][:r])
                bottom = tree > np.max(grid[:, c][r+1:])
                visible = left or right or top or bottom
                if visible:
                    visible_trees[r, c] = 1
    edge_trees = 2 * sz[0] + 2 * sz[1] - 4
    total_trees = np.sum(visible_trees) + edge_trees
    print(f"answer is {total_trees}")


if __name__ == "__main__":
    main()
