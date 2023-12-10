#include "Yellow_Agent.h"
#include <stdlib.h>
#include <time.h>
#include <iostream>

Yellow_Agent::Yellow_Agent() : Agent(colour, health, current_ammo, max_ammo, retreat_number) {
    agent_dice = new Dice{ dice_number_sides };
}
Yellow_Agent::~Yellow_Agent() {}