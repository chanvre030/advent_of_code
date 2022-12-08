import os
import re

from pathlib import Path


def main():
    parent = Path(__file__).parent.resolve()
    txt = "input_day7.txt"
    path = os.path.join(parent, txt)
    with open(path) as file:
        raw_data = file.read()
    data = raw_data.split("\n")
    dir_tree = []
    dir_sizes = {}
    for line in data:
        if line[0:5] == "$ cd ":
            if line[5:] == "..":
                dir_tree.pop(-1)
            elif line[5:] == "/":
                dir_tree = ["/"]
            else:
                dir_tree.append(line[5:])
        elif line[0] in "0123456789":
            file_size = int(re.findall("[0-9]*", line)[0])
            for dir_num in range(len(dir_tree)):
                mini_tree = dir_tree[:dir_num+1]
                dir_path = ""
                for part in mini_tree:
                    dir_path += part + "/"
                if dir_path in dir_sizes:
                    dir_sizes[dir_path] += file_size
                else:
                    dir_sizes[dir_path] = file_size

    combined_size = 0
    for dir_name in dir_sizes.keys():
        size = dir_sizes[dir_name]
        if size <= 100000:
            combined_size += size
    print(f"answer is {combined_size}")


if __name__ == "__main__":
    main()
