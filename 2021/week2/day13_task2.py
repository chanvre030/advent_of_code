import numpy as np
import os

from pathlib import Path


def main():
    parent = Path(__file__).parent.resolve()
    txt = "input_day13.txt"
    path = os.path.join(parent, txt)
    raw_data = open(path, "r").read().split("\n\n")
    points = np.array([dat.split(",") for dat in raw_data[0].split("\n")], dtype=int)
    instructions = np.array([d.split("=") for d in [dat.split(" ")[-1] for dat in raw_data[1].split("\n")]])
    for instruction in instructions:
        folded = []
        axis = instruction[0]
        num = int(instruction[1])
        if axis == "x":
            for point in points:
                if point[0] > num:
                    folded.append([point[0] - 2 * (point[0] - num), point[1]])
                else:
                    folded.append(point)
        elif axis == "y":
            for point in points:
                if point[1] > num:
                    folded.append([point[0], point[1] - 2 * (point[1] - num)])
                else:
                    folded.append(point)
        points = folded

    points = np.array(points)
    code = np.empty((max(points[:, 0]) + 1, max(points[:, 1]) + 1), dtype=str)
    for p in points:
        code[p[0], p[1]] = "#"
    code = np.where(code == "#", chr(9632), " ")
    for n in range(0, code.shape[0], 5):
        letter = code[n:n+4].transpose()
        print()
        for line in letter:
            print(line)


if __name__ == "__main__":
    main()
