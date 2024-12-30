import re

from pathlib import Path


def main():
    parent = Path(__file__).parent.resolve()
    txt = "input_day3.txt"
    path = parent / txt

    with open(path) as file:
        raw_data = file.read()

    ans = 0
    do = True

    finds = re.findall(r"(don't\(\))|(do\(\))|(mul\([0-9]+,[0-9]+\))", raw_data)
    for find in finds:
        if find[0] == "don't()":
            do = False
        elif find[1] == "do()":
            do = True
        elif do:
            instr = find[2]
            numbers = re.findall(r"[0-9]+", instr)
            mul = int(numbers[0]) * int(numbers[1])
            ans += mul

    print(f"answer: {ans}")


if __name__ == "__main__":
    main()
