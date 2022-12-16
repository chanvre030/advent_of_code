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

    n_parts = 10
    snake = np.zeros((2, n_parts), dtype=int)
    xs = []
    ys = []
    for instruction in data:
        for step in range(int(instruction[1])):
            move = instruction[0]
            snake[:, 0] = move_head(snake[:, 0], move)
            for i in range(1, n_parts):
                prev_part = snake[:, i-1]
                this_part = snake[:, i]
                snake[:, i] = move_tail(this_part, prev_part)
            xs.append(this_part[0])
            ys.append(this_part[1])
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
