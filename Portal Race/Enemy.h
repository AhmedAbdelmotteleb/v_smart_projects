//this is the Enemy header file

#ifndef ENEMY_H
#define ENEMY_H
#include<iostream>

class Enemy {
protected:
	int health;
	int damage;
public:
	Enemy(int health_input, int damage_input);
	~Enemy();
};
#endif