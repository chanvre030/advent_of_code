import numpy as np
import sys

bingo_input = open("input_day4.txt", "r").read().split("\n\n")
numbers = list(map(int, bingo_input[0].split(",")))
boards = list(np.array(list(np.fromstring(line, dtype=int, sep=" ") for line in board.split("\n"))) for board in bingo_input[1:])
competing_boards = np.arange(len(boards))

binary_boards = list(np.zeros_like(board) for board in boards)
zeros = np.zeros_like(boards[0])
ones = np.ones_like(boards[0])

for number in numbers:
    for i in range(len(boards)):
        if i in competing_boards:
            binary_boards[i] = np.where(boards[i] == number, ones, binary_boards[i])
            for j in range(boards[i].shape[0]):
                horizontal = np.sum(binary_boards[i][j])
                vertical = np.sum(binary_boards[i][:, j])
                if horizontal == 5 or vertical == 5:
                    competing_boards = np.delete(competing_boards, np.argwhere(competing_boards == i))
                    if len(competing_boards) == 0:
                        final_score = np.sum(np.where(binary_boards[i] == 0, boards[i], zeros)) * number
                        print("final score:", final_score)
                        sys.exit()
