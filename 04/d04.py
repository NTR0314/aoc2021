import numpy as np

drawn_numbers = [int(x) for x in open("input.txt").readline().split(",")]
print(drawn_numbers)

boards = [(lambda y: np.array([(lambda z: [int(x) for x in z.split()])(x) for x in y.split("\n")]))(x) for x in
          open("input.txt").read().split("\n\n")[1:]]


def bingo(board: np.ndarray):
    # Check rows
    for row in board:
        if (row == -1).all():
            return True


    # Check columns
    for column in board.transpose():
        if (column == -1).all():
            return True

    return False


def parse_draw(draw: int, board):
    board[board == draw] = -1
    return board


def get_unmarked(board):
    return sum(board[board != -1])


for drawn_number in drawn_numbers:
    for board in boards:
        board = parse_draw(drawn_number, board)
        if bingo(board):
            print(f"silver: {get_unmarked(board) * drawn_number}")
        if (np.array([bingo(x) for x in boards])).all():
            print(f"gold: {get_unmarked(board) * drawn_number}")
            quit()