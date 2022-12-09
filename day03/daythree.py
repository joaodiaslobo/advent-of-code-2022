def get_input():
    input = []
    with open("daythree.txt") as f:
        for i in f.readlines():
            input.append(i.rstrip())
    return input

def day_three_part_one(input):
    answer = 0
    for i in input:
        mid = int(len(i) / 2)
        first_compartment = i[:mid]
        second_compartment = i[mid:]
        intersection = list(set(first_compartment).intersection(second_compartment))
        shared_item = intersection[0]
        value = ord(shared_item)
        if value >= 97:
            value -= 96
        else:
            value -= 38
        answer += value

    return answer

def day_three_part_two(input):
    answer = 0
    index = 0
    while index < 300:
        f = input[index]
        s = input[index+1]
        t = input[index+2]
        intersection = list(set(list(set(f).intersection(s))).intersection((t)))
        shared_item = intersection[0]
        value = ord(shared_item)
        if value >= 97:
            value -= 96
        else:
            value -= 38
        answer += value
        index += 3
    return answer




if __name__ == '__main__':
    print("Day Three - Part One: " + str(day_three_part_one(get_input())))
    print("Day Three - Part Two: " + str(day_three_part_two(get_input())))