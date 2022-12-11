def day_nine_part_one():
    with open("daynine.txt") as f:
        lines = f.read().split("\n")
        return simulation(lines, 2)


def day_nine_part_two():
    with open("daynine.txt") as f:
        lines = f.read().split("\n")
        return simulation(lines, 10)


def simulation(data, knots):
    directions = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
    rope = [(0, 0)] * knots

    positions = set()
    positions.add(rope[-1])

    for line in data:
        dir, n = line.split()

        for _ in range(int(n)):
            rope[0] = (rope[0][0] + directions[dir][0], rope[0][1] + directions[dir][1])

            for i in range(knots - 1):
                w = rope[i][0] - rope[i + 1][0]
                h = rope[i][1] - rope[i + 1][1]
                dx, dy = 0, 0
                if abs(w) == 2 or abs(h) == 2:
                    if w == 0:
                        dx = 0
                    else:
                        if w > 0:
                            dx = 1
                        else:
                            dx = -1

                    if h == 0:
                        dy = 0
                    else:
                        if h > 0:
                            dy = 1
                        else:
                            dy = -1
                if dx or dy:
                    rope[i + 1] = (rope[i + 1][0] + dx, rope[i + 1][1] + dy)
            positions.add(rope[-1])
    return len(positions)


if __name__ == '__main__':
    print("Day Nine - Part One: " + str(day_nine_part_one()))
    print("Day Nine - Part Two: " + str(day_nine_part_two()))
