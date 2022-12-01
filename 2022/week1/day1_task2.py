import numpy as np
import os

from pathlib import Path


def main():
    parent = Path(__file__).parent.resolve()
    txt = "input_day1.txt"
    path = os.path.join(parent, txt)
    with open(path) as file:
        raw_data = file.read()
        split_data = [data_str.split("\n") for data_str in raw_data.split("\n\n")]
        totals = []
        for data_list in split_data:
            data_list = np.array(data_list, dtype='int')
            totals.append(np.sum(data_list))
        sorted_data = np.sort(np.array(totals))
        total = np.sum(sorted_data[-3:])
        print(f"answer is {total}")


if __name__ == "__main__":
    main()
