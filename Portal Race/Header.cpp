//this is the implementation file
//it contains the method definitions
#include "Header.h"
#include <iostream>

//================================= Return representation
void complex::representation() const {
    if (imaginary_part > 0) {
        std::cout << "Representation = " << real_part << " + " << imaginary_part << "i" << std::endl;
    }
    else {
        std::cout << "Representation = " << real_part << " - " << abs(imaginary_part) << "i" << std::endl;
    }
}