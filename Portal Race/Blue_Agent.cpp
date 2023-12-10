#include "Blue_Agent.h"
#include <stdlib.h>
#include <time.h>
#include <iostream>

Blue_Agent::Blue_Agent() : Agent(colour, health, current_ammo, max_ammo, retreat_number) {
    agent_dice = new Dice{ dice_number_sides,dice_load };
    std::cout << colour << std::endl;
    std::cout << health << std::endl;
}
Blue_Agent::~Blue_Agent() {}