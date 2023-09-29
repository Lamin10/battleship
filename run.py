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


# Computer creates 5 ships
def create_ships(board):
    for _ in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = "X"
        

def get_ship_location():
    while True:
        row = int(input("Enter the row of the ship from 1 to 8: "))
        if row in "12345678":
            break
        print('Not an appropriate choice, please select a valid row')
    while True:
        column = input("Enter the column of the ship from A to H: ").upper()
        if column in "ABCDEFGH":
            break
        print('Not an appropriate choice, please select a valid column')
    return int(row) - 1, letters_to_numbers[column]


# Check if all ships are hit
def count_hit_ships(board):
    return sum(row.count("X") for row in board)


# function to play the game
def play_game():
    create_ships(HIDDEN_BOARD)
    turns = 10
    hits = 0
    misses = 0
    while turns > 0:
        print("Welcome To Battleship Game!!")
        print('Guess a Battleship Location') 
        print_board(GUESS_BOARD)
        print_board(HIDDEN_BOARD)
        row, column = get_ship_location()
        if GUESS_BOARD[row][column] == "-":
            print("You guessed that one already.")
        elif HIDDEN_BOARD[row][column] == "X":
            print("Hit")
            GUESS_BOARD[row][column] = "X"
            hits += 1
            turns -= 1
        else:
            print("MISS!")
            GUESS_BOARD[row][column] = "-"
            misses += 1
            turns -= 1
        if count_hit_ships(GUESS_BOARD) == 5:
            print("You win!")
            break
        print(f"You have {turns} turns left")
        if turns == 0:
            print("You ran out of turns")
            print(f"Number of Hits: {hits}")
            print(f"Number of Misses: {misses}")


# Function to replay the game after it ends
def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()

