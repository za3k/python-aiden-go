
def get_move() -> tuple[int, int] | str:
    move_row  = input('Enter row or PASS:')
    if move_row == 'PASS':
        return 'PASS'
    move_column = input ('Enter column:')
    move = (int(move_row), int(move_column))
    return move


def play_move():
    pass

def main():
    board = [['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-']]
    black_to_play = True
    move = get_move()
    print(repr(move))


if __name__ == "__main__":
    main()