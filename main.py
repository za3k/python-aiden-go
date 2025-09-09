import copy
copy_board = copy.deepcopy

SIZE = 5

# Assume that the user passes in valid input
def get_move() -> tuple[int, int] | str:
    move_column  = input('Enter column or PASS:')
    if move_column == 'PASS':
        return 'PASS'
    move_row = input('Enter row:')
    move_column=int(move_column)-1
    move_row=int(move_row)-1
    move = (move_row, move_column)
    return move


def print_row(row: list[str]) -> None :
    print('{} {} {} {} {}'.format(row[0], row[1], row[2], row[3], row[4]))


def make_empty_board() -> list[list[str]]:
    return [['‧','‧','‧','‧','‧'],['‧','‧','‧','‧','‧'],['‧','‧','‧','‧','‧'],['‧','‧','‧','‧','‧'],['‧','‧','‧','‧','‧']]


def print_board(board: list[list[str]]) -> None:
    for i in range(SIZE):
        print_row(board[4-i])


def stone_for(black_stone: bool)-> str:
    if black_stone:
        return '◯'
    else:
        return '⬤'


def play_move(move: tuple[int, int] | str, board: list[list[str]], black_to_play: bool) -> list[list[str]]:
    new_board = copy_board(board)
    if move == 'PASS':
        return new_board
    else:
        new_board[move[0]][move[1]] = stone_for(black_to_play)
        return new_board


def main():
    board = make_empty_board()
    black_to_play = True
    print_board(board)
    move = get_move()
    #print(repr(move))

    board = play_move(move, board, black_to_play)
    black_to_play = not black_to_play
    print_board(board)


if __name__ == "__main__":
    main()