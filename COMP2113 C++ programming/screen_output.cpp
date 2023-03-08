
#include <iomanip>
#include <iostream>

#include <vector>

using namespace std;

#include "chess_and_grid.h"

#include "screen_output.h"
//screen output.cpp
//This function helps print the status of each players' planes at proper situations
//There is no input needed for this function to conduct
//This function gives no output
void screen_output_after_each_player()
{
  //-------- START to print the status of Player Spade's Plane------------
  cout << setw(15) << setfill(' ') << left << "Player Spade" << "-> ";
  cout << "s1: ";
  if (s1.exist && s1.depart) 
    cout << setw(16) << left << setfill(' ') << s1.position << " ";
  else if (s1.exist && !s1.depart)
    cout << setw(16) << left << setfill(' ') <<  "not departed!" << " ";
  else if (!s1.exist)
    cout << setw(16) << left << setfill(' ') <<  "already arrived!" << " ";
    
  cout << "s2: ";
  if (s2.exist && s2.depart) 
    cout << setw(16) << left << setfill(' ') <<  s2.position << " ";
  else if (s2.exist && !s2.depart)
    cout << setw(16) << left << setfill(' ') <<  "not departed!" << " ";
  else if (!s2.exist)
    cout << setw(16) << left << setfill(' ') <<  "already arrived!" << " ";
    
  cout << "s3: ";
  if (s3.exist && s3.depart) 
    cout << setw(16) << left << setfill(' ') << s3.position << " ";
  else if (s3.exist && !s3.depart)
    cout << setw(16) << left << setfill(' ') << "not departed!" << " ";
  else if (!s3.exist)
    cout << setw(16) << left << setfill(' ') << "already arrived!" << " ";
    
  cout << "s4: ";
  if (s4.exist && s4.depart) 
    cout << setw(16) << left << setfill(' ') << s4.position << " ";
  else if (s4.exist && !s4.depart)
    cout << setw(16) << left << setfill(' ') << "not departed!" << " ";
  else if (!s4.exist)
    cout << setw(16) << left << setfill(' ') << "already arrived!" << " ";
  
  cout << endl;
  //--------- FINISH Print the status of Player Spade's Plane------------
  
    //-------- START to print the status of Player Heart's Plane------------
  cout << setw(15) << setfill(' ') << left << "Player Heart" << "-> ";
  cout << "h1: ";
  if (h1.exist && h1.depart) 
    cout << setw(16) << left << setfill(' ') << h1.position << " ";
  else if (h1.exist && !h1.depart)
    cout << setw(16) << left << setfill(' ') << "not departed!" << " ";
  else if (!h1.exist)
    cout << setw(16) << left << setfill(' ') << "already arrived!" << " ";
    
  cout << "h2: ";
  if (h2.exist && h2.depart) 
    cout << setw(16) << left << setfill(' ') << h2.position << " ";
  else if (h2.exist && !h2.depart)
    cout << setw(16) << left << setfill(' ') << "not departed!" << " ";
  else if (!h2.exist)
    cout << setw(16) << left << setfill(' ') << "already arrived!" << " ";
    
  cout << "h3: ";
  if (h3.exist && h3.depart) 
    cout << setw(16) << left << setfill(' ') << h3.position << " ";
  else if (h3.exist && !h3.depart)
    cout << setw(16) << left << setfill(' ') << "not departed!" << " ";
  else if (!h3.exist)
    cout << setw(16) << left << setfill(' ') << "already arrived!" << " ";
    
  cout << "h4: ";
  if (h4.exist && h4.depart) 
    cout << setw(16) << left << setfill(' ') << h4.position << " ";
  else if (h4.exist && !h4.depart)
    cout << setw(16) << left << setfill(' ') << "not departed!" << " ";
  else if (!h4.exist)
    cout << setw(16) << left << setfill(' ') << "already arrived!" << " ";
  
  cout << endl;
  //--------- FINISH Print the status of Player Heart's Plane------------
  // intended output: Player Heart -> h1: 19 h2: not departed! h3: 24 h4: already arrived!
  
    //-------- START to print the status of Player Diamond's Plane------------
  cout << setw(15) << setfill(' ') << left << "Player Diamond" << "-> ";
  cout << "d1: ";
  if (d1.exist && d1.depart) 
    cout << setw(16) << left << setfill(' ') << d1.position << " ";
  else if (d1.exist && !d1.depart)
    cout << setw(16) << left << setfill(' ') << "not departed!" << " ";
  else if (!d1.exist)
    cout << setw(16) << left << setfill(' ') << "already arrived!" << " ";
    
  cout << "d2: ";
  if (d2.exist && d2.depart) 
    cout << setw(16) << left << setfill(' ') << d2.position << " ";
  else if (d2.exist && !d2.depart)
    cout << setw(16) << left << setfill(' ') << "not departed!" << " ";
  else if (!d2.exist)
    cout << setw(16) << left << setfill(' ') << "already arrived!" << " ";
    
  cout << "d3: ";
  if (d3.exist && d3.depart) 
    cout << setw(16) << left << setfill(' ') << d3.position << " ";
  else if (d3.exist && !d3.depart)
    cout << setw(16) << left << setfill(' ') << "not departed!" << " ";
  else if (!d3.exist)
    cout << setw(16) << left << setfill(' ') << "already arrived!" << " ";
    
  cout << "d4: ";
  if (d4.exist && d4.depart) 
    cout << setw(16) << left << setfill(' ') << d4.position << " ";
  else if (d4.exist && !d4.depart)
    cout << setw(16) << left << setfill(' ') << "not departed!" << " ";
  else if (!d4.exist)
    cout << setw(16) << left << setfill(' ') << "already arrived!" << " ";
  
  cout << endl;
  //--------- FINISH Print the status of Player Diamond's Plane------------
  
    //-------- START to print the status of Player Club's Plane------------
  cout << setw(15) << setfill(' ') << left << "Player Club" << "-> ";
  cout << "c1: ";
  if (c1.exist && c1.depart) 
    cout << setw(16) << left << setfill(' ') << c1.position << " ";
  else if (c1.exist && !c1.depart)
    cout << setw(16) << left << setfill(' ') << "not departed!" << " ";
  else if (!c1.exist)
    cout << setw(16) << left << setfill(' ') << "already arrived!" << " ";
    
  cout << "c2: ";
  if (c2.exist && c2.depart) 
    cout << setw(16) << left << setfill(' ') << c2.position << " ";
  else if (c2.exist && !c2.depart)
    cout << setw(16) << left << setfill(' ') << "not departed!" << " ";
  else if (!c2.exist)
    cout << setw(16) << left << setfill(' ') << "already arrived!" << " ";
    
  cout << "c3: ";
  if (c3.exist && c3.depart) 
    cout << setw(16) << left << setfill(' ') << c3.position << " ";
  else if (c3.exist && !c3.depart)
    cout << setw(16) << left << setfill(' ') << "not departed!" << " ";
  else if (!c3.exist)
    cout << setw(16) << left << setfill(' ') << "already arrived!" << " ";
    
  cout << "c4: ";
  if (c4.exist && c4.depart) 
    cout << setw(16) << left << setfill(' ') << c4.position << " ";
  else if (c4.exist && !c4.depart)
    cout << setw(16) << left << setfill(' ') << "not departed!" << " ";
  else if (!c4.exist)
    cout << setw(16) << left << setfill(' ') << "already arrived!" << " ";
  
  cout << endl;
  //--------- FINISH Print the status of Player Club's Plane------------
  
  return;
}
