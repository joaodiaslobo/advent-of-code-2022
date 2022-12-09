class Input():
    def __init__(self, opponent, player):
        self.opponent = opponent
        self.player = player


def get_input():
    opponent_plays = []
    player_moves = []
    with open("daytwo.txt") as f:
        lines = f.readlines()
        for i in lines:
            a = i.rstrip().split(" ")
            if a[0] == "A":
                opponent_plays.append("1")
            elif a[0] == "B":
                opponent_plays.append("2")
            else:
                opponent_plays.append("3")

            if a[1] == "X":
                player_moves.append("1")
            elif a[1] == "Y":
                player_moves.append("2")
            else:
                player_moves.append("3")
        return Input(opponent_plays, player_moves)


def day_two_part_one(input):
    answer = 0
    for i in range(len(input.opponent)):
        op_play = input.opponent[i]
        p_play = input.player[i]
        score = 0
        if op_play == p_play:
            score = int(p_play) + 3
        if op_play == "1":
            if p_play == "2":
                score = 2 + 6
            elif p_play == "3":
                score = 3 + 0
        if op_play == "2":
            if p_play == "1":
                score = 1 + 0
            elif p_play == "3":
                score = 3 + 6
        if op_play == "3":
            if p_play == "1":
                score = 1 + 6
            elif p_play == "2":
                score = 2 + 0
        answer += score
    return answer


def day_two_part_two(input):
    answer = 0
    for i in range(len(input.opponent)):
        op_play = input.opponent[i]
        game_result = input.player[i]
        score = 0
        if game_result == "1":
            if op_play == "1":
                score = 3 + 0
            elif op_play == "2":
                score = 1 + 0
            else:
                score = 2 + 0
        elif game_result == "3":
            if op_play == "1":
                score = 2 + 6
            elif op_play == "2":
                score = 3 + 6
            else:
                score = 1 + 6
        else:
            score = 3 + int(op_play)
        answer += score
    return answer


if __name__ == '__main__':
    print("Day Two - Part One: " + str(day_two_part_one(get_input())))
    print("Day Two - Part Two: " + str(day_two_part_two(get_input())))
