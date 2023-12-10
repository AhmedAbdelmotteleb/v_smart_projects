#include "Portal.h"
#include <stdlib.h>
#include <time.h>
#include <iostream>

//if you teleport with portal, link it to new position function
int Portal::teleport() {
	srand(time(NULL));
	int teleport_value = rand() % (15 - 4) + 4;
	std::cout << "teleport value: " << teleport_value << std::endl;
	return teleport_value;
}