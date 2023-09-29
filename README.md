# Battleship Game
  Welcome to the Battleship Game!

## About
 In this Python game of Battleship:

+ The computer creates and hides five battleships on its board.
+ You have 10 turns to guess the coordinates to attack.
+ The game provides feedback on whether your attack was a "Hit" or "Miss."
+ The game ends when you successfully sink all five enemy ships or run out of turns.
  
  ## Table of Contents
  
## Game Overview
  + Battleship is a two-player game where each player tries to sink the other player's ships. 
  + In this Python game, you'll play against the computer, which has hidden its ships 
    on an 8x8 board. 
  + Your task is to guess the locations of these ships and sink them before running out of turns.
   
## How to Play The Game
  + Launching the Game: Run the game by executing the python3 run.py file.
  + You have 10 turns to guess the locations of the computer's ships.
  + Enter the row (from 1 to 8) and column (from A to H) coordinates to target a square on the board.
  + You'll receive feedback on whether your guess was a "Hit" (you hit a ship) or a "Miss" (you missed).
  + You guessed that one already" if you target a square you've already attacked
  + Winning the Game:
  + The game ends when you successfully sink all five of the computer's battleships.
  + If you run out of turns before sinking all ships, the game will display the final board, including your hits and misses.
   
## Functions and Features
    This Battleship game is built with the following functions and features:

   ### print_board(board): 
   + The print_board function is responsible for displaying the game board, including ship locations and hits/misses.
   + It presents the board in a user-friendly format, making it easy to understand and play the game.
   ### create_ships(board): 
   + The create_ships function is called when the game starts and is responsible for the computer creating and placing five ships randomly on its hidden board.
   + It ensures that ships do not overlap.
     
   ### get_ship_location(): 
   + The get_ship_location function prompts the player to enter the row and column coordinates to target a square on the board.
   + It validates the input to ensure the coordinates are within the valid range (1-8 for rows, A-H for columns).
     
 ### count_hit_ships(board):
  + The count_hit_ships function calculates the number of enemy ships that have been hit by counting the "X" symbols on the board. 
  + This information is used to determine when you win the game.
  
## Testing
### Manual
## Bugs Detected
## Validator Testing
## Deployment
## Credits
