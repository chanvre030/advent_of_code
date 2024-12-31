from pathlib import Path


def check_adjacent(data, lid, cid, direction):
    found = False
    if direction == 1 and lid - 3 >= 0 and cid - 3 >= 0:
        m_okay = data[lid - 1][cid - 1] == "M"
        a_okay = data[lid - 2][cid - 2] == "A"
        s_okay = data[lid - 3][cid - 3] == "S"
        found = m_okay and a_okay and s_okay
    if direction == 2 and lid - 3 >= 0:
        m_okay = data[lid - 1][cid] == "M"
        a_okay = data[lid - 2][cid] == "A"
        s_okay = data[lid - 3][cid] == "S"
        found = m_okay and a_okay and s_okay
    if direction == 3 and lid - 3 >= 0 and cid + 3 <= len(data[lid]) - 1:
        m_okay = data[lid - 1][cid + 1] == "M"
        a_okay = data[lid - 2][cid + 2] == "A"
        s_okay = data[lid - 3][cid + 3] == "S"
        found = m_okay and a_okay and s_okay
    if direction == 4 and cid - 3 >= 0:
        m_okay = data[lid][cid - 1] == "M"
        a_okay = data[lid][cid - 2] == "A"
        s_okay = data[lid][cid - 3] == "S"
        found = m_okay and a_okay and s_okay
    if direction == 6 and cid + 3 <= len(data[lid]) - 1:
        m_okay = data[lid][cid + 1] == "M"
        a_okay = data[lid][cid + 2] == "A"
        s_okay = data[lid][cid + 3] == "S"
        found = m_okay and a_okay and s_okay
    if direction == 7 and lid + 3 <= len(data) - 1 and cid - 3 >= 0:
        m_okay = data[lid + 1][cid - 1] == "M"
        a_okay = data[lid + 2][cid - 2] == "A"
        s_okay = data[lid + 3][cid - 3] == "S"
        found = m_okay and a_okay and s_okay
    if direction == 8 and lid + 3 <= len(data) - 1:
        m_okay = data[lid + 1][cid] == "M"
        a_okay = data[lid + 2][cid] == "A"
        s_okay = data[lid + 3][cid] == "S"
        found = m_okay and a_okay and s_okay
    if direction == 9 and lid + 3 <= len(data) - 1 and cid + 3 <= len(data[lid]) - 1:
        m_okay = data[lid + 1][cid + 1] == "M"
        a_okay = data[lid + 2][cid + 2] == "A"
        s_okay = data[lid + 3][cid + 3] == "S"
        found = m_okay and a_okay and s_okay
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
            if char == "X":
                for direction in [1, 2, 3, 4, 6, 7, 8, 9]:
                    found = check_adjacent(data, lid, cid, direction)
                    finds += int(found)

    print(f"answer: {finds}")


if __name__ == "__main__":
    main()
