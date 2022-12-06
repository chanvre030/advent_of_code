import os

from pathlib import Path


def main():
    parent = Path(__file__).parent.resolve()
    txt = "input_day6.txt"
    path = os.path.join(parent, txt)
    with open(path) as file:
        raw_data = file.read()
    for i in range(14, len(raw_data)):
        window = raw_data[i-14:i]
        unique_letters = []
        for c in window:
            if c not in unique_letters:
                unique_letters.append(c)
        if len(unique_letters) == 14:
            print(f"answer is: {i}")
            break


if __name__ == "__main__":
    main()
