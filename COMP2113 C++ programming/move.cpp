#include <iostream>
#include <string>
#include <vector>
#include "move.h"
#include "chess_and_grid.h"
#include "screen_output.h"


using namespace std;


// The depart function helps chesses(planes) to depart
// The input is the targeted chess
//There's no output for this function
void depart(Chess &o) {
	o.depart = true;
	if (o.suit == 's')
		o.position = 1;
	else if (o.suit == 'h')
		o.position = 13;
	else if (o.suit == 'd')
		o.position = 25;
	else if (o.suit == 'c')
		o.position = 37;
	
	cout << "Your plane " << o.suit << o.code << " has departed!" << endl;
}


//The jump function implements the "jump" feature of the game.
//the imput is the targeted chess(plane)
//there is no output for this function
void jump(Chess& o) 
{
   int pos = o.position;
   if (pos != 0)
   {
	   // if it is a spade chess
	   if (o.suit == 's' && o.position != 1) {
		   if ((o.position >=2) && (o.position <= 40)) {
			   if (GridArr[pos].suit == o.suit) {
				   o.position += 4;
				   cout << "Your plane " << "s" << o.code << " has jumped!" << endl;
			   }
		   }
	   }

	   // if it is a heart chess
	   else if (o.suit == 'h' && o.position != 13) {
		   if ((o.position >= 14 && o.position <= 42) || (o.position == 2)) {
			   if (GridArr[pos].suit == o.suit) {
				   o.position += 4;
				   cout << "Your plane " << o.suit << o.code << " has jumped!" << endl;
			   }
		   }

		   else if (o.position == 46) {
			   o.position = 2;
			   cout << "Your plane " << o.suit << o.code << " has jumped!" << endl;
		   }

	   }

	   // if it is a diamond chess
	   else if (o.suit == 'd' && o.position != 25) {
		   if (o.position == 47) {
			   o.position = 3;
			   cout << "Your plane " << o.suit << o.code << " has jumped!" << endl;
		   }
		   else if ((o.position > 25 && o.position <= 43) || (o.position >= 3 && o.position <= 15)) {
			   if (GridArr[pos].suit == o.suit) {
				   o.position += 4;
				   cout << "Your plane " << o.suit << o.code << " has jumped!" << endl;
			   }
		   }
	   }


	   //if it is a club plane
	   else if (o.suit == 'c' && o.position != 37) {
		   if (o.position == 48) {
			   o.position = 4;
			   cout << "Your plane " << o.suit << o.code << " has jumped!" << endl;
		   }
		   else if ((o.position >= 40 && o.position <= 44) || (o.position >= 8 && o.position <= 24)) {
			   if (GridArr[pos].suit == o.suit) {
				   o.position += 4;
				   cout << "Your plane " << o.suit << o.code << " has jumped!" << endl;
			   }
		   }

		   
	   }
   }
   cout << endl;
}


