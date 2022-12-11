class Monkey:
    def __init__(self, items, operation, divisible, true, false, inspections):
        self.items = items
        self.operation = operation
        self.divisible = divisible
        self.true = true
        self.false = false
        self.inspections = inspections


# Monkey parser
def get_input():
    with open("dayeleven.txt") as f:
        monkeys = []
        lines = f.read().split("\n")
        for i in range(len(lines) - 1):
            line = lines[i]
            if line.startswith("Monkey"):
                items = [eval(i) for i in lines[i + 1].lstrip().removeprefix("Starting items: ").split(",")]
                operation = lines[i + 2].lstrip().removeprefix("Operation: new = ")
                divisible = int(lines[i + 3].lstrip().removeprefix("Test: divisible by "))
                true = int(lines[i + 4][-1])
                false = int(lines[i + 5][-1])
                monkeys.append(Monkey(items, operation, divisible, true, false, 0))
        return monkeys


def day_eleven_part_one():
    monkeys = get_input()
    # 20 rounds
    for a in range(20):
        index = 0
        for monkey in monkeys:
            for item in monkey.items:
                worry = item
                monkey.inspections += 1
                # Parse operation (old (+ or *) (n or old))
                op_l = monkey.operation.split(" ")
                if op_l[1] == "*":
                    if op_l[2] == "old":
                        worry *= worry
                    else:
                        v = int(op_l[2])
                        worry *= v
                else:
                    if op_l[2] == "old":
                        worry += worry
                    else:
                        v = int(op_l[2])
                        worry += v
                # Bored
                worry = int(worry / 3)
                # Check divisible
                if worry % monkey.divisible == 0:
                    # Give to monkey in true
                    monkeys[monkey.true].items.append(worry)
                else:
                    # Give to monkey in false
                    monkeys[monkey.false].items.append(worry)
                # Remove item from this monkey
            monkey.items = []
            index += 1

    ins = []
    for m in monkeys:
        ins.append(m.inspections)

    m_f = max(ins)
    ins.remove(m_f)
    m_s = max(ins)
    monkey_business = m_f * m_s
    return monkey_business


# TODO: Find a way to keep the values manage-able without losing info because this will probably run out of memory
#  before it ends
def day_eleven_part_two():
    monkeys = get_input()
    # 20 rounds
    for a in range(10000):
        index = 0
        for monkey in monkeys:
            for item in monkey.items:
                worry = item
                monkey.inspections += 1
                # Parse operation (old (+ or *) (n or old))
                op_l = monkey.operation.split(" ")
                if op_l[1] == "*":
                    if op_l[2] == "old":
                        worry *= worry
                    else:
                        v = int(op_l[2])
                        worry *= v
                else:
                    if op_l[2] == "old":
                        worry += worry
                    else:
                        v = int(op_l[2])
                        worry += v
                # Bored
                # worry = int(worry / 3)
                # Check divisible
                if worry % monkey.divisible == 0:
                    # Give to monkey in true
                    monkeys[monkey.true].items.append(worry)
                else:
                    # Give to monkey in false
                    monkeys[monkey.false].items.append(worry)
                # Remove item from this monkey
            monkey.items = []
            index += 1

    ins = []
    for m in monkeys:
        ins.append(m.inspections)

    m_f = max(ins)
    ins.remove(m_f)
    m_s = max(ins)
    monkey_business = m_f * m_s
    return monkey_business


if __name__ == '__main__':
    print("Day Eleven - Part One: " + str(day_eleven_part_one()))
    print("Day Eleven - Part Two: " + str(day_eleven_part_two()))
