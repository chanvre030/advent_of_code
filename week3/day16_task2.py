def get_version_and_type(packet):
    version_bin = packet[0:3]
    version_dec = int(version_bin, base=2)
    type_bin = packet[3:6]
    type_dec = int(type_bin, base=2)
    packet = packet[6:]
    return packet, version_dec, type_dec


def get_len_type(packet):
    len_type = packet[0]
    packet = packet[1:]
    return packet, len_type


def get_len(packet):
    packet_len_bin = packet[0:15]
    packet_len_dec = int(packet_len_bin, base=2)
    packet = packet[15:]
    return packet, packet_len_dec


def get_num(packet):
    packet_num_bin = packet[0:11]
    packet_num_dec = int(packet_num_bin, base=2)
    packet = packet[11:]
    return packet, packet_num_dec


def type_4(packet):
    val_bin = ""
    stop = False
    while not stop:
        group = packet[:5]
        val_bin += group[1:5]
        packet = packet[5:]
        if group[0] == "0":
            stop = True
    val_dec = int(val_bin, base=2)
    return packet, val_dec


def process_one_message(msg):
    type_dict = {0: "sum", 1: "product", 2: "min", 3: "max", 4: "value", 5: ">", 6: "<", 7: "=="}
    value = None
    sub_values = []
    print(f"binary: {msg}")
    msg, v, t = get_version_and_type(msg)
    print(f"version: {v} \ntype: {t}")
    if t == 4:
        msg, value = type_4(msg)
        print(f"value: {value}")
    else:
        msg, length_type = get_len_type(msg)
        print(f"length type: {length_type}")
        if length_type == "0":
            msg, packet_len = get_len(msg)
            print(f"packet length: {packet_len}")
            sub_msg = msg[:packet_len]
            msg = msg[packet_len:]
            while sub_msg:
                print(f"\nsubpacket")
                sub_msg, sub_val = process_one_message(sub_msg)
                sub_values.append(sub_val)
            print(f"\n{type_dict[t]} of: {sub_values}\n")
        elif length_type == "1":
            msg, subpacket_num = get_num(msg)
            print(f"subpacket num: {subpacket_num}")
            for i in range(subpacket_num):
                print(f"\nsubpacket {i}")
                msg, sub_val = process_one_message(msg)
                sub_values.append(sub_val)
            print(f"\n{type_dict[t]} of: {sub_values}\n")
        if t == 0:
            value = sum(sub_values)
        elif t == 1:
            value = 1
            for sv in sub_values:
                value *= sv
        elif t == 2:
            value = min(sub_values)
        elif t == 3:
            value = max(sub_values)
        elif t == 5:
            value = int(sub_values[0] > sub_values[1])
        elif t == 6:
            value = int(sub_values[0] < sub_values[1])
        elif t == 7:
            value = int(sub_values[0] == sub_values[1])
    return msg, value


data = open("input_day16.txt", "r").read()
data = f"{int(data, base=16):0>{len(data)*4}b}"                    # hex to binary with some witchery

answer = None
while "1" in data:
    data, answer = process_one_message(data)

print(f"\nfinal answer: {answer}")
