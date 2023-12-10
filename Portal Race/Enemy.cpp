#include "Enemy.h"
#include <iostream>

Enemy::Enemy(int health_input, int damage_input) {
	health = health_input;
	damage = damage_input;
}
Enemy::~Enemy() {}

