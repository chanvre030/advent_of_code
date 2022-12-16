import os
import numpy as np

from pathlib import Path


def move_head(head_pos, move):
    if move == "U":
        head_pos[0] += 1
    elif move == "D":
        head_pos[0] -= 1
    elif move == "L":
        head_pos[1] -= 1
    elif move == "R":
        head_pos[1] += 1
    return head_pos


def move_tail(tail_pos, head_pos):
    dif = head_pos - tail_pos
    mov_diag = np.sum(abs(dif)) > 2

    x = dif[0]
    y = dif[1]

    if x > 0:
        if (x > 1) or mov_diag:
            tail_pos[0] += 1
    elif x < 0:
        if (x < -1) or mov_diag:
            tail_pos[0] -= 1

    if y > 0:
        if (y > 1) or mov_diag:
            tail_pos[1] += 1
    elif y < 0:
        if (y < -1) or mov_diag:
            tail_pos[1] -= 1

    return tail_pos


def main():
    parent = Path(__file__).parent.resolve()
    txt = "input_day9.txt"
    path = os.path.join(parent, txt)
    with open(path) as file:
        raw_data = file.read().split("\n")
    data = [line.split(" ") for line in raw_data]

    h = np.array([0, 0])
    t = np.array([0, 0])
    xs = []
    ys = []
    for instruction in data:
        for step in range(int(instruction[1])):
            move = instruction[0]
            h = move_head(h, move)
            t = move_tail(t, h)
            xs.append(t[0])
            ys.append(t[1])
    visited = np.vstack((np.array(xs), np.array(ys)))
    x_range = np.max(visited[0, :]) - np.min(visited[0, :]) + 1
    y_range = np.max(visited[1, :]) - np.min(visited[1, :]) + 1
    visit_mask = np.zeros((x_range, y_range))
    for px, py in zip(visited[0], visited[1]):
        visit_mask[px, py] = 1
    visited_positions = int(np.sum(visit_mask))

    print(f"answer is {visited_positions}")


if __name__ == "__main__":
    main()
