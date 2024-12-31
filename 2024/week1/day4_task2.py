from pathlib import Path


def check_adjacent(data, lid, cid, direction):
    found = False
    position_ok = lid - 1 >= 0 and lid + 1 <= len(data) - 1 and cid - 1 >= 0 and cid + 1 <= len(data[lid]) - 1
    if position_ok:
        if direction == 1:
            m_okay = data[lid - 1][cid - 1] == "M" and data[lid - 1][cid + 1] == "M"
            s_okay = data[lid + 1][cid + 1] == "S" and data[lid + 1][cid - 1] == "S"
            found = m_okay and s_okay
        if direction == 3:
            m_okay = data[lid - 1][cid + 1] == "M" and data[lid + 1][cid + 1] == "M"
            s_okay = data[lid + 1][cid - 1] == "S" and data[lid - 1][cid - 1] == "S"
            found = m_okay and s_okay
        if direction == 7:
            m_okay = data[lid + 1][cid - 1] == "M" and data[lid - 1][cid - 1] == "M"
            s_okay = data[lid - 1][cid + 1] == "S" and data[lid + 1][cid + 1] == "S"
            found = m_okay and s_okay
        if direction == 9:
            m_okay = data[lid + 1][cid + 1] == "M" and data[lid + 1][cid - 1] == "M"
            s_okay = data[lid - 1][cid - 1] == "S" and data[lid - 1][cid + 1] == "S"
            found = m_okay and s_okay
    return found


def main():
    parent = Path(__file__).parent.resolve()
    txt = "input_day4.txt"
    path = parent / txt

    with open(path) as file:
        raw_data = file.read()
    data = raw_data.splitlines()

    finds = 0

    for lid, line in enumerate(data):
        for cid, char in enumerate(line):
            if char == "A":
                for direction in [1, 3, 7, 9]:
                    found = check_adjacent(data, lid, cid, direction)
                    finds += int(found)

    print(f"answer: {finds}")


if __name__ == "__main__":
    main()
