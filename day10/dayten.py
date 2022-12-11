def day_ten_part_one():
    with open("dayten.txt") as f:
        lines = f.read().split("\n")
        cycle = 0
        x = 1
        sum = 0
        register = 20
        signal_strengths = []
        for instruction in lines:
            # ADD
            if instruction.startswith("addx"):
                cycle += 1
                signal_strengths.append(x)
                cycle += 1
                x += int(instruction.split(" ")[1])
                signal_strengths.append(x)
            # NONE
            else:
                cycle += 1
                signal_strengths.append(x)
        while register <= 220:
            sum += register * signal_strengths[register - 2]
            register += 40

    return sum


def day_ten_part_two():
    with open("dayten.txt") as f:
        lines = f.read().split("\n")
        cycle = 1
        x = 1
        index = 0
        pixels = ""
        for instruction in lines:
            if x - 1 <= index <= x + 1:
                pixels += "█"
            else:
                pixels += " "
            if index < 39:
                index += 1
            else:
                index -= 39
            if index == 0:
                pixels += "\n"
            cycle += 1

            if instruction.startswith("addx"):
                if x - 1 <= index <= x + 1:
                    pixels += "█"
                else:
                    pixels += " "
                if index < 39:
                    index += 1
                else:
                    index -= 39
                if index == 0:
                    pixels += "\n"
                cycle += 1
                x += int(instruction.split(" ")[1])
        return pixels


if __name__ == '__main__':
    print("Day Ten - Part One: " + str(day_ten_part_one()))
    print("Day Ten - Part Two: \n" + day_ten_part_two())
