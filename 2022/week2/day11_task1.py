import os
import re

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
                    value = [int(num) for num in re.findall("[0-9]+", line)]
                else:
                    value = int(re.findall("[0-9]+", line)[0])
                monkeys[-1][prop] = value

    for monkey in monkeys:
        monkey['inspections'] = 0

    for i in range(20):
        for monkey in monkeys:
            while len(monkey['items']) > 0:
                old = monkey['items'][0]
                new = eval(monkey['Operation'][6:])
                new = new//3
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
