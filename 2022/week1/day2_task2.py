import numpy as np
import os

from pathlib import Path


def main():
    parent = Path(__file__).parent.resolve()
    txt = "input_day2.txt"
    path = os.path.join(parent, txt)
    with open(path) as file:
        raw_data = file.read()
        split_data = [data_str.split(" ") for data_str in raw_data.split("\n")]
        shape_dict = {'A': 1, 'B': 2, 'C': 3}
        outcome_dict = {'AA': 3, 'AB': 0, 'AC': 6, 'BA': 6, 'BB': 3, 'BC': 0, 'CA': 0, 'CB': 6, 'CC': 3}
        match_dict = {'XA': 'C', 'XB': 'A', 'XC': 'B', 'YA': 'A', 'YB': 'B', 'YC': 'C', 'ZA': 'B', 'ZB': 'C', 'ZC': 'A'}
        total_score = 0
        for match in split_data:
            move = match_dict.get(match[1]+match[0])
            outcome = outcome_dict.get(move+match[0])
            shape_score = shape_dict.get(move)
            total_score += outcome + shape_score
        print(f"total score is {total_score}")


if __name__ == "__main__":
    main()
