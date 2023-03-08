#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <string>
#include <fstream>
#include <vector>
#include <ctime>

using namespace std;

#include "chess_and_grid.h"

vector<Chess> chess_vector;

Chess s1 = { false, false, 0, 's', 1, true }; 
Chess s2 = { false, false, 0, 's', 2, true };
Chess s3 = { false, false, 0, 's', 3, true };
Chess s4 = { false, false, 0, 's', 4, true };
Chess h1 = { false, false, 0, 'h', 1, true };
Chess h2 = { false, false, 0, 'h', 2, true };
Chess h3 = { false, false, 0, 'h', 3, true };
Chess h4 = { false, false, 0, 'h', 4, true };
Chess d1 = { false, false, 0, 'd', 1, true };
Chess d2 = { false, false, 0, 'd', 2, true };
Chess d3 = { false, false, 0, 'd', 3, true };
Chess d4 = { false, false, 0, 'd', 4, true };
Chess c1 = { false, false, 0, 'c', 1, true };
Chess c2 = { false, false, 0, 'c', 2, true };
Chess c3 = { false, false, 0, 'c', 3, true };
Chess c4 = { false, false, 0, 'c', 4, true };


#include "check_end.h"
#include "move.h"
#include "print_map.h"
#include "roll_dice.h"
#include "screen_output.h"
#include "suspend_and_restart_the_game.h"

Grid GridArr[70];

void initialize_all_grids();

void initialize_all_grids()
{
	// ------initialize the 0th grid(this grid is useless!!!!)------
	GridArr[0].central = false;
	GridArr[0].shortcut = false;
	GridArr[0].suit = '#';
	GridArr[0].plane_num = 0;
	GridArr[0].plane_suit = '#';
	GridArr[0].jump_to_next = -100;
	// ------FINISH initialize the 0th grid (this grid is useless!!!!)------

	// ------initialize the suit of 69 grids------
	// 48 outer grids
	for (int i = 1; i <= 48; i++) {
		if (i % 4 == 1)
			GridArr[i].suit = 's';
		else if (i % 4 == 2)
			GridArr[i].suit = 'h';
		else if (i % 4 == 3)
			GridArr[i].suit = 'd';
		else if (i % 4 == 0)
			GridArr[i].suit = 'c';
	}
	// 5*4 central grids 
	for (int i = 49; i <= 53; i++)
		GridArr[i].suit = 'H';
	for (int i = 60; i <= 64; i++)
		GridArr[i].suit = 'S';
	for (int i = 55; i <= 59; i++)
		GridArr[i].suit = 'C';
	for (int i = 65; i <= 69; i++)
		GridArr[i].suit = 'D';
	// 1 final grid
	GridArr[54].suit = '*';

	// ------FINISH initialize the suit of 69 grids------

	// ------initialize the shortcut of 69 grids------
	for (int i = 1; i <= 69; i++)
		GridArr[i].shortcut = false;

	GridArr[11].shortcut = true;
	GridArr[24].shortcut = true;
	GridArr[33].shortcut = true;
	GridArr[46].shortcut = true;

	// ------FINISH initialize the shortcut of 69 grids------

	// ------initialize the central of 69 grids------
	for (int i = 1; i <= 69; i++)
		GridArr[i].central = false;

	for (int i = 49; i <= 53; i++)
		GridArr[i].central = true;
	for (int i = 60; i <= 64; i++)
		GridArr[i].central = true;
	for (int i = 55; i <= 59; i++)
		GridArr[i].central = true;
	for (int i = 65; i <= 69; i++)
		GridArr[i].central = true;
	// ------FINISH initialize the central of 69 grids------

	// ------initialize the plane_num of 69 grids------
	for (int i = 1; i <= 69; i++)
		GridArr[i].plane_num = 0;
	// ------FINISH initialize the plane_num of 69 grids------

	// ------initialize the plane_suit of 69 grids------
	for (int i = 1; i <= 69; i++)
		GridArr[i].plane_suit = ' ';
	// ------FINISH initialize the plane_suit of 69 grids------

	// ------initialize the jump_to_next of 69 grids------
	for (int i = 1; i <= 44; i++)
		GridArr[i].jump_to_next = i + 4;

	GridArr[45].jump_to_next = 1;
	GridArr[46].jump_to_next = 2;
	GridArr[47].jump_to_next = 3;
	GridArr[48].jump_to_next = 4;

	//use -1 to initalize those grids which could not implement jump_to_next
	for (int i = 49; i <= 69; i++)
		GridArr[i].jump_to_next = -1;


	// ------FINISH initialize the jump_to_next of 69 grids------

	//-------FINISH initialize all the grid in GridArr

}


