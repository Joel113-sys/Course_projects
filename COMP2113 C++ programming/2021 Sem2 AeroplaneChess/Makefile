FLAGS = -pedantic-errors -std=c++11

check_end.o: check_end.cpp check_end.h chess_and_grid.h
	g++ $(FLAGS) -c check_end.cpp
move.o: move.cpp move.h chess_and_grid.h screen_output.h
	g++ $(FLAGS) -c move.cpp
print_map.o: print_map.cpp print_map.h chess_and_grid.h
	g++ $(FLAGS) -c print_map.cpp
roll_dice.o: roll_dice.cpp roll_dice.h
	g++ $(FLAGS) -c roll_dice.cpp
screen_output.o: screen_output.cpp screen_output.h chess_and_grid.h
	g++ $(FLAGS) -c screen_output.cpp
suspend_and_restart_the_game.o: suspend_and_restart_the_game.cpp suspend_and_restart_the_game.h chess_and_grid.h
	g++ $(FLAGS) -c suspend_and_restart_the_game.cpp
main.o: main.cpp check_end.h chess_and_grid.h move.h print_map.h roll_dice.h screen_output.h suspend_and_restart_the_game.h
	g++ $(FLAGS) -c main.cpp
aeroplane: main.o suspend_and_restart_the_game.o screen_output.o roll_dice.o print_map.o move.o check_end.o
	g++ $(FLAGS) main.o suspend_and_restart_the_game.o screen_output.o roll_dice.o print_map.o move.o check_end.o -o aeroplane
