//this is the blue agent header file
//it contains the derived class specifications using the abstract components class

#ifndef BLUE_AGENT_H
#define BLUE_AGENT_H
#include<iostream>
#include <stdlib.h>
#include <time.h>
#include "Agent.h" 
//derived from base class (Agent)
class Blue_Agent : public Agent {
private:
	std::string colour{ "blue" };
	int health{ 8 };
	int current_ammo{ 1 };
	int max_ammo{ 2 };
	int retreat_number{ 5 };
	int dice_number_sides{ 6 };
	std::vector <int> dice_load{ 3,4 };
public:
	//agents(string agent_colour_input, double health_input, double max_ammo_number_input, double max_retreat_number_input)
	Blue_Agent(); 
	~Blue_Agent();
	void set_position(int move_value);
	int get_position();
	bool attack(int thug_health);
	bool retreat();
	void check_win();
	void check_loss();

};
#endif