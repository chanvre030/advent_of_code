from pathlib import Path


def main():
    parent = Path(__file__).parent.resolve()
    txt = "input_day1.txt"
    path = parent / txt
    nums = "0123456789"
    with open(path) as file:
        raw_data = file.read()
    calibration_total = 0
    split_data = raw_data.split("\n")
    for data_list in split_data:
        found_nums = []
        for char in data_list:
            if char in nums:
                found_nums.append(char)
        calibration_total += int(found_nums[0] + found_nums[-1])

    print(f"answer is {calibration_total}")


if __name__ == "__main__":
    main()
