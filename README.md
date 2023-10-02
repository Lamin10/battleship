# Battleship Game
  Welcome to the Battleship Game!

## About
 In this Python game of Battleship:

+ The computer creates and hides five battleships on its board.
+ You have 10 turns to guess the coordinates to attack.
+ The game provides feedback on whether your attack was a "Hit" or "Miss."
+ The game ends when you successfully sink all five enemy ships or run out of turns.
+ And it ask whether you would like to play again if yes the the game restart if no it ends with a gooddbye.
    
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
+ A manual testing was done on the user input which accept input in the range of 1 to 8 on the rows, a number out of that range was entered
+ and it gives a valueErrow with a message "Not an appropriate choice, please select a valid row".
+ The same was done on the column input which range from A to H and got the same valueError with the message "Not a correct choice, please select a valid column"
+ When a hit is made and it miss a dass "-" is printed on that spot when you select the same spot again you get and error message that "You guessed that one already"
+ The same when you hit a ship which prints an "x" on that spot
## Bugs Detected
+ Indentations issues was detected
+ 

## Validator Testing
+ Testing of the python battleship game code was done on Pep8online.com website and indentation issues was found and it was troubleshoot
+ The secon testing was done and no bugs where found.
  
## Deployment
+ Unfortunately the battleship game was not been able to be deployed
+ RENDER: Deployment was tryied to be done on Render but it was not successful it always encounter an EOFError.
+ The error typically occurs when the input() function is used to read input from the user, but the input stream ends unexpectedly.
+ This error is happening at line 33, where its trying to read the row of the ship
+ To troubleshoot this error i added a "/n" on all the input fields but was to no success
+ Testing Locally: the code was tested locally to see if it runs without errors and it did work without any error  and it was likely an issue with the Render environment.
+ DIGITALOCEAN: Deployment was also tried on DigitalOcean but to no success it was asking for a package-lock.json file
+ To troubleshoot this error i tried to install a package-lock.json file using the terminal with the command "npm install" but return command not found.
+ The package.json file was renamed to package-lock.json but still the deployment failed.
+ HEROKU: Couldnt also deploy on Heroku due to registration issues which have to do with my bank card
## Credits
+ The battleship game was build with VisualCode Studio and then transfered to Codeanywhere with the Codeinstitute python deployment template
+  This Battleship game is built with the following functions and features:
