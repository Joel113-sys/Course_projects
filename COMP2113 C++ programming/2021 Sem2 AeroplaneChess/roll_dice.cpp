#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>
#include "roll_dice.h"

using namespace std;

//#include "chess_and_grid.h"


//This function is used to implement the dice rolling feature of the game
//There is no input needed for the function
//the function outputs an integer
int roll_dice() {
	int num;
	cout << "please enter an integer to roll the dice (1-100)" << endl;
	cin >> num;

	srand(time(NULL));
	int result;
	result = rand() % 6 + 1;
	cout << "You rolled a " << result << " !" << endl;

	return result;
}
