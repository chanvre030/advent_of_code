import os

from pathlib import Path


def check_signal_strength(a, b, cnt):
    n_min = 20
    n_step = 40
    if a % n_step == n_min:
        cnt += a*b
    return cnt


def main():
    parent = Path(__file__).parent.resolve()
    txt = "input_day10.txt"
    path = os.path.join(parent, txt)
    with open(path) as file:
        raw_data = file.read().split("\n")
    data = [line.split(" ") for line in raw_data]

    signal = 0
    c = 0
    x = 1
    for instruction in data:
        instr_len = len(instruction)
        if instr_len == 1:
            c += 1
            signal = check_signal_strength(c, x, signal)
        elif instr_len == 2:
            for i in range(2):
                c += 1
                signal = check_signal_strength(c, x, signal)
            x += int(instruction[1])
    print(f"answer is {signal}")


if __name__ == "__main__":
    main()