//This function helps update the location and other several features of the targeted chess(plane)
//the inputs are move_num(result of the dice roll), and the targeted chess
//there is no output for this function
void update_chess (int move_num, Chess& c)
{
	if (c.position != 0)
	{
		//if it is a spade chess
		if (c.suit == 's') {
			//normal situation
			if (c.position >= 1 && c.position <= 37)
				c.position += move_num;
			//for SPADE central track 60-64
			else if (c.position >= 60 && c.position <= 64) {
				if (c.position + move_num == 65) {
					c.position = 54;
					cout << "Your plane " << c.suit << c.code << " has arrived at the destination!";
					c.exist = false;
					//Delete_arrived_plane(c);
				}
				else if (c.position + move_num > 65){
					c.position = 65 - (c.position + move_num - 65);
				}
				else
				{
					c.position += move_num;
				}
			}
			//
			else if (c.position >= 38 && c.position < 43) {
				if ((c.position + move_num) > 43)
					c.position = 59 + (c.position + move_num) - 43;
				else
					c.position += move_num;
			}
			else if (c.position == 43) {
				if (move_num == 6) {
					cout << "Your plane " << c.suit << c.code << " has arrived at the destination!";
					c.exist = false;
				}
				else
					c.position = 59 + move_num;
			}
		}

		//if it is a heart chess
		if (c.suit == 'h') {
			//normal situation
			if ((c.position >= 13 && c.position <= 42) || c.position == 1)
				c.position += move_num;
			else if (c.position >= 43 && c.position <= 48) {
				if ((c.position + move_num) <= 48)
					c.position += move_num;
				else
					c.position = (c.position + move_num) % 48;
			}
			//for HEART central track 49-53
			else if (c.position >= 49 && c.position <= 53) {
				if (c.position + move_num == 54) {
					c.position = 54;
					cout << "Your plane " << c.suit << c.code << " has arrived at the destination!";
					c.exist = false;
				}
				else if (c.position + move_num > 54){
					c.position = 54 - (c.position + move_num - 54);
				}
				else {
					c.position += move_num;
				}

					
			}
			//
			else if (c.position >= 2 && c.position <= 6) {
				if ((c.position + move_num) > 7)
					c.position = 48 + (c.position + move_num) - 7;
				else
					c.position += move_num;
			}
			else if (c.position == 7) {
				if (move_num == 6) {
					cout << "Your plane " << c.suit << c.code << " has arrived at the destination!";
					c.exist = false;
				}
				else
					c.position = 49 + move_num;
			}
		}


		//if it is a diamond chess
		if (c.suit == 'd') {
			//normal situation
			if ((c.position >= 25 && c.position <= 42) || (c.position >= 1 && c.position <= 13))
				c.position += move_num;
			else if (c.position >= 43 && c.position <= 48) {
				if ((c.position + move_num) <= 48)
					c.position += move_num;
				else
					c.position = (c.position + move_num) % 48;
			}
			//for DIAMOND central track 65-69
			else if (c.position >= 65 && c.position <= 69) {
				if (c.position - move_num == 64) {
					c.position = 54;
					cout << "Your plane " << c.suit << c.code << " has arrived at the destination!";
					c.exist = false;
				}
				else if (c.position - move_num < 64){
					c.position = 64 + (64 - c.position + move_num);
				}
				else {
					c.position -= move_num;
				}
			}
			//
			else if (c.position >= 14 && c.position <= 18) {
				if ((c.position + move_num) > 19)
					c.position = 70 - ((c.position + move_num) - 19);
				else
					c.position += move_num;
			}
			else if (c.position == 19) {
				if (move_num == 6) {
					cout << "Your plane " << c.suit << c.code << " has arrived at the destination!";
					c.exist = false;
				}
				else
					c.position = 70 - move_num;
			}
		}


		//if it is a CLUB chess
		if (c.suit == 'c') {
			//normal situation
			if ((c.position >= 37 && c.position <= 42) || (c.position >= 1 && c.position <= 25))
				c.position += move_num;
			else if (c.position >= 43 && c.position <= 48) {
				if ((c.position + move_num) <= 48)
					c.position += move_num;
				else
					c.position = (c.position + move_num) % 48;
			}
			//for CLUB central track 55-59
			else if (c.position >= 55 && c.position <= 59) {
				if (c.position - move_num == 54) {
					c.position = 54;
					cout << "Your plane " << c.suit << c.code << " has arrived at the destination!";
					c.exist = false;
				}
				else if (c.position - move_num < 54){
					c.position = 54 + (54 - c.position + move_num);
				}
				else
				{
					c.position -= move_num;
				}
			}
			//
			else if (c.position >= 26 && c.position <= 30) {
				if ((c.position + move_num) > 31)
					c.position = 60 - ((c.position + move_num) - 31);
				else
					c.position += move_num;
			}
			else if (c.position == 31) {
				if (move_num == 6) {
					cout << "Your plane " << c.suit << c.code << " has arrived at the destination!";
					c.exist = false;
				}
				else
					c.position = 60 - move_num;
			}
		}
	}
	
	else
	{
		cout << "Your plane hasn't departed yet!" << endl;
	}
	return;

}




