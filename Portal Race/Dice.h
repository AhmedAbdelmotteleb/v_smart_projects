#ifndef DICE_H
#define DICE_H
#include<iostream>
#include <vector>

class Dice {
private:
	std::string agent_colour;
	int dice_number_sides{};
	std::vector <int> dice_value;
	std::vector <int> dice_load;

public:
	Dice(const int dice_number_sides_input) {
		dice_number_sides = dice_number_sides_input;
		fill_values(dice_number_sides);
	}
	Dice(const int dice_number_sides_input, const std::vector<int>dice_load_input) {
		dice_number_sides = dice_number_sides_input;
		dice_load = dice_load_input;
		fill_values(dice_number_sides, dice_load);
	}
	~Dice() {}
	int roll_dice();
	void fill_values(int num_sides_input);
	void fill_values(int num_sides_input, std::vector <int> dice_load_input);
};

#endif