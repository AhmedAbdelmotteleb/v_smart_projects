#include "Red_Agent.h"
#include <stdlib.h>
#include <time.h>
#include <iostream>

Red_Agent::Red_Agent() : Agent(colour, health, current_ammo, max_ammo, retreat_number) {
    agent_dice = new Dice{ dice_number_sides,dice_load };
}
Red_Agent::~Red_Agent() {}