//This function implements the shortcut (flying) feature of the game
//the input is the targeted chess
//there is no output for this function, but it will change the position of the chess
void fly(Chess& o)
{
	int pos = o.position;
	if ((pos == 11) && (o.suit == 'd')) {
		o.position = 68;
		cout << "Congrats! Your plane flew to Grid " << o.position << "!" << endl;
		
	}
	if ((pos == 24) && (o.suit == 'c')) {
		o.position = 59;
		cout << "Congrats! Your plane flew to Grid " << o.position << "!" << endl;
		
	}
	if ((pos == 33) && (o.suit == 's')) {
		o.position = 63;
		cout << "Congrats! Your plane flew to Grid " << o.position << "!" << endl;
		
	}
	if ((pos == 46) && (o.suit == 'h')) {
		o.position = 51;
		cout << "Congrats! Your plane flew to Grid " << o.position << "!" << endl;
		
	}
}

//This function implements the trodding feature of the game
//the input is the targeted chess
//there is no output for this function
void trodding(Chess &o)
{
	int pos = o.position;
	
	if (s1.position == pos && o.suit != 's' && pos != 0) {
		s1.position = 0;
		s1.depart = false;
		s1.stack = false;
		cout << "Plane " << "s1" << " has been trodded back to the origin." << endl;
		
	}
	if (s2.position == pos && o.suit != 's' && pos != 0) {
		s2.position = 0;
		s2.depart = false;
		s2.stack = false;
		cout << "Plane " << "s2" << " has been trodded back to the origin." << endl;
		
	}
	if (s3.position == pos && o.suit != 's' && pos != 0) {
		s3.position = 0;
		s3.depart = false;
		s2.stack = false;
		cout << "Plane " << "s3"  << " has been trodded back to the origin." << endl;
		
	}
	if (s4.position == pos && o.suit != 's' && pos != 0) {
		s4.position = 0;
		s3.depart = false;
		s4.stack = false;
		cout << "Plane " << "s4" << " has been trodded back to the origin." << endl;
		
	}
	if (h1.position == pos && o.suit != 'h' && pos != 0) {
		h1.position = 0;
		h1.depart = false;
		h1.stack = false;
		cout << "Plane " << "h1" << " has been trodded back to the origin." << endl;
		
	}
	if (h2.position == pos && o.suit != 'h' && pos != 0) {
		h2.position = 0;
		h2.depart = false;
		h2.stack = false;
		cout << "Plane " << "h2"  << " has been trodded back to the origin." << endl;
		
	}
	if (h3.position == pos && o.suit != 'h' && pos != 0) {
		h3.position = 0;
		h3.depart = false;
		h3.stack = false;
		cout << "Plane " << "h3"  << " has been trodded back to the origin." << endl;
		
	}
	if (h4.position == pos && o.suit != 'h' && pos != 0) {
		h4.position = 0;
		h4.depart = false;
		h4.stack = false;
		cout << "Plane " << "h4"  << " has been trodded back to the origin." << endl;
		
	}
	if (d1.position == pos && o.suit != 'd' && pos != 0) {
		d1.position = 0;
		d1.depart = false;
		d1.stack = false;
		cout << "Plane " << "d1"  << " has been trodded back to the origin." << endl;
		
	}
	if (d2.position == pos && o.suit != 'd' && pos != 0) {
		d2.position = 0;
		d2.depart = false;
		d2.stack = false;
		cout << "Plane " << "d2"  << " has been trodded back to the origin." << endl;
		
	}
	if (d3.position == pos && o.suit != 'd' && pos != 0) {
		d3.position = 0;
		d3.depart = false;
		d3.stack = false;
		cout << "Plane " << "d3"  << " has been trodded back to the origin." << endl;
		
	}
	if (d4.position == pos && o.suit != 'd' && pos != 0) {
		d4.position = 0;
		d4.depart = false;
		d4.stack = false;
		cout << "Plane " << "d4"  << " has been trodded back to the origin." << endl;
		
	}
	if (c1.position == pos && o.suit != 'c' && pos != 0) {
		c1.position = 0;
		c1.depart = false;
		c1.stack = false;
		cout << "Plane " << "c1"  << " has been trodded back to the origin." << endl;
		
	}
	if (c2.position == pos && o.suit != 'c' && pos != 0) {
		c2.position = 0;
		c2.depart = false;
		c2.stack = false;
		cout << "Plane " << "c2"  << " has been trodded back to the origin." << endl;
		
	}
	if (c3.position == pos && o.suit != 'c' && pos != 0) {
		c3.position = 0;
		c3.depart = false;
		c3.stack = false;
		cout << "Plane " << "c3"  << " has been trodded back to the origin." << endl;
		
	}
	if (c4.position == pos && o.suit != 'c' && pos != 0) {
		c4.position = 0;
		c4.depart = false;
		c4.stack = false;
		cout << "Plane " << "c4"  << " has been trodded back to the origin." << endl;
		
	}
}

