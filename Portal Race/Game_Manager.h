#ifndef GAME_MANAGER_H
#define GAME_MANAGER_H
#include <iostream>
#include <vector>
#include <map>

#include "Agent.h"
#include"Blue_Agent.h"
#include "Board.h"
#include "Dice.h"
#include "Enemy.h"
#include "Green_Agent.h"
#include "Mystery_Box.h"
#include "Portal.h"
#include "Red_Agent.h"
#include "Strong_Enemy.h"
#include "Weak_Enemy.h"
#include "Yellow_Agent.h"

class Game_Manager {
private:
	Board board;
	Red_Agent red;
	Blue_Agent blue;
	Green_Agent green;
	Yellow_Agent yellow;
	std::vector <Agent> available_agents;
	std::vector <Agent> chosen_agents;
	int number_of_players;
	std::map <int, Enemy> enemies;
	std::map <int, Portal> portals;
	std::map <int, Mystery_Box> mystery_boxes;


public:
	void initialise_game();
	void turn();
	void start_game();
	void end_game();

};

#endif