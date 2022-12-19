class Input:
    def __init__(self, sensors, beacons):
        self.sensors = sensors
        self.beacons = beacons


def get_manhattan_distance(s, e):
    return abs(s[0] - e[0]) + abs(s[1] - e[1])


def get_input():
    with open("dayfifteen.txt") as f:
        lines = f.read().split("\n")
        sensors = []
        beacons = []
        for line in lines:
            line = line.split(" ")
            sx = int(line[2].split("=")[1].removesuffix(","))
            sy = int(line[3].split("=")[1].removesuffix(":"))
            bx = int(line[8].split("=")[1].removesuffix(","))
            by = int(line[9].split("=")[1])
            sensors.append((sx, sy))
            beacons.append((bx, by))
        return Input(sensors, beacons)


def day_fifteen_part_one(input):
    sensors = input.sensors
    beacons = input.beacons
    dists = []
    intervals = []
    has_beacon_x = []
    for i in range(len(sensors)):
        dists.append(get_manhattan_distance(sensors[i], beacons[i]))

    for i, s in enumerate(sensors):
        dx = dists[i] - abs(s[1] - 2000000)

        if dx <= 0:
            continue

        intervals.append((s[0] - dx, s[0] + dx))

    for bx, by in beacons:
        if by == 2000000:
            has_beacon_x.append(bx)

    min_x = min([i[0] for i in intervals])
    max_x = max([i[1] for i in intervals])

    answer = 0
    for x in range(min_x, max_x + 1):
        if x in has_beacon_x:
            continue

        for l, r in intervals:
            if l <= x <= r:
                answer += 1
                break

    return answer


def day_fifteen_part_two(input):
    pass


if __name__ == '__main__':
    print("Day Fifteen - Part One: " + str(day_fifteen_part_one(get_input())))
    print("Day Fifteen - Part Two: " + str(day_fifteen_part_two(get_input())))
