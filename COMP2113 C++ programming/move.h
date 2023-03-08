#ifndef MOVE_H
#define MOVE_H

#include <vector>
using namespace std;

#include "chess_and_grid.h"


void depart(Chess &o);
void jump(Chess& o);
void update_chess (int move_num, Chess& c);
void fly(Chess& o);
void trodding(Chess &o);
void stack(Chess& o);
void dual_move(Chess &o, int num);
void move(int num, Chess& o);
void move_plane(int dice_num, int count);


#endif
