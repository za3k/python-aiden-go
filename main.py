SIZE = 5

def get_move() -> tuple[int, int] | str:
    move_row  = input('Enter row or PASS:')
    if move_row == 'PASS':
        return 'PASS'
    move_column = input ('Enter column:')
    move = (int(move_row), int(move_column))
    return move


def print_row(row: list[str]) -> None :
    print('{} {} {} {} {}'.format(row[0], row[1], row[2], row[3], row[4]))


def make_empty_board() -> list[list[str]]:
    return [['‧','‧','‧','‧','‧'],['‧','‧','‧','‧','‧'],['‧','‧','‧','‧','‧'],['‧','‧','‧','‧','‧'],['‧','‧','‧','‧','‧']]


def print_board(board: list[list[str]]) -> None:
    for i in range(SIZE):
        print_row(board[i])

#‧ ‧ ‧ ‧ ‧
#‧ ‧ ‧ ⬤ ◯
#‧ ‧ ‧ ‧ ‧
#‧ ‧ ‧ ‧ ‧
#‧ ‧ ‧ ‧ ‧


def play_move():
    pass

def main():
    board = make_empty_board()
    black_to_play = True
    print_board(board)
    move = get_move()
    print(repr(move))


if __name__ == "__main__":
    main()