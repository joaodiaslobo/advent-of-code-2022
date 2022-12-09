def day_nine_part_one():
    with open("daynine.txt") as f:
        lines = f.read().split("\n")
        head = (0, 0)
        tail = (0, 0)
        visits = [tail]
        for m in lines:
            p = m.split()
            move = p[0]
            units = int(p[1])
            if move == "R":
                for i in range(units):
                    head = (head[0] + 1, head[1])
                    if tail[0] < head[0] - 1:
                        tail = (tail[0] + 1, head[1])
                    visits.append(tail)
            elif move == "U":
                for i in range(units):
                    head = (head[0], head[1] + 1)
                    if tail[1] < head[1] - 1:
                        tail = (head[0], tail[1] + 1)
                    visits.append(tail)
            elif move == "L":
                for i in range(units):
                    head = (head[0] - 1, head[1])
                    if tail[0] > head[0] + 1:
                        tail = (tail[0] - 1, head[1])
                    visits.append(tail)
            elif move == "D":
                for i in range(units):
                    head = (head[0], head[1] - 1)
                    if tail[1] > head[1] + 1:
                        tail = (head[0], tail[1] - 1)
                    visits.append(tail)
        return len(set(visits))


def day_nine_part_two():
    pass


if __name__ == '__main__':
    print("Day Nine - Part One: " + str(day_nine_part_one()))
    print("Day Nine - Part Two: " + str(day_nine_part_two()))
