import os
import numpy as np

from pathlib import Path


def update_display(a, b, disp):
    disp_len = 40
    sprite_size = 3
    check = (a-1) % disp_len
    if check+1 in range(b, b+sprite_size):
        disp += "#"
    else:
        disp += " "
    return disp


def main():
    parent = Path(__file__).parent.resolve()
    txt = "input_day10.txt"
    path = os.path.join(parent, txt)
    with open(path) as file:
        raw_data = file.read().split("\n")
    data = [line.split(" ") for line in raw_data]

    display = ""
    c = 0
    x = 1
    for instruction in data:
        instr_len = len(instruction)
        if instr_len == 1:
            c += 1
            display = update_display(c, x, display)
        elif instr_len == 2:
            for i in range(2):
                c += 1
                display = update_display(c, x, display)
            x += int(instruction[1])

    display = np.reshape(np.array([pix for pix in display]), (-1, 40))
    output = "output_day10.txt"
    np.savetxt(output, display, fmt="%c")
    print(f"for answer see [{output}]")


if __name__ == "__main__":
    main()
