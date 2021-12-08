import numpy as np

nums = np.loadtxt("input_day1.txt", delimiter="\n")
prev = nums[0]
counter = 0
for num in nums[1:]:
    if num > prev:
        counter += 1
    prev = num
print(counter)
