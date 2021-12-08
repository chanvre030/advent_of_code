import re
data = re.split('[\n|]', open("input_day8.txt", "r").read())
filtered = [y for x in (data[i].split(" ") for i in range(1, len(data), 2)) for y in x]
usable = len([w for w in filtered if len(w) == 2 or len(w) == 3 or len(w) == 4 or len(w) == 7])
print(usable)
