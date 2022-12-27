import os
import re
import numpy as np

from pathlib import Path


def main():
    parent = Path(__file__).parent.resolve()
    txt = "input_day11.txt"
    path = os.path.join(parent, txt)
    with open(path) as file:
        raw_data = file.read().split("\n")

    monkeys = []
    for line in raw_data:
        if line.split(" ")[0] == "Monkey":
            monkeys.append({})
        else:
            prop = re.findall("[A-Za-z]+:", line)
            if len(prop) > 0:
                prop = prop[0][:-1]
                if prop == 'Operation':
                    value = re.findall(":.+", line)[0][2:]
                elif prop == 'items':
                    value = [np.int64(num) for num in re.findall("[0-9]+", line)]
                else:
                    value = int(re.findall("[0-9]+", line)[0])
                monkeys[-1][prop] = value

    divisors = []
    for monkey in monkeys:
        monkey['inspections'] = 0
        divisors.append(monkey['Test'])
    lcm = np.lcm.reduce(divisors)

    for i in range(10000):
        if i % 2000 == 0:
            print(f"round {i}")
        for monkey in monkeys:
            while len(monkey['items']) > 0:
                old = monkey['items'][0]
                new = eval(monkey['Operation'][6:])
                if new >= lcm:
                    new = new % lcm
                if new % monkey['Test'] == 0:
                    monkeys[monkey['true']]['items'].append(new)
                else:
                    monkeys[monkey['false']]['items'].append(new)
                monkey['items'].pop(0)
                monkey['inspections'] += 1

    inspections = []
    for monkey in monkeys:
        inspections.append(monkey['inspections'])
    inspections = sorted(inspections)
    monkey_business = inspections[-2]*inspections[-1]

    print(f"answer is {monkey_business}")


if __name__ == "__main__":
    main()
