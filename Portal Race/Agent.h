//this is the components header file
//it contains the abstract class specifications

#ifndef AGENT_H
#define AGENT_H
#include <iostream>
#include "Dice.h"
#include <memory>
//abstract class that only has basic shared functions for all derived classes to come 
class Agent {
protected:
	//variables are protected so that they can shared with all derived classes
	std::string agent_colour;
	unsigned int health{};
	int current_ammo{};
	int max_ammo_number{};
	int retreat_number{};
	int position = 1;
	Dice* agent_dice{};
	//std::unique_ptr<dice> agent_dice = std::make_unique<dice>(); //safer method to deal with exceptions as not to have memory leaks
	//however, seems like i can't use a smart pointer here because a smart pointer implies ownership, since dice is in a different class then it prob won't work.

public:
	//parameterised constructor takes in the agent's colour and their features
	Agent(const std::string agent_colour_input, const int health_input, const int current_ammo_input, const int max_ammo_number_input, const int retreat_number_input) {
		agent_colour = agent_colour_input;
		health = health_input;
		current_ammo = current_ammo_input;
		max_ammo_number = max_ammo_number_input;
		retreat_number = retreat_number_input;
	}
	//pure virtual functions to be used in the derived classes
	void set_position(int move_value);
	int get_position();
	bool attack(int thug_health);
	//virtual int next_same_coloured_square() = 0;
	bool retreat();
	void check_win();
	void check_loss();
	//virtual destructor useful if we want to delete an instance of a derived class through a pointer to the base class
	virtual ~Agent() {}

};


#endif
