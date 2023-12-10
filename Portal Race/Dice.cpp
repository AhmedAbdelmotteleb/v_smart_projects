#include "Dice.h"
#include <stdlib.h>
#include <time.h>
#include <iostream>

//Function to roll a random number based on the colour of the character
int Dice::roll_dice() {
	srand(time(NULL)); //initialize the random seed
	int rolled_number = rand() % dice_value.size(); //generates a random number from the array
	return dice_value[rolled_number];
}

void Dice::fill_values(int dice_number_sides_input) {
	for (int element{}; element < dice_number_sides_input; element++) {
		dice_value.push_back(element + 1); //to start from 1 instead of 0
	}
	//for (int element{}; element < dice_value.size(); element++) {
	//	std::cout << dice_value[element] << std::endl; //to start from 1 instead of 0
	//}
}

//overwrite the function to create unfair dice, previous function was a fair dice
void Dice::fill_values(int dice_number_sides_input, std::vector <int> dice_load_input) {
	fill_values(dice_number_sides_input); //call previous function
	dice_value.insert(dice_value.end(), dice_load.begin(), dice_load.end());
	//concatenating loads with normal values. Now, certain values are repeated and have higher probability of getting called ->unfair dice
	//for (int element{}; element < dice_value.size(); element++) {
	//	std::cout << dice_value[element] << std::endl; //to start from 1 instead of 0
	//}
}