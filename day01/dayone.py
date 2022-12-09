def day_one_part_one():
    with open("dayone.txt") as f:
        lines = f.readlines()
        calories = []
        csum = 0
        for i in lines:
            if i != "\n":
                csum += int(i)
            else:
                calories.append(csum)
                csum = 0
        return max(calories)


def day_one_part_two():
    with open("dayone.txt") as f:
        lines = f.readlines()
        calories = []
        csum = 0
        for i in lines:
            if i != "\n":
                csum += int(i)
            else:
                calories.append(csum)
                csum = 0
        answer = 0
        answer += max(calories)
        calories.remove(max(calories))
        answer += max(calories)
        calories.remove(max(calories))
        answer += max(calories)
        calories.remove(max(calories))

        return answer


if __name__ == '__main__':
    print("Day One - Part One: " + str(day_one_part_one()))
    print("Day One - Part Two: " + str(day_one_part_two()))
