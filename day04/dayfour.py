def day_four_part_one():
    with open("dayfour.txt") as f:
        answer = 0
        for i in f.readlines():
            pairs = i.rstrip().split(",")
            f_elf = pairs[0].split("-")
            f_elf_s = int(f_elf[0])
            f_elf_e = int(f_elf[1]) + 1
            s_elf = pairs[1].split("-")
            s_elf_s = int(s_elf[0])
            s_elf_e = int(s_elf[1]) + 1
            first_elf = [*range(f_elf_s, f_elf_e, 1)]
            second_elf = [*range(s_elf_s, s_elf_e, 1)]
            if all(item in first_elf for item in second_elf) or all(item in second_elf for item in first_elf):
                answer += 1
    return answer


def day_four_part_two():
    with open("dayfour.txt") as f:
        answer = 0
        for i in f.readlines():
            pairs = i.rstrip().split(",")
            f_elf = pairs[0].split("-")
            f_elf_s = int(f_elf[0])
            f_elf_e = int(f_elf[1]) + 1
            s_elf = pairs[1].split("-")
            s_elf_s = int(s_elf[0])
            s_elf_e = int(s_elf[1]) + 1
            first_elf = [*range(f_elf_s, f_elf_e, 1)]
            second_elf = [*range(s_elf_s, s_elf_e, 1)]
            if any(item in first_elf for item in second_elf):
                answer += 1
    return answer


if __name__ == '__main__':
    print("Day Four - Part One: " + str(day_four_part_one()))
    print("Day Four - Part Two: " + str(day_four_part_two()))
