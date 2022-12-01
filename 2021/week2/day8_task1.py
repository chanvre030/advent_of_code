import re
import os

from pathlib import Path


def main():
    parent = Path(__file__).parent.resolve()
    txt = "input_day8.txt"
    path = os.path.join(parent, txt)
    data = re.split('[\n|]', open(path, "r").read())
    filtered = [y for x in (data[i].split(" ") for i in range(1, len(data), 2)) for y in x]
    usable = len([w for w in filtered if len(w) == 2 or len(w) == 3 or len(w) == 4 or len(w) == 7])
    print(usable)


if __name__ == "__main__":
    main()

