import os
import re
import numpy as np

from pathlib import Path


# terrible code, but it works :)
def main():
    parent = Path(__file__).parent.resolve()
    txt = "input_day8.txt"
    path = os.path.join(parent, txt)
    with open(path) as file:
        data = file.read()
    grid = np.array([re.findall("[0-9]", line) for line in data.split("\n")], int)
    sz = grid.shape
    scenic_scores = np.zeros_like(grid)
    for r, row in enumerate(grid):
        rr = sz[0] - r
        for c, tree in enumerate(row):
            cc = sz[1] - c
            on_edge = r == 0 or r == sz[0]-1 or c == 0 or c == sz[1]-1
            if not on_edge:
                scores = [0, 0, 0, 0]

                # left
                blocked = False
                for i in range(1, c+1):
                    if not blocked:
                        if row[c-i] < tree:
                            scores[0] += 1
                        elif row[c-i] >= tree:
                            scores[0] += 1
                            blocked = True

                # right
                blocked = False
                for i in range(1, cc):
                    if not blocked:
                        if row[c+i] < tree:
                            scores[1] += 1
                        elif row[c+i] >= tree:
                            scores[1] += 1
                            blocked = True

                # top
                blocked = False
                for i in range(1, r+1):
                    if not blocked:
                        if grid[:, c][r-i] < tree:
                            scores[2] += 1
                        elif grid[:, c][r-i] >= tree:
                            scores[2] += 1
                            blocked = True

                # bottom
                blocked = False
                for i in range(1, rr):
                    if not blocked:
                        if grid[:, c][r+i] < tree:
                            scores[3] += 1
                        elif grid[:, c][r+i] >= tree:
                            scores[3] += 1
                            blocked = True

                scenic_scores[r, c] = scores[0]*scores[1]*scores[2]*scores[3]

    high_score = np.max(scenic_scores)
    print(f"answer is {high_score}")


if __name__ == "__main__":
    main()