//main.cpp
int main()
{
	

	initialize_all_grids();
	
	chess_vector.push_back(s1);
	chess_vector.push_back(s2);
	chess_vector.push_back(s3);
	chess_vector.push_back(s4);
	chess_vector.push_back(h1);
	chess_vector.push_back(h2);
	chess_vector.push_back(h3);
	chess_vector.push_back(h4);
	chess_vector.push_back(d1);
	chess_vector.push_back(d2);
	chess_vector.push_back(d3);
	chess_vector.push_back(d4);
	chess_vector.push_back(c1);
	chess_vector.push_back(c2);
	chess_vector.push_back(c3);
	chess_vector.push_back(c4);
	


	int dice_num;
	string user_input;
	int count = 1;
	
	vector<Chess>::iterator citr = chess_vector.begin();

	bool restart = restart_or_not();
	if (restart) {
		initialize_with_old_game(count, citr);
		cout << "Successfully restart the old game :D" << endl;
		print_AC_map();
		cout << endl;

		s1 = chess_vector[0];
		s2 = chess_vector[1];
		s3 = chess_vector[2];
		s4 = chess_vector[3];
		h1 = chess_vector[4];
		h2 = chess_vector[5];
		h3 = chess_vector[6];
		h4 = chess_vector[7];
		d1 = chess_vector[8];
		d2 = chess_vector[9];
		d3 = chess_vector[10];
		d4 = chess_vector[11];
		c1 = chess_vector[12];
		c2 = chess_vector[13];
		c3 = chess_vector[14];
		c4 = chess_vector[15];

		while ((int)chess_vector.size() != 0)
			chess_vector.pop_back();
	}

	while (true)
	{

		if (count % 4 == 1)
		{

			print_AC_map();
			cout << endl;

			screen_output_after_each_player();
			cout << endl;
			cout << "Spade's turn." << endl;
			dice_num = roll_dice();

			if (dice_num == 6)
			{
			SELECT_6_S:
				cout << "please select your action: depart/move" << endl;
				cin >> user_input;

				if (user_input == "depart")
				{
					string input;
				SELECT_PLANE_6_S:
					cout << "Please select a plane to depart(s1/s2/s3/s4)" << endl;
					cin >> input;
					if (input == "s1")
						depart(s1);
					else if (input == "s2")
						depart(s2);
					else if (input == "s3")
						depart(s3);
					else if (input == "s4")
						depart(s4);
					else {
						cout << "Invalid input! Please enter again!" << endl;
						goto SELECT_PLANE_6_S;
					}

					screen_output_after_each_player();
				}

				else if (user_input == "move" && (s1.depart || s2.depart || s3.depart || s4.depart))
				{
					move_plane(dice_num, count);
				}

				else {
					cout << "Invalid input! Please enter again!" << endl;
					goto SELECT_6_S;
				}

				cout << "Congrats! You get another chance to roll the dice!" << endl;
				continue;
			}

			//modified, need to have at least one departed chess
			else
			{
				if (s1.depart || s2.depart || s3.depart || s4.depart)
				{
					move_plane(dice_num, count);
				}


				else 
				{
				  cout << "None of the planes has departed yet!" << endl;
			  	}

			}

			if (check_end())
				break;

			

			count++;
		}

		else if (count % 4 == 2)
		{


			screen_output_after_each_player();
			cout << endl;
			cout << "Heart's turn." << endl;
			dice_num = roll_dice();


			if (dice_num == 6)
			{
			SELECT_6_H:
				cout << "please select your action: depart/move" << endl;
				cin >> user_input;

				if (user_input == "depart")
				{
					string input;

				SELECT_PLANE_6_H:
					cout << "Please select a plane to depart(h1/h2/h3/h4)" << endl;
					cin >> input;
					if (input == "h1")
						depart(h1);
					else if (input == "h2")
						depart(h2);
					else if (input == "h3")
						depart(h3);
					else if (input == "h4")
						depart(h4);
					else {
						cout << "Invalid input! Please enter again!" << endl;
						goto SELECT_PLANE_6_H;
					}

					screen_output_after_each_player();
				}

				else if (user_input == "move" && (h1.depart || h2.depart || h3.depart || h4.depart))
				{
					move_plane(dice_num, count);
				}

				else {
					cout << "Invalid input! Please enter again!" << endl;
					goto SELECT_6_H;
				}

				cout << "Congrats! You get another chance to roll the dice!" << endl;
				continue;
			}

			else
			{
				if (h1.depart || h2.depart || h3.depart || h4.depart) {
					move_plane(dice_num, count);
				}

				else 
				{
				  cout << "None of the planes has departed yet!" << endl;
			  	}
			}
			if (check_end())
				break;

			

			count++;
		}

		else if (count % 4 == 3)
		{

			screen_output_after_each_player();
			cout << endl;
			cout << "Diamond's turn." << endl;
			dice_num = roll_dice();

			if (dice_num == 6)
			{
			SELECT_6_D:
				cout << "please select your action: depart/move" << endl;
				cin >> user_input;

				if (user_input == "depart")
				{
					string input;

				SELECT_PLANE_6_D:
					cout << "Please select a plane to depart(d1/d2/d3/d4)" << endl;
					cin >> input;

					if (input == "d1")
						depart(d1);
					else if (input == "d2")
						depart(d2);
					else if (input == "d3")
						depart(d3);
					else if (input == "d4")
						depart(d4);
					else {
						cout << "Invalid input! Please enter again!" << endl;
						goto SELECT_PLANE_6_D;
					}

					screen_output_after_each_player();
				}

				else if ((user_input == "move") && (d1.depart || d2.depart || d3.depart || d4.depart))
				{
					move_plane(dice_num, count);
				}

				else {
					cout << "Invalid input! Please enter again!" << endl;
					goto SELECT_6_D;
				}

				cout << "Congrats! You get another chance to roll the dice!" << endl;
				continue;
			}

			else
			{
				if (d1.depart || d2.depart || d3.depart || d4.depart)
				{
					move_plane(dice_num, count);
				}

				else 
				{
				  cout << "None of the planes has departed yet!" << endl;
			  	}

			}

			if (check_end())
				break;

			

			count++;
		}

		else if (count % 4 == 0)
		{


			screen_output_after_each_player();
			cout << endl;
			cout << "Club's turn." << endl;
			dice_num = roll_dice();

			if (dice_num == 6)
			{
			SELECT_6_C:
				cout << "please select your action: depart/move" << endl;
				cin >> user_input;

				if (user_input == "depart")
				{
					string input;

				SELECT_PLANE_6_C:
					cout << "Please select a plane to depart(c1/c2/c3/c4)" << endl;
					cin >> input;
					if (input == "c1")
						depart(c1);
					else if (input == "c2")
						depart(c2);
					else if (input == "c3")
						depart(c3);
					else if (input == "c4")
						depart(c4);
					else {
						cout << "Invalid input! Please enter again!" << endl;
						goto SELECT_PLANE_6_C;
					}

					screen_output_after_each_player();
				}

				else if (user_input == "move" && (c1.depart || c2.depart || c3.depart || c4.depart))
				{
					move_plane(dice_num, count);
				}

				else {
					cout << "Invalid input! Please enter again!" << endl;
					goto SELECT_6_C;
				}

				cout << "Congrats! You get another chance to roll the dice!" << endl;
				continue;
			}

			else
			{
				if (c1.depart || c2.depart || c3.depart || c4.depart)
				{
					move_plane(dice_num, count);
				}

				else 
				{
				  cout << "None of the planes has departed yet!" << endl;
			  	}

			}

			if (check_end())
				break;

			

			count++;
			suspend_or_not(count);
			cout << "Next round!" << endl;
			
		}
		
		
	}
	return 0;
}
