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


def process_one_message(msgs, version_sum):
    msg = msgs[-1]
    print(f"binary: {msg}")
    msg, v, t = get_version_and_type(msg)
    print(f"version: {v} \ntype: {t}")
    version_sum += v
    if t == 4:
        stop = False
        while not stop:
            group = msg[0:5]
            print("group:", group)
            msg = msg[5:]
            if group[0] == "0":
                stop = True
        msgs[-1] = msg
    else:
        msg, length_type = get_len_type(msg)
        print(f"length type: {length_type}")
        if length_type == "0":
            msg, packet_len = get_len(msg)
            print(f"packet length: {packet_len}")
            sub_msg = msg[:packet_len]
            msgs = msgs[:-1]
            msgs.extend([sub_msg, msg[packet_len:]])        # weird order, but needed for the recursion later on
        elif length_type == "1":
            msg, subpacket_num = get_num(msg)
            sub_msgs = [msg]
            print(f"subpacket num: {subpacket_num}")
            for i in range(subpacket_num):
                print(f"\nsubpacket {i}")
                sub_msgs, version_sum = process_one_message(sub_msgs, version_sum)
            msgs = msgs[:-1]
            print(msgs, sub_msgs)
            msgs.extend(sub_msgs)
    return msgs, version_sum


data = open("input_day16.txt", "r").read()
data_list = [f"{int(data, base=16):0>{len(data)*4}b}"]                         # hex to binary with some witchery

answer = 0
while data_list:
    print("\ndatalist:", data_list)
    if "1" in data_list[-1]:
        data_list, answer = process_one_message(data_list, answer)
    else:
        data_list.pop(-1)

print(f"\nfinal answer: {answer}")