//This function implements the stack feature of the game
//The input is the targeted chess
//There is no output for this function
void stack(Chess& o)
{
	int pos = o.position;
	int cod = o.code;
	
	if (s1.position == pos && o.suit == 's' && (cod != 1) && pos != 0 && o.suit != GridArr[pos].suit && s1.stack == false) {
		s1.stack = true;
		o.stack = true;
		cout << "Plane " << o.suit << o.code << " has been stacked." << endl;
	}
	if (s2.position == pos && o.suit == 's' && (cod != 2) && pos != 0 && o.suit != GridArr[pos].suit && s2.stack == false) {
		s2.stack = true;
		o.stack = true;
		cout << "Plane " << o.suit << o.code << " has been stacked." << endl;
	}
	if (s3.position == pos && o.suit == 's' && (cod != 3) && pos != 0 && o.suit != GridArr[pos].suit && s3.stack == false) {
		s3.stack = true;
		o.stack = true;
		cout << "Plane " << o.suit << o.code << " has been stacked." << endl;
	}
	if (s4.position == pos && o.suit == 's' && (cod != 4) && pos != 0 && o.suit != GridArr[pos].suit && s4.stack == false) {
		s4.stack = true;
		o.stack = true;
		cout << "Plane " << o.suit << o.code << " has been stacked." << endl;
	}
	if (h1.position == pos && o.suit == 'h' && (cod != 1) && pos != 0 && o.suit != GridArr[pos].suit && h1.stack == false) {
		h1.stack = true;
		o.stack = true;
		cout << "Plane " << o.suit << o.code << " has been stacked." << endl;
		
	}
	if (h2.position == pos && o.suit == 'h' && (cod != 2) && pos != 0 && o.suit != GridArr[pos].suit && h2.stack == false) {
		h2.stack = true;
		o.stack = true;
		cout << "Plane " << o.suit << o.code << " has been stacked." << endl;
		
	}
	if (h3.position == pos && o.suit == 'h' && (cod != 3) && pos != 0 && o.suit != GridArr[pos].suit && h3.stack == false) {
		h3.stack = true;
		o.stack = true;
		cout << "Plane " << o.suit << o.code << " has been stacked." << endl;
		
	}
	if (h4.position == pos && o.suit == 'h' && (cod != 4) && pos != 0 && o.suit != GridArr[pos].suit && h4.stack == false) {
		h4.stack = true;
		o.stack = true;
		cout << "Plane " << o.suit << o.code << " has been stacked." << endl;
		
	}
	if (d1.position == pos && o.suit == 'd' && (cod != 1) && pos != 0 && o.suit != GridArr[pos].suit && d1.stack == false) {
		d1.stack = true;
		o.stack = true;
		cout << "Plane " << o.suit << o.code << " has been stacked." << endl;
		
	}
	if (d2.position == pos && o.suit == 'd' && (cod != 2) && pos != 0 && o.suit != GridArr[pos].suit && d2.stack == false) {
		d2.stack = true;
		o.stack = true;
		cout << "Plane " << o.suit << o.code << " has been stacked." << endl;
		
	}
	if (d3.position == pos && o.suit == 'd' && (cod != 3) && pos != 0 && o.suit != GridArr[pos].suit && d3.stack == false) {
		d3.stack = true;
		o.stack = true;
		cout << "Plane " << o.suit << o.code << " has been stacked." << endl;
		
	}
	if (d4.position == pos && o.suit == 'd' && (cod != 4) && pos != 0 && o.suit != GridArr[pos].suit && d4.stack == false) {
		d4.stack = true;
		o.stack = true;
		cout << "Plane " << o.suit << o.code << " has been stacked." << endl;
		
	}
	if (c1.position == pos && o.suit == 'c' && (cod != 1) && pos != 0 && o.suit != GridArr[pos].suit && c1.stack == false) {
		c1.stack = true;
		o.stack = true;
		cout << "Plane " << o.suit << o.code << " has been stacked." << endl;
		
	}
	if (c2.position == pos && o.suit == 'c' && (cod != 2) && pos != 0 && o.suit != GridArr[pos].suit && c2.stack == false) {
		c2.stack = true;
		o.stack = true;
		cout << "Plane " << o.suit << o.code << " has been stacked." << endl;
		
	}
	if (c3.position == pos && o.suit == 'c' && (cod != 3) && pos != 0 && o.suit != GridArr[pos].suit && c3.stack == false) {
		c3.stack = true;
		o.stack = true;
		cout << "Plane " << o.suit << o.code << " has been stacked." << endl;
		
	}
	if (c4.position == pos && o.suit == 'c' && (cod != 4) && pos != 0 && o.suit != GridArr[pos].suit && c4.stack == false) {
		c4.stack = true;
		o.stack = true;
		cout << "Plane " << o.suit << o.code << " has been stacked." << endl;
		
	}   
}	    

