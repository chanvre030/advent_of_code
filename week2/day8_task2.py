import re
import os

from pathlib import Path


def main():
    parent = Path(__file__).parent.resolve()
    txt = "input_day8.txt"
    path = os.path.join(parent, txt)
    data = re.split(r'\n|\| ', open(path, "r").read())
    signal = [x for x in (data[i].split(" ") for i in range(0, len(data), 2))]
    output = [y for y in (data[i].split(" ") for i in range(1, len(data), 2))]
    final_answer = 0
    for pattern, display in zip(signal, output):
        mapping = {}
        while len(mapping) < 10:
            for word in pattern:
                if word not in mapping.values():
                    if len(word) == 2:
                        mapping[1] = word
                    elif len(word) == 3:
                        mapping[7] = word
                    elif len(word) == 4:
                        mapping[4] = word
                    elif len(word) == 7:
                        mapping[8] = word
                    elif len(word) == 5:
                        if 5 not in mapping:
                            if 1 in mapping:
                                one_seg_in_all = [sum(segment in w for w in pattern) for segment in mapping[1]]
                                one_seg_in_word = mapping[1][one_seg_in_all.index(min(one_seg_in_all))] not in word
                                if one_seg_in_word:
                                    mapping[5] = word
                        else:
                            if 1 in mapping:
                                if all([s in word for s in mapping[1]]):
                                    mapping[3] = word
                                else:
                                    mapping[2] = word
                    elif len(word) == 6:
                        if 1 in mapping:
                            if not all([s in word for s in mapping[1]]):
                                mapping[6] = word
                            elif 5 in mapping:
                                if all([s in word for s in mapping[5]]):
                                    mapping[9] = word
                                else:
                                    mapping[0] = word
        num = ""
        imap = dict((mapping[i], i) for i in mapping)
        for dgt in display:
            num += str(imap[list(imap.keys())[list(all(d in k and len(k) == len(dgt) for d in dgt) for k in imap).index(True)]])
        final_answer += int(num)
    print("final answer:", final_answer)


if __name__ == "__main__":
    main()
