//this is the green agent header file
//it contains the derived class specifications using the abstract components class

#ifndef GREEN_AGENT_H
#define GREEN_AGENT_H
#include<iostream>
#include <stdlib.h>
#include <time.h>
#include "Agent.h" 
//derived from base class (Agent)
class Green_Agent : public Agent {
private:
	std::string colour{ "green" };
	int health{ 10 };
	int current_ammo{ 1 };
	int max_ammo{ 3 };
	int retreat_number{ 4 };
	int dice_number_sides{ 6 };
public:
	//agents(string agent_colour_input, double health_input, double max_ammo_number_input, double max_retreat_number_input)
	Green_Agent();
	~Green_Agent();

	void set_position(int move_value);
	int get_position();
	bool attack(int thug_health);
	bool retreat();
	void check_win();
	void check_loss();

};
#endif