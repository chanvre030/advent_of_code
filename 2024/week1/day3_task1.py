import re

from pathlib import Path


def main():
    parent = Path(__file__).parent.resolve()
    txt = "input_day3.txt"
    path = parent / txt

    with open(path) as file:
        raw_data = file.read()

    ans = 0

    finds = re.findall(r"mul\([0-9]+,[0-9]+\)", raw_data)
    for find in finds:
        numbers = re.findall(r"[0-9]+", find)
        mul = int(numbers[0]) * int(numbers[1])
        ans += mul

    print(f"answer: {ans}")


if __name__ == "__main__":
    main()
