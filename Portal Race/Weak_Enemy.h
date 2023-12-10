#ifndef WEAK_ENEMY_H
#define WEAK_ENEMY_H
#include<iostream>
#include <stdlib.h>
#include "Enemy.h" 
//derived from base class (Enemy)
class Weak_Enemy : public Enemy {
private:
	int health{ 1 };
	int damage{ 5 };
public:
	Weak_Enemy();
	~Weak_Enemy();
};
#endif