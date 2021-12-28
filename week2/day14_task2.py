import numpy as np

total_steps = 40
max_calc_steps = 20
repetitions = total_steps // max_calc_steps

raw_data = open("input_day14.txt", "r").read().split("\n\n")
chain = raw_data[0]
mappings = {opt[0]: opt[1] for opt in [d.split(" -> ") for d in raw_data[1].split("\n")]}
shackles = np.unique(np.array([opt[0] for opt in [d.split(" -> ") for d in raw_data[1].split("\n")]]))

print("calculating reference chains and histograms")
predictions = {}
histograms = {}
for sh in shackles:
    hist = {}
    starting_chain = sh
    for n in range(max_calc_steps):
        n_chain = starting_chain[0]
        for i in range(1, len(starting_chain)):
            n_chain += mappings[starting_chain[i - 1:i + 1]] + starting_chain[i]
        starting_chain = n_chain
    predictions[sh] = starting_chain

    unique_elements, counts = np.unique(np.array(list(starting_chain[1:])), return_counts=True)
    for u in range(len(unique_elements)):
        element = unique_elements[u]
        hist[element] = counts[u]
    histograms[sh] = hist

    if len(predictions) % 10 == 0:
        print(len(predictions) / (len(shackles)) * 100, "%")

print("calculating combined histogram")
final_histogram = {chain[0]: 1}
for st in range(len(chain) - 1):
    key = chain[st:st+2]
    for p in range(len(predictions[key]) - 1):
        if p % 100 == 0:
            print((p / len(predictions[key])) * (100 / (len(chain) - 1)) + ((st / len(chain)) * 100), "%")

        pr = predictions[key][p:p+2]
        p_hist = histograms[pr]
        for k in p_hist.keys():
            if k in final_histogram:
                final_histogram[k] += p_hist[k]
            else:
                final_histogram[k] = p_hist[k]

occurrence = [final_histogram[ky] for ky in final_histogram.keys()]
result = np.max(occurrence) - np.min(occurrence)
print("final result:", result)
