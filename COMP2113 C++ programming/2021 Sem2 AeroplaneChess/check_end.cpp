#include "check_end.h"
#include <iostream>
#include "chess_and_grid.h"
#include <vector>
using namespace std;


// This function check whether the game is end
//no inputs for this function
// Use binary output to indicate if each play has finished the game or not
bool check_end()
{
  if (!s1.exist && !s2.exist && !s3.exist && !s4.exist){
    cout << "Player Space have finished the game! Congratulation!" << endl;
    return true;
  }
  
  else if (!h1.exist && !h2.exist && !h3.exist && !h4.exist){
    cout << "Player Heart have finished the game! Congratulation!" << endl;
    return true;
  }
  else if (!d1.exist && !d2.exist && !d3.exist && !d4.exist){
    cout << "Player Diamond have finished the game! Congratulation!" << endl;
    return true;
  }
  else if (!c1.exist && !c2.exist && !c3.exist && !c4.exist){
    cout << "Player Club have finished the game! Congratulation!" << endl;
    return true;
  }
  else{
      cout << "None of the players has finished the game. Game continues..." << endl;
    return false;
  }
  
  return false;
}
