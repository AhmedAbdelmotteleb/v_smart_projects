#include "Green_Agent.h"
#include <stdlib.h>
#include <time.h>
#include <iostream>

Green_Agent::Green_Agent() : Agent(colour, health, current_ammo, max_ammo, retreat_number) {
    agent_dice = new Dice{ dice_number_sides };
}
Green_Agent::~Green_Agent() {}