//This function implements the dual_move feature of the game. Only works for stacked chesses
//The inputs are the targeted chess and the number of displacement
//there is no output for this function
void dual_move(Chess &o, int num)
{
	update_chess(num, o);
		trodding(o);
		stack(o);
		fly(o);
		trodding(o);
		stack(o);
		jump(o);
		trodding(o);
		stack(o);
	
	if (o.suit == 's') {
		if (s1.stack == true && o.code != 1){
			if(o.position == 54)
				s1.exist = false;
			s1.position = o.position;
		}
		if (s2.stack == true && o.code != 2){
			if(o.position == 54)
				s2.exist = false;
			s2.position = o.position;
		}
		if (s3.stack == true && o.code != 3){
			if(o.position == 54)
				s3.exist = false;
			s3.position = o.position;
		}
		if (s4.stack == true && o.code != 4) {
			if(o.position == 54)
				s4.exist = false;
			s4.position = o.position;
		}
	}
	
	if (o.suit == 'h') {
		if (h1.stack == true && o.code != 1) {
			if(o.position == 54)
				h1.exist = false;
			h1.position = o.position;
		}
		if (h2.stack == true && o.code != 2) {
			if(o.position == 54)
				h2.exist = false;
			h2.position = o.position;
		}
		if (h3.stack == true && o.code != 3) {
			if(o.position == 54)
				h3.exist = false;
			h3.position = o.position;
		}
		if (h4.stack == true && o.code != 4) {
			if(o.position == 54)
				h4.exist = false;
			h4.position = o.position;
		}
	}
	
	if (o.suit == 'c') {
		if (c1.stack == true && o.code != 1) {
			if(o.position == 54)
				c1.exist = false;
			c1.position = o.position;
		}
		if (c2.stack == true && o.code != 2) {
			if(o.position == 54)
				c2.exist = false;
			c2.position = o.position;
		}
		if (c3.stack == true && o.code != 3) {
			if(o.position == 54)
				c3.exist = false;
			c3.position = o.position;
		}
		if (c4.stack == true && o.code != 4) {
			if(o.position == 54)
				c4.exist = false;
			c4.position = o.position;
		}
	}
	
	if (o.suit == 'd') {
		if (d1.stack == true && o.code != 1) {
			if(o.position == 54)
				d1.exist = false;
			d1.position = o.position;
		}
		if (d2.stack == true && o.code != 2)  {
			if(o.position == 54)
				d2.exist = false;
			d2.position = o.position;
		}
		if (d3.stack == true && o.code != 3) {
			if(o.position == 54)
				d3.exist = false;
			d3.position = o.position;
		}
		if (d4.stack == true && o.code != 4) {
			if(o.position == 54)
				d4.exist = false;
			d4.position = o.position;
		}
	}
}

//This function implements the "select function" feature of the game
//There is no input  involved i nthis function
//the output is the selected plane
/*Chess select_plane()
{
Select_Again:
    string input;
    cout << "Please enter the plane that you intend to move: ";
    cin >> input;
    if (input == "s1")
        return s1;
    else if (input == "s2")
        return s2;
    else if (input == "s3")
        return s3;
    else if (input == "s4")
        return s4;
    else if (input == "h1")
        return h1;
    else if (input == "h2")
        return h2;
    else if (input == "h3")
        return h3;
    else if (input == "h4")
        return h4;
    else if (input == "d1")
        return d1;
    else if (input == "d2")
        return d2;
    else if (input == "d3")
        return d3;
    else if (input == "d4")
        return d4;
    else if (input == "c1")
        return c1;
    else if (input == "c2")
        return c2;
    else if (input == "c3")
        return c3;
    else if (input == "c4")
        return c4;
    else {
		cout << "There is no chess called " << input << "! Please select again!" << endl;
		goto Select_Again;
	}
}*/
	    
