import numpy as np

raw_data = open("input_day14.txt", "r").read().split("\n\n")
options = {opt[0]: opt[1] for opt in [d.split(" -> ") for d in raw_data[1].split("\n")]}
chain = raw_data[0]
for n in range(10):
    new_chain = chain[0]
    for i in range(1, len(chain)):
        if chain[i-1:i+1] in options:
            new_chain += options[chain[i-1:i+1]]+chain[i]
        else:
            print("kadook")
            new_chain += chain[i]
    chain = new_chain
chain = np.array(list(chain))
unique, counts = np.unique(chain, return_counts=True)
result = np.max(counts) - np.min(counts)
print("final result:", result)
