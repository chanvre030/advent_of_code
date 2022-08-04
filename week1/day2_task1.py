import numpy as np
import os

from pathlib import Path


def main():
    h_pos = 0
    v_pos = 0

    parent = Path(__file__).parent.resolve()
    txt = "input_day2.txt"
    path = os.path.join(parent, txt)
    commands = np.loadtxt(path, dtype=str, delimiter="\n")
    for command in commands:
        command = command.split()
        direction = command[0]
        magnitude = int(command[1])
        if direction == "forward":
            h_pos += magnitude
        elif direction == "down":
            v_pos += magnitude
        elif direction == "up":
            v_pos -= magnitude
        else:
            print("something wrong with the command:", command)

    print("\n horizontal postion:", h_pos, "\n vertical position:", v_pos)
    multiplication = h_pos * v_pos
    print("multiplication result:", multiplication)


if __name__ == "__main__":
    main()
