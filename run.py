from random import randint

# Board for holding ship locations
HIDDEN_BOARD = [[" "] * 8 for _ in range(8)]
# Board for displaying hits and misses
GUESS_BOARD = [[" "] * 8 for _ in range(8)]


def print_board(board):
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    for row_num, row in enumerate(board, 1):
        row_str = f"{row_num}|{'|'.join(row)}|"
        print(row_str)


letters_to_numbers = {chr(ord('A') + i): i for i in range(8)}

print(print_board(GUESS_BOARD))




