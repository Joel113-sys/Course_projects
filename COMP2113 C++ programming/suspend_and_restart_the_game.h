#ifndef SUSPEND_AND_RESTART_THE_GAME_H
#define SUSPEND_AND_RESTART_THE_GAME_H

#include <vector>
using namespace std;

#include "chess_and_grid.h"

void suspend_or_not(int count);
void suspend_the_game(int count);
void delete_state_array (int * sptr) ;
bool restart_or_not();
int * ptr_to_old_game();
void initialize_with_old_game(int & count, vector<Chess>::iterator citr);



#endif
