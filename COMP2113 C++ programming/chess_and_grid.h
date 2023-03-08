#ifndef CHESS_AND_GRID_H
#define CHESS_AND_GRID_H

#include <iostream>
#include <vector>
using namespace std;


	
	struct Chess {
		bool stack;
		bool depart;
		int position;
		char suit;
		int code;
		bool exist;
	};

	extern vector<Chess> chess_vector;
	extern Chess s1;
	extern Chess s2;
	extern Chess s3;
	extern Chess s4;
	extern Chess h1;
	extern Chess h2;
	extern Chess h3;
	extern Chess h4;
	extern Chess d1;
	extern Chess d2;
	extern Chess d3;
	extern Chess d4;
	extern Chess c1;
	extern Chess c2;
	extern Chess c3;
	extern Chess c4;

	struct Grid
	{
		char suit;
		bool shortcut;
		bool central;
		int plane_num;
		char plane_suit;
		int jump_to_next;
	};


	extern Grid GridArr[70];

	void initialize_all_grids();


#endif