//This function implements the move action that planes take
//The imputs are the number of displacement and the intended plane
//there is no output for this function
void move(int num, Chess &o)
{
	if (o.stack == false)
	{
		update_chess(num, o);
		trodding(o);
		stack(o);
		fly(o);
		trodding(o);
		stack(o);
		jump(o);
		trodding(o);
		stack(o);
	}
	    
	else
	{
		dual_move(o, num);
	}
}   

//This function moves certain plane
//The inputs are the number of displacement and the targeted plane
//there is no output for this function
void move_plane(int dice_num, int count)
{
	string input;
	cout << "Please enter the plane that you intend to move: ";
	cin >> input;
	if ((count % 4 == 1) && (input == "s1") && (s1.exist != false) && (s1.depart != false)) {
		move(dice_num, s1);
		screen_output_after_each_player();
	}
	else if ((count % 4 == 1) && (input == "s2") && (s2.exist != false) && (s2.depart != false)) {
		move(dice_num, s2);
		screen_output_after_each_player();
	}
	else if ((count % 4 == 1) && (input == "s3") && (s3.exist != false) && (s3.depart != false)) {
		move(dice_num, s3);
		screen_output_after_each_player();
	}
	else if ((count % 4 == 1) && (input == "s4") && (s4.exist != false) && (s4.depart != false)) {
		move(dice_num, s4);
		screen_output_after_each_player();
	}
	else if ((count % 4 == 2) && (input == "h1") && (h1.exist != false) && (h1.depart != false)) {
		move(dice_num, h1);
		screen_output_after_each_player();
	}
	else if ((count % 4 == 2) && (input == "h2") && (h2.exist != false) && (h2.depart != false)) {
		move(dice_num, h2);
		screen_output_after_each_player();
	}
	else if ((count % 4 == 2) && (input == "h3") && (h3.exist != false) && (h3.depart != false)) {
		move(dice_num, h3);
		screen_output_after_each_player();
	}
	else if ((count % 4 == 2) && (input == "h4") && (h4.exist != false) && (h4.depart != false)) {
		move(dice_num, h4);
		screen_output_after_each_player();
	}
	else if ((count % 4 == 3) && (input == "d1") && (d1.exist != false) && (d1.depart != false)) {
		move(dice_num, d1);
		screen_output_after_each_player();
	}
	else if ((count % 4 == 3) && (input == "d2") && (d2.exist != false) && (d2.depart != false)) {
		move(dice_num, d2);
		screen_output_after_each_player();
	}
	else if ((count % 4 == 3) && (input == "d3") && (d3.exist != false) && (d3.depart != false)) {
		move(dice_num, d3);
		screen_output_after_each_player();
	}
	else if ((count % 4 == 3) && (input == "d4") && (d4.exist != false) && (d4.depart != false)) {
		move(dice_num, d4);
		screen_output_after_each_player();
	}
	else if ((count % 4 == 0) && (input == "c1") && (c1.exist != false) && (c1.depart != false)) {
		move(dice_num, c1);
		screen_output_after_each_player();
	}
	else if ((count % 4 == 0) && (input == "c2") && (c2.exist != false) && (c2.depart != false)) {
		move(dice_num, c2);
		screen_output_after_each_player();
	}
	else if ((count % 4 == 0) && (input == "c3") && (c3.exist != false) && (c3.depart != false)) {
		move(dice_num, c3);
		screen_output_after_each_player();
	}
	else if ((count % 4 == 0) && (input == "c4") && (c4.exist != false) && (c4.depart != false)) {
		move(dice_num, c4);
		screen_output_after_each_player();
	}
	else {
		cout << "Invaild input! Penalize the player to lose this chance!" << endl;
		screen_output_after_each_player();
	}
}
