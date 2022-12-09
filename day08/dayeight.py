def day_eight_part_one():
    with open("dayeight.txt") as f:
        sum = 0
        lines = f.read().split()
        rows = len(lines) - 1
        columns = len(lines[0]) - 1
        sum += columns * 2 + rows * 2
        for i in range(1, rows, 1):
            for a in range(1, columns, 1):
                pos_x = a
                pos_y = i
                item = lines[i][a]
                # CHEK LEFT
                if lines[i][0:pos_x + 1].count(item) == 1 and max(lines[i][0:pos_x + 1]) == item:
                    sum += 1
                    continue
                # CHECK RIGHT
                if lines[i][pos_x:rows + 1].count(item) == 1 and max(lines[i][pos_x:rows + 1]) == item:
                    sum += 1
                    continue
                # CHECK TOP
                top = []
                for y in range(0, pos_y + 1, 1):
                    top.append(lines[y][pos_x])

                if top.count(item) == 1 and max(top) == item:
                    sum += 1
                    continue
                # CHECK BOTTOM
                bottom = []
                for y in range(pos_y, columns + 1, 1):
                    bottom.append(lines[y][pos_x])

                if bottom.count(item) == 1 and max(bottom) == item:
                    sum += 1
                    continue
        return sum


def day_eight_part_two():
    with open("dayeight.txt") as f:
        considerations = []
        lines = f.read().split()
        rows = len(lines)
        columns = len(lines[0])
        for i in range(0, rows, 1):
            for a in range(0, columns, 1):
                view = 1
                pos_x = a
                pos_y = i
                item = lines[i][a]
                # CHECK LEFT
                sumL = 0
                if pos_x != 0:
                    sumL = 0
                    view = True
                    index = pos_x - 1
                    while view:
                        sumL += 1
                        if lines[pos_y][index] >= item or index == 0:
                            view = False
                        index -= 1
                # CHECK RIGHT
                sumR = 0
                if pos_x != (columns-1):
                    sumR = 0
                    view = True
                    index = pos_x + 1
                    while view:
                        sumR += 1
                        if lines[pos_y][index] >= item or index == columns-1:
                            view = False
                        index += 1
                # CHECK TOP
                sumT = 0
                if pos_y != 0:
                    sumT = 0
                    view = True
                    index = pos_y - 1
                    while view:
                        sumT += 1
                        if lines[index][pos_x] >= item or index == 0:
                            view = False
                        index -= 1
                # CHECK BOTTOM
                sumB = 0
                if pos_y != rows-1:
                    sumB = 0
                    view = True
                    index = pos_y + 1
                    while view:
                        sumB += 1
                        if lines[index][pos_x] >= item or index == rows-1:
                            view = False
                        index += 1
                view = sumL * sumR * sumT * sumB
                considerations.append(view)
        return max(considerations)




if __name__ == '__main__':
    print("Day Eight - Part One: " + str(day_eight_part_one()))
    print("Day Eight - Part Two: " + str(day_eight_part_two()))
