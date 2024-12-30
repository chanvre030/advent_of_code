import numpy as np

from pathlib import Path


def main():
    parent = Path(__file__).parent.resolve()
    txt = "input_day1.txt"
    path = parent / txt

    input_data = np.loadtxt(path, dtype=int)
    left = input_data[:, 0]
    right = input_data[:, 1]
    left = np.sort(left)
    right = np.sort(right)
    total_score = 0
    for left_val in left:
        score = left_val * np.sum(right == left_val)
        total_score += score

    print(f"answer: {total_score}")

    pass


if __name__ == "__main__":
    main()