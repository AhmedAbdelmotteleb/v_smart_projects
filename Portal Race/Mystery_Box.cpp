#include "Mystery_Box.h"
#include <stdlib.h>
#include <time.h>
#include <iostream>
#include <vector>

Mystery_Box::Mystery_Box() {}
Mystery_Box::~Mystery_Box() {}

std::array<int, 2> Mystery_Box::reward() {
	std::array<int, 2> returned_value; //dynamic he5a
	srand(time(NULL)); //initialize the random seed
	int ammo_or_health = rand() % 2; //generates a random number from the array
	const int reward_value[] = { 2, 2, -2 };
	int reward_choice = rand() % 3;
	returned_value[0] = ammo_or_health == 1 ? 1 : 2;
	returned_value[1] = reward_value[reward_choice];
	std::cout << "zebby zalabya: " << returned_value[1] << std::endl;
	return returned_value;
}


//		std::cout << R"(
//*******************************************************************************
//          |                   |                  |                     |       
// _________|________________.=""_;=.______________|_____________________|_______
//|                   |  ,-"_,=""     `"=.|                  |                   
//|___________________|__"=._o`"-._        `"=.______________|___________________
//          |                `"=._o`"=._      _`"=._                     |       
// _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
//|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |                   
//|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
//          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |       
// _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
//|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |                   
//|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
//____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
///______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
//____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
///______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
//____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
///______/______/______/______/______/______/______/______/______/______/______/_
//*******************************************************************************
//    )" << std::endl;