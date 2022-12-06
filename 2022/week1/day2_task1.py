import os

from pathlib import Path


def main():
    parent = Path(__file__).parent.resolve()
    txt = "input_day2.txt"
    path = os.path.join(parent, txt)
    with open(path) as file:
        raw_data = file.read()
        split_data = [data_str.split(" ") for data_str in raw_data.split("\n")]
        shape_dict = {'X': 1, 'Y': 2, 'Z': 3}
        outcome_dict = {'XA': 3, 'XB': 0, 'XC': 6, 'YA': 6, 'YB': 3, 'YC': 0, 'ZA': 0, 'ZB': 6, 'ZC': 3}
        total_score = 0
        for match in split_data:
            outcome = outcome_dict.get(match[1]+match[0])
            shape_score = shape_dict.get(match[1])
            total_score += outcome + shape_score
        print(f"total score is {total_score}")


if __name__ == "__main__":
    main()
