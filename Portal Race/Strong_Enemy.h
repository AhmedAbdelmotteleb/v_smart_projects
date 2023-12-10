#ifndef STRONG_ENEMY_H
#define STRONG_ENEMY_H
#include<iostream>
#include <stdlib.h>
#include "Enemy.h" 
//derived from base class (Enemy)
class Strong_Enemy : public Enemy {
private:
	int health{ 2 };
	int damage{ 10 };
public:
	Strong_Enemy();
	~Strong_Enemy();

};
#endif
