def get_input():
    with open("daysix.txt") as f:
        return f.readline().rstrip()


def day_six_part_one(input):
    answer = 0
    for i in range(len(input) - 4):
        test = input[i:i+4]
        if len(set(test)) == len(test):
            answer += 4
            return answer
        else:
            answer += 1


def day_six_part_two(input):
    answer = 0
    for i in range(len(input) - 14):
        test = input[i:i+14]
        if len(set(test)) == len(test):
            answer += 14
            return answer
        else:
            answer += 1


if __name__ == '__main__':
    print("Day Six - Part One: " + str(day_six_part_one(get_input())))
    print("Day Six - Part Two: " + str(day_six_part_two(get_input())))
