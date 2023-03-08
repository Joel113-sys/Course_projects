#include <string>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

#include "chess_and_grid.h"
#include "suspend_and_restart_the_game.h"
void suspend_the_game(int count);



//This function is to ask for opinions as to suspend the game or not
//The fucntion takes in an integer input called count
//The function gives no output
void suspend_or_not(int count)
{
	string user_input;
	cout << "Do you want to suspend the game? (Y/N)" << endl;
	YorN_SUS:
	cin >> user_input;
	if (user_input == "N")
		return;
	else if (user_input == "Y")
		suspend_the_game(count);
	else {
		cout << "Invalid input! Please enter (Y/N):" << endl;
		goto YorN_SUS;
	}
}

//The function implements the game suspending feature of the game
//The needed input of the function is an integer number called count
//This function gives no output
void suspend_the_game(int count)
{
	ofstream fout;
	fout.open("game_state.txt");
	
   if ( fout.fail() ) {
      cout << "Error occurred! Could not save the game state :(" << endl;
      exit(1);
   }

	else {
		int current_player = count % 4;
		fout << current_player << endl;
		
		fout << s1.stack << " " << s1.depart << " " << s1.position << " " << s1.exist << endl;
		fout << s2.stack << " " << s2.depart << " " << s2.position << " " << s2.exist << endl;
		fout << s3.stack << " " << s3.depart << " " << s3.position << " " << s3.exist << endl;
		fout << s4.stack << " " << s4.depart << " " << s4.position << " " << s4.exist << endl;
		
		fout << h1.stack << " " << h1.depart << " " << h1.position << " " << h1.exist << endl;
		fout << h2.stack << " " << h2.depart << " " << h2.position << " " << h2.exist << endl;
		fout << h3.stack << " " << h3.depart << " " << h3.position << " " << h3.exist << endl;
		fout << h4.stack << " " << h4.depart << " " << h4.position << " " << h4.exist << endl;
		
		fout << d1.stack << " " << d1.depart << " " << d1.position << " " << d1.exist << endl;
		fout << d2.stack << " " << d2.depart << " " << d2.position << " " << d2.exist << endl;
		fout << d3.stack << " " << d3.depart << " " << d3.position << " " << d3.exist << endl;
		fout << d4.stack << " " << d4.depart << " " << d4.position << " " << d4.exist << endl;
		
		fout << c1.stack << " " << c1.depart << " " << c1.position << " " << c1.exist << endl;
		fout << c2.stack << " " << c2.depart << " " << c2.position << " " << c2.exist << endl;
		fout << c3.stack << " " << c3.depart << " " << c3.position << " " << c3.exist << endl;
		fout << c4.stack << " " << c4.depart << " " << c4.position << " " << c4.exist << endl;
		
		fout.close();
		
		cout << "The game state has been saved successfully in file: game_state.txt :)" << endl;
		exit(0);
	}
}


//This function is to determine whether to restart the game or not
//The functions need no input
//The function gives a binary output to indicate player's opinion as to restart or not
bool restart_or_not()
{
	string user_input;
	
	cout << "Do you want to restart an old game? (Y/N)" << endl;
	YorN:
	cin >> user_input;
	if (user_input == "N")
		return false;
	else if (user_input == "Y") {
		return true;
	}
	else {
		cout << "Invalid input! Please enter (Y/N):" << endl;
		goto YorN;
	}
}

//This function helps load the trace and data resulted from a previous time of gaming
//This function needs no input
//This function gives an integer number as the output
int * ptr_to_old_game()
{
	string filename;
		
	cout << "Please enter the name of the file:" << endl;
	cin >> filename;
	
	
	ifstream fin;
	fin.open(filename.c_str());
	
	if ( fin.fail() ){
		cout << "Error in file opening :(" << endl;
 		exit(1);
 	}
 	
 	else {
		int size = 65;
		int * stateptr = new int[size];
		for (int i = 0; i < 65; i++) 
			fin >> stateptr[i];
		fin.close();
		return stateptr;
	}
	
		
}

void delete_state_array (int * sptr);

//This function helps initialize with the data from the previous gaming.
//This function takes in an integer count and a vector storing Chesses as inputs
//The function gives no particular output 
void initialize_with_old_game(int & count, vector<Chess>::iterator citr) {
	int * stateptr = ptr_to_old_game();
	
	count = stateptr[0];
	vector<Chess>::iterator cbeg = citr;
	for (int i = 0; i < 16; i++) {
		cbeg->stack = (bool)stateptr[4 * i + 1];
		cbeg->depart = (bool)stateptr[4 * i + 2];
		cbeg->position = stateptr[4 * i + 3];
		cbeg->exist = (bool)stateptr[4 * i + 4];
		++cbeg;
	}
	if (stateptr != nullptr)
		delete_state_array(stateptr);
}

//This function implements the array deleting feature of the game, it only works on planes that have already arrived at the end
//The function takes in a pointer as the input
//the function give no output
void delete_state_array (int * sptr) 
{
	if (sptr != nullptr) {
		delete [] sptr;
	}
	return;
}
