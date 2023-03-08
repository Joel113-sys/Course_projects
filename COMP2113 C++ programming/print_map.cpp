#include <iostream>
#include <string>
#include <iomanip>


#include <vector>

using namespace std;

#include "chess_and_grid.h"

#include "print_map.h"
// What does the fuction do: This function will print out the map of the aeroplane chess to the screen
// What are the input: N/A
// What are the output: print the map of the aeroplane chess to the screen
void print_AC_map()
{
  cout << "Here is the board of the aeroplane chess! Have fun :D" << endl;
  /* template
  cout << "------" << endl;
  cout << "| 01 |" << endl;
  cout << "| Sp |" << endl;
  cout << "------" << endl;
  */
  
  // 1st line
  cout << setfill('-') << setw(78) << "" << endl;
  cout << "| 01 || 02 || 03 || 04 || 05 || 06 || 07 || 08 || 09 || 10 || 11 || 12 || 13 |" << endl;
  cout << "| Sp || He || Di || Cl || Sp || He || Di || Cl || Sp || He || Di || Cl || Sp |" << endl;
  cout << setfill('-') << setw(78) << "" << endl; 
  
  // 2nd line
  cout << right << "| 48 |" << setfill(' ') << setw(36) << "| 49 |" << setw(21) << setfill(' ') << "|" << setw(15) << "| 14 |" << endl;
  cout << "| Cl |" << setfill(' ') << setw(36) << "| H* |" << setw(21) << setfill(' ') << "|" << setw(15) << "| He |" << endl;
  cout << left << setfill(' ') << setw(36) << "------" << setw(36) << "------" << "------" << endl;
  
  // 3rd line
  cout << right << "| 47 |" << setfill(' ') << setw(36) << "| 50 |" << setw(21) << setfill(' ') << "|" << setw(15) << "| 15 |" << endl;
  cout << "| Di |" << setfill(' ') << setw(36) << "| H* |" << setw(21) << setfill(' ') << "|" << setw(15) << "| Di |" << endl;
  cout << left << setfill(' ') << setw(36) << "------" << setw(36) << "------" << "------" << endl;
  
  // 4th line
  cout << right << "| 46 |" << setfill('-') << setw(30) << ">" << "| 51 |" << setw(21) << setfill(' ') << "|" << setw(15) << "| 16 |" << endl;
  cout << "| He |" << setfill(' ') << setw(36) << "| H* |" << setw(21) << setfill(' ') << "|" << setw(15) << "| Cl |" << endl;
  cout << left << setfill(' ') << setw(36) << "------" << setw(36) << "------" << "------" << endl;
  
  // 5th line
  cout << right << "| 45 |" << setfill(' ') << setw(36) << "| 52 |" << setw(21) << setfill(' ') << "|" << setw(15) << "| 17 |" << endl;
  cout << "| Sp |" << setfill(' ') << setw(36) << "| H* |" << setw(21) << setfill(' ') << "|" << setw(15) << "| Sp |" << endl;
  cout << left << setfill(' ') << setw(36) << "------" << setw(36) << "------" << "------" << endl;
  
  // 6th line
  cout << right << "| 44 |" << setfill(' ') << setw(36) << "| 53 |" << setw(21) << setfill(' ') << "|" << setw(15) << "| 18 |" << endl;
  cout << "| Cl |" << setfill(' ') << setw(36) << "| H* |" << setw(22) << setfill(' ') << "\\|/" << setw(14) << "| He |" << endl;

  
  // 7th line
  cout << setfill('-') << setw(78) << "" << endl;
  cout << "| 43 || 60 || 61 || 62 || 63 || 64 || 54 || 65 || 66 || 67 || 68 || 69 || 19 |" << endl;
  cout << "| Di || S* || S* || S* || S* || S* || ** || D* || D* || D* || D* || D* || Di |" << endl;
  cout << setfill('-') << setw(78) << "" << endl;
  
  // 8th line
  cout << right << "| 42 |" << setw(22) << setfill(' ') << "/|\\" << setw(14) << setfill(' ') << "| 55 |" << setw(36) << "| 20 |" << endl;
  cout << "| He |" << setw(21) << setfill(' ') << "|" << setw(15) << setfill(' ') << "| C* |"  << setw(36) << "| Cl |" << endl;
  cout << left << setfill(' ') << setw(36) << "------" << setw(36) << "------" << "------" << endl;
  
  // 9th line
  cout << right << "| 41 |" << setw(21) << setfill(' ') << "|" << setw(15) << setfill(' ') << "| 56 |" << setw(36) << "| 21 |" << endl;
  cout << "| Sp |" << setw(21) << setfill(' ') << "|" << setw(15) << setfill(' ') << "| C* |"  << setw(36) << "| Sp |" << endl;
  cout << left << setfill(' ') << setw(36) << "------" << setw(36) << "------" << "------" << endl;
  
  // 10th line
  cout << right << "| 40 |" << setw(21) << setfill(' ') << "|" << setw(15) << setfill(' ') << "| 57 |" << setw(36) << "| 22 |" << endl;
  cout << "| Cl |" << setw(21) << setfill(' ') << "|" << setw(15) << setfill(' ') << "| C* |"  << setw(36) << "| He |" << endl;
  cout << left << setfill(' ') << setw(36) << "------" << setw(36) << "------" << "------" << endl;
  
  // 11th line
  cout << right << "| 39 |" << setw(21) << setfill(' ') << "|" << setw(15) << setfill(' ') << "| 58 |" << setw(36) << "| 23 |" << endl;
  cout << "| Di |" << setw(21) << setfill(' ') << "|" << setw(15) << setfill(' ') << "| C* |"  << setw(36) << "| Di |" << endl;
  cout << left << setfill(' ') << setw(36) << "------" << setw(36) << "------" << "------" << endl;
  
  // 12th line
  cout << right << "| 38 |" << setw(21) << setfill(' ') << "|" << setw(15) << setfill(' ') << "| 59 |" << "<" << setw(35) << setfill('-') << "| 24 |" << endl;
  cout << "| He |" << setw(21) << setfill(' ') << "|" << setw(15) << setfill(' ') << "| C* |"  << setw(36) << "| Cl |" << endl;
  
  // 13th line
  cout << setfill('-') << setw(78) << "" << endl;
  cout << "| 37 || 36 || 35 || 34 || 33 || 32 || 31 || 30 || 29 || 28 || 27 || 26 || 25 |" << endl;
  cout << "| Sp || Cl || Di || He || Sp || Cl || Di || He || Sp || Cl || Di || He || Sp |" << endl;
  cout << setfill('-') << setw(78) << "" << endl; 
  
  return;
}

