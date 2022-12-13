import ast


def get_input(pair):
    with open("daythirteen.txt") as f:
        packets = []
        lines = f.read().split("\n")
        index = 0
        while index < len(lines):
            line = lines[index]
            if line.startswith("["):
                f = ast.literal_eval(line)
                s = ast.literal_eval(lines[index + 1])
                if pair:
                    packets.append((f, s))
                else:
                    packets.append(f)
                    packets.append(s)
                index += 1
            index += 1
        return packets


def day_thirteen_part_one(input):
    order = []
    cur_pair = 1
    for pair in input:
        small_order = []
        r = list_comparer(pair[0], pair[1])
        small_order.append(r)
        if small_order[0]:
            order.append(cur_pair)
        cur_pair += 1
    return sum(order)


def day_thirteen_part_two(input):
    ordered = []
    input.append([[2]])
    input.append([[6]])
    for packet in input:
        done = False
        index = 0
        while not done:
            if len(ordered) - 1 < index:
                ordered.append(packet)
                done = True
            else:
                check = ordered[index]
                r = list_comparer(packet, check)
                if r:
                    ordered.insert(index, packet)
                    done = True
            index += 1
    v1 = ordered.index([[2]]) + 1
    v2 = ordered.index([[6]]) + 1
    return v1 * v2


def list_comparer(l1, l2):
    order = []
    l_index = 0
    leave = False
    while len(order) == 0 and not leave:
        if len(l2) - 1 < l_index and len(l1) - 1 < l_index:
            leave = True
        elif len(l2) - 1 < l_index:
            order.append(False)
        elif len(l1) - 1 < l_index:
            order.append(True)
        elif isinstance(l1[l_index], int) and isinstance(l2[l_index], int):
            if len(l1) - 1 < l_index:
                order.append(False)
            elif l1[l_index] < l2[l_index]:
                order.append(True)
            elif l1[l_index] > l2[l_index]:
                order.append(False)
        elif isinstance(l1[l_index], list) and isinstance(l2[l_index], list):
            r = list_comparer(l1[l_index], l2[l_index])
            if r is not None:
                order.append(r)
        elif isinstance(l1[l_index], int) and isinstance(l2[l_index], list):
            l1_l = [l1[l_index]]
            r = list_comparer(l1_l, l2[l_index])
            if r is not None:
                order.append(r)
        elif isinstance(l1[l_index], list) and isinstance(l2[l_index], int):
            l2_l = [l2[l_index]]
            r = list_comparer(l1[l_index], l2_l)
            if r is not None:
                order.append(r)
        l_index += 1

    if len(order) == 0:
        return None
    return order[0]


if __name__ == '__main__':
    print("Day Thirteen - Part One: " + str(day_thirteen_part_one(get_input(True))))
    print("Day Thirteen - Part Two: " + str(day_thirteen_part_two(get_input(False))))
