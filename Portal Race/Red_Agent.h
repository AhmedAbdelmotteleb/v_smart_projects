//this is the red agent header file
//it contains the derived class specifications using the abstract components class

#ifndef RED_AGENT_H
#define RED_AGENT_H
#include<iostream>
#include <stdlib.h>
#include <time.h>
#include "Agent.h" 
//derived from base class (Agent)
class Red_Agent : public Agent {
private:
	std::string colour{ "red" };
	int health{ 17 };
	int current_ammo{ 2 };
	int max_ammo{ 5 };
	int retreat_number{ 1 };
	int dice_number_sides{ 5 };
	std::vector <int> dice_load{ 3,4 };
public:
	//agents(string agent_colour_input, double health_input, double max_ammo_number_input, double max_retreat_number_input)
	Red_Agent();
	~Red_Agent();
};
#endif