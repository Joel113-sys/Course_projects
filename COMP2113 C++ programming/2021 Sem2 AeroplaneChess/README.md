# 2021Sem2COMP2113Group73AeroplaneChess

Group No.: 73

Group members: 

Xin Jiayi     UID: 3035770525

Lou Huajie    UID: 3035772418

Topic: Aeroplane chess

Link:  

https://github.com/Raina-Xin/2021Sem2COMP2113Group73AeroplaneChess/find/main

**Compilation and execution instructions:**
1. chmod 777 Makefile 
1. make aeroplane
2. ./aeroplane


**Description of the game:**

Aeroplane Chess is a Chinese cross-and-circle board game. The game consists of a game board, four sets of 4 coloured airplane pieces, typically red, yellow, blue and green and a 6-faced dice. In our implementation, the four colors correspond to four suits: spade, heart, diamond and club. Featuring four starting hangars in each corner, the board has an outer track consisting of 48 grids, four central tracks each leading from the track to the destination (grid 54) at the centre of the board. The board is evenly divided between the suits spade, heart, diamond, and club. 

Four players each try to get all their four planes hangars around the outer track, through the central track, to the the destination grid. Each player takes a turn by rolling the die. The first player to get all four planes to the destination grid wins.

 - The routes of each player are as follows (Clockwise):
	- Player Spade: 01 -> 13 -> 25 -> 37 -> 43-(turning point)-60 -> 54
	- Player Heart: 13 -> 25 -> 37 -> 01-> 07-(turning point)-49 -> 54
	- Player Diamond: 25 -> 37 -> 01-> 13 -> 19-(turning point)-69 -> 54
	- Player Club: 37 -> 01-> 13 -> 25 -> 31-(turning point)-59 -> 54

![areoplane_chess_board](https://user-images.githubusercontent.com/75571511/116039839-cfb8c080-a69d-11eb-8da5-0def0309047a.jpg)



**In one turn a player could do the following:**

- (Departure) Take a piece out of the hangar onto the board if and only if the player rolls a 6.
- (Move a piece) Move a piece that is on the board clockwise around the outer track, the number of spaces indicated by the die.
- (Additional roll) A roll of 6, whether it is used to enter or move a piece, gives that player another roll. A player could roll continuously if he/she gets consecutive 6.
- (Trodding) When a player's chess lands on an opponent's chess, the opponent's chess will be trodded back to its hangar.
- (Jump) When a plane lands on a grid of its own colour, it immediately jumps to the next grid of its own colour. Any opposing planes sitting on these grids are sent back to their hangars.
- (Flying) There are additional shortcut squares. When a plane lands on one of these of its own colour, it may take the shortcut, and any opposing planes in the path of the shortcut are sent back to their hangars. 
- (Stacking) When a plane lands on another plane in its own fleet, the chess will be stacked to each other and be moved as one piece until they reach the centre or being landed on by an opponent's piece. When stacked pieces are sent back to their hangar by an opponent landing on them, they are no longer stacked. 
- (Central Track) When the player's chess comes to the corresponding central track (e.g., for player Spade, the track is denote with symbol S* on the map), the play need to throw a dice with exact number of the distance to get to the distination. Otherwise, the chess will go back and forth on the central track.



**Implemented Features:**

- Initialization/suspension of the game
	- Restart an old game with an input file
	- Suspend the game and generate a file which stores the game state

- During the Play 
	- Print the areoplane chess map
	- Roll the dice and cast the dice
	- Depart
	- Additional roll
	- Jump 
	- Flying
	- Stacking and dual move
	- Trodding
	- Game continues/ends
	- Central track
	- Input corrrection and penalty to invalid input
	
- Check End of the game
	- Check the end and print winner
	

**Explanation with Code requirements:**
- Generation of random game sets or events
	- when implementing random roll of dice, rand() and srand(time(NULL)) are used to simulate the dice-rolling process, which can randomly produce an integer number.
	
- Data structures for storing game status
	- define a structure called "Chess" to store the status of the chess
	- define a structure called "grid" to store the charateristics of a grid
	- define a Chess vector to help with the initialization of the game
	- define an array of Grid structure	

- Dynamic memory management
	- use a dynamic array to help the initialization of the game
	- delete the dynamic array after the initialization to free the memory
	- use chess_vector.pop_back() to free the memory of the vector container after the usage
	
- File input/output 
	- use file input which contains the game state of an old game to initialize the game
	- use file output to save game status in a file called "game_state.txt" which could be used to restart the game next time

- Program codes in multiple files
	- separate the definition and implementation of different functions in .h and .cpp files, respectively. For example, move.h and move.cpp
	- separate the whole project into different sections and write multiple files for easier debugging process. We divide it into eight sections as follows: check_end, chess_and_grid, move, print_map, roll_dice, screen_output, suspend_and_restart_the_game, main
	- use MakeFile to facilitate separate complilation

**Library we used:**
- cstdlib and ctime: use for generating random numbers while rolling the dice    
- iostream: standard input and output
- fstream: file I/O 
- vector: to store the data and help with the initialization of the game  
- string: store the data of each move and conditions
- iomanip: we adopted the setw function to regulate the standard space length when plotting the map.

**Note**
- There is a file called "game_state.txt" in the repo, you could use it to initialize the game
- Since this game has many randomness, we could not write sample input. But we include four sample output files in the repo for your reference :D
- Have fun by play the aeroplane chess!



