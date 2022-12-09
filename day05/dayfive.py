class Move:
    def __init__(self, num, fro, to):
        self.num = num
        self.fro = fro
        self.to = to


class Input:
    def __init__(self, stacks, moves):
        self.stacks = stacks
        self.moves = moves


# PARSER
def get_input():
    with open("dayfive.txt") as f:
        lines = f.readlines()
        num_line = 0
        not_found = False
        while not lines[num_line][1].isdigit():
            num_line += 1
        stack_height = num_line
        num_line = lines[num_line].strip()
        num_stacks = int(num_line[len(num_line) - 1])
        stacks = []
        stack = 1

        # STACKS
        while stack < (num_stacks * 4):
            l = []
            for i in range(int(stack_height)):
                if len(lines[i]) > stack and lines[i][stack] != " ":
                    l.append(lines[i][stack])
            stacks.append(l)
            stack += 4

        # MOVES
        moves = []
        start = stack_height + 2
        while start < len(lines):
            cur_line = lines[start]
            num_line = ""
            for b in range(len(cur_line)):
                if (cur_line[b].isdigit()) or (cur_line[b] == " "):
                    num_line += cur_line[b]
            num_line = num_line.lstrip()
            nums = num_line.split("  ")
            move = Move(int(nums[0]), int(nums[1]), int(nums[2]))
            moves.append(move)
            start += 1
        return Input(stacks, moves)


def day_five_part_one(input):
    stacks = input.stacks
    for m in input.moves:
        receiver = m.to - 1
        gives = m.fro - 1
        for i in range(m.num):
            item = stacks[gives][0]
            stacks[gives].pop(0)
            stacks[receiver].insert(0, item)
    answer = ""
    for i in stacks:
        answer += i[0]
    return answer


def day_five_part_two(input):
    stacks = input.stacks
    for m in input.moves:
        receiver = m.to - 1
        gives = m.fro - 1
        temp = []
        for i in range(m.num):
            item = stacks[gives][0]
            stacks[gives].pop(0)
            temp.append(item)
        stacks[receiver] = temp + stacks[receiver]
    answer = ""
    for i in stacks:
        answer += i[0]
    return answer


if __name__ == '__main__':
    print("Day Five - Part One: " + str(day_five_part_one(get_input())))
    print("Day Five - Part Two: " + str(day_five_part_two(get_input())))
