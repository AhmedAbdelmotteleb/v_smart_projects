//this is the yellow agent header file
//it contains the derived class specifications using the abstract components class

#ifndef YELLOW_AGENT_H
#define YELLOW_AGENT_H
#include<iostream>
#include <stdlib.h>
#include <time.h>
#include "Agent.h" 
//derived from base class (Agent)
class Yellow_Agent : public Agent {
private:
	std::string colour{ "yellow" };
	int health{ 9 };
	int current_ammo{ 1 };
	int max_ammo{ 3 };
	int retreat_number{ 2 };
	int dice_number_sides{ 10 };
public:
	//agents(string agent_colour_input, double health_input, double max_ammo_number_input, double max_retreat_number_input)
	Yellow_Agent();
	~Yellow_Agent();
	void set_position(int move_value);
	int get_position();
	bool attack(int thug_health);
	bool retreat();
	void check_win();
	void check_loss();

};
#endif