from collections import defaultdict


# PARSER
def tree(lines):
    curr, sizes = "", defaultdict(int)
    for line in lines:
        match line.split():
            # BACKWARDS
            case ("$", "cd", ".."):
                curr = curr[: curr.rindex("/") if "/" in curr else 0]
            # ADDS TO PATH
            case ("$", "cd", path):
                curr = f"{curr}/{path}" if curr else path
            # / AS ""
            case ("$", "cd", "/"):
                curr = ""
            # FILES
            case (size, *_):
                # GETS SIZE ON LINE
                try:
                    size = int(size)
                except ValueError as _:
                    continue
                path = curr
                while True:
                    sizes[path] += size
                    if not path:
                        break
                    path = path[: path.rindex("/") if "/" in path else 0]
    return sizes


def day_seven_part_one():
    with open("dayseven.txt") as f:
        lines = f.read().split("\n")
        a = tree(lines)
        return sum(size for size in a.values() if size <= 100000)


def day_seven_part_two():
    with open("dayseven.txt") as f:
        lines = f.read().split("\n")
        a = tree(lines)
        total = a[""]
        for size in sorted(a.values()):
            if 70000000 - (total - size) >= 30000000:
                return size


if __name__ == '__main__':
    print("Day Seven - Part One: " + str(day_seven_part_one()))
    print("Day Seven - Part Two: " + str(day_seven_part_two()))
