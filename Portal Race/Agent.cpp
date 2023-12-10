#include "Agent.h"
#include <stdlib.h>
#include <iostream>

void Agent::set_position(int move_value) {
    position += move_value;
}
int Agent::get_position() { return position; }
bool Agent::attack(int thug_health) {
    if (current_ammo >= thug_health) {
        current_ammo -= thug_health;
        return true;
    }
    else { return false; }
}
bool Agent::retreat() {
    if (retreat_number > 0) {
        retreat_number--;
        set_position(-agent_dice->roll_dice());
        return true;
    }
    else { return false; }
}
void Agent::check_win() {
    if (get_position() >= 100) {
        exit(-1);
    }
}
void Agent::check_loss() {
    if (health <= 0) {
        std::cout << R"(
 /  _____/_____    _____   ____   \_____  \___  __ ___________ 
/   \  ___\__  \  /     \_/ __ \   /   |   \  \/ // __ \_  __ \
\    \_\  \/ __ \|  Y Y  \  ___/  /    |    \   /\  ___/|  | \/
 \______  (____  /__|_|  /\___  > \_______  /\_/  \___  >__|   
        \/     \/      \/     \/          \/          \/       
         .e$$$$e.
       e$$$$$$$$$$e
      $$$$$$$$$$$$$$
     d$$$$$$$$$$$$$$b
     $$$$$$$$$$$$$$$$
    4$$$$$$$$$$$$$$$$F
    4$$$$$$$$$$$$$$$$F
     $$$" "$$$$" "$$$
     $$F   4$$F   4$$
     '$F   4$$F   4$"
      $$   $$$$   $P
      4$$$$$"^$$$$$%
       $$$$F  4$$$$
        "$$$ee$$$"
        . *$$$$F4
         $     .$
         "$$$$$$"
          ^$$$$
 4$$c       ""       .$$r
 ^$$$b              e$$$"
 d$$$$$e          z$$$$$b
4$$$*$$$$$c    .$$$$$*$$$r
 ""    ^*$$$be$$$*"    ^"
          "$$$$"
        .d$$P$$$b
       d$$P   ^$$$b
   .ed$$$"      "$$$be.
 $$$$$$P          *$$$$$$
4$$$$$P            $$$$$$"
 "*$$$"            ^$$P
    ""              ^"
)" << std::endl;
    }
}