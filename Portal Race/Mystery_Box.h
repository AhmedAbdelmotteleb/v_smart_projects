//this is the mystery box header file

#ifndef MYSTERY_BOX_H
#define MYSTERY_BOX_H
#include<iostream>
#include<array>

class Mystery_Box {
public:
	Mystery_Box();
	~Mystery_Box();

	std::array<int, 2> reward(); //dynamic int array

};
#endif