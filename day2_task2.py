import numpy as np

h_pos = 0
v_pos = 0
aim = 0

commands = np.loadtxt("input_day2.txt", dtype=str, delimiter="\n")
for command in commands:
    command = command.split()
    direction = command[0]
    magnitude = int(command[1])
    if direction == "forward":
        h_pos += magnitude
        v_pos += aim * magnitude
    elif direction == "down":
        aim += magnitude
    elif direction == "up":
        aim -= magnitude
    else:
        print("something wrong with the command:", command)

print("\n horizontal postion:", h_pos, "\n vertical position:", v_pos)
multiplication = h_pos * v_pos
print("multiplication result:", multiplication)
