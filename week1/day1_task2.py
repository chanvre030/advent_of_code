import numpy as np

nums = np.loadtxt("input_day1.txt", delimiter="\n")
last_three = np.array([nums[0], nums[1], nums[2]])
prev_total = np.sum(last_three)
counter = 0
for num in nums[3:]:
    current_three = np.append(last_three[1:], num)
    current_total = np.sum(current_three)
    if current_total > prev_total:
        counter += 1
    last_three = current_three
    prev_total = current_total
print(counter)
