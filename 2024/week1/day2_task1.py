import numpy as np

from pathlib import Path


def main():
    parent = Path(__file__).parent.resolve()
    txt = "input_day2.txt"
    path = parent / txt

    with open(path) as file:
        raw_data = file.read()
    split_data = raw_data.split("\n")
    safe = 0
    for line in split_data:
        input_data = np.fromstring(line, dtype=int, sep=" ")
        left_data = input_data[:-1]
        right_data = input_data[1:]
        diff = right_data - left_data
        if diff[0] < 0:
            diff *= -1
        too_big_dist = np.any(diff > 3)
        wrong_sign = np.any(diff <= 0)
        if not too_big_dist and not wrong_sign:
            safe += 1

    print(f"answer: {safe}")


if __name__ == "__main__":
    main()
