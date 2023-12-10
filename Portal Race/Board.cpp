#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <windows.h>
#include <ctime>
#include "Board.h"

Board::Board() {
    hconsole = GetStdHandle(STD_OUTPUT_HANDLE);
    intialise_block_positions();
    randomise_mystery();
    randomise_enemies();
    colourise_blocks();
    print_board();
}

void Board::intialise_block_positions() {
    for (int i{}; i < board_string.size(); i++) {
        char_value++; //count each character 
             //essentially while not at the end of the line
        if (board_string[i] == '\n') {
            line_value++;
        }
        //if you encounter a wall and if after the wall the line doesn't end (border wall)
        else if (board_string[i] == '|' && board_string[i + 1] != '\n') {
            board_string[i + 1] = empty_char;
            board_string[i + 2] = empty_char;
            board_string[i + 3] = empty_char;
            if (line_value % 2 == 0) {
                std::vector<int> v2;
                v2.push_back(char_value);
                v2.push_back(char_value + 1);
                v2.push_back(char_value + 2);
                v2.push_back(char_value + 42);
                v2.push_back(char_value + 43);
                v2.push_back(char_value + 44);
                block_positions.push_back(v2);
                block_value++;
            }
        }
    }
    board_string[877] = 'E';
    board_string[878] = 'N';
    board_string[879] = 'D';

}
/*
The different color codes are

0   BLACK
1   BLUE
2   GREEN
3   CYAN
4   RED
5   MAGENTA
6   BROWN
7   LIGHTGRAY
8   DARKGRAY
9   LIGHTBLUE
10  LIGHTGREEN
11  LIGHTCYAN
12  LIGHTRED
13  LIGHTMAGENTA
14  YELLOW
15  WHITE
*/
void Board::print_board() {
    for (int i{}; i < board_string.size(); i++) {
        if (std::find(std::begin(red_positions), std::end(red_positions), i) != std::end(red_positions)) {
            SetConsoleTextAttribute(hconsole, 12);
        }
        else if (std::find(std::begin(blue_positions), std::end(blue_positions), i) != std::end(blue_positions)) {
            SetConsoleTextAttribute(hconsole, 9);
        }
        else if (std::find(std::begin(green_positions), std::end(green_positions), i) != std::end(green_positions)) {
            SetConsoleTextAttribute(hconsole, 2);
        }
        else if (std::find(std::begin(yellow_positions), std::end(yellow_positions), i) != std::end(yellow_positions)) {
            SetConsoleTextAttribute(hconsole, 14);
        }
        else {
            SetConsoleTextAttribute(hconsole, 15);
        }
        std::cout << board_string[i];
        SetConsoleTextAttribute(hconsole, 15);
    }
}


void Board::randomise_mystery() {
    srand(time(NULL));
    int rand1 = (rand() % (25 - 15)) + 15;
    board_string[block_positions[rand1][1]] = '?';
    board_string[block_positions[rand1][4]] = '?';
    int rand2 = (rand() % (55 - 45)) + 45;
    board_string[block_positions[rand2][1]] = '?';
    board_string[block_positions[rand2][4]] = '?';
    int rand3 = (rand() % (85 - 75)) + 75;
    board_string[block_positions[rand3][1]] = '?';
    board_string[block_positions[rand3][4]] = '?';
    mystery_positions.push_back(rand1);
    mystery_positions.push_back(rand2);
    mystery_positions.push_back(rand3);
}

void Board::randomise_enemies() {
    srand(time(NULL));
    for (int i = 1; i < 101; i += 10) {
        int random;
        do {
            random = (rand() % 9) + i;
        } while (std::find(mystery_positions.begin(), mystery_positions.end(), i) != mystery_positions.end());
        enemies_positions.push_back(random);
    }
}

void Board::randomise_portals() {
    srand(time(NULL));
    for (int i = 1; i < 101; i += 10) {
        int random;
        do {
            random = (rand() % 9) + i;
        } while ((std::find(mystery_positions.begin(), mystery_positions.end(), i) != mystery_positions.end() ||
            (std::find(enemies_positions.begin(), enemies_positions.end(), i) != enemies_positions.end())));
        portals_positions.push_back(random);
    }
}

void Board::add_to_colour(std::vector<int> input, char colour) {
    switch (colour) {
    case 'R':
        red_positions.insert(red_positions.end(), input.begin(), input.end());
        break;
    case 'G':
        green_positions.insert(green_positions.end(), input.begin(), input.end());
        break;
    case 'B':
        blue_positions.insert(blue_positions.end(), input.begin(), input.end());
        break;
    case 'Y':
        yellow_positions.insert(yellow_positions.end(), input.begin(), input.end());
        break;
    default:
        std::cout << "ERROR";
    }
}
void Board::colourise_blocks() {
    srand(time(NULL));
    int colour_position = rand() % 4;
    for (int i = 1; i < (block_positions.size() - 1); i++) {
        if (std::find(mystery_positions.begin(), mystery_positions.end(), i) != mystery_positions.end()) {
            colour_position = (colour_position + 1) % 4;
            continue;
        }
        switch (colour_position)
        {
        case 0:
            add_to_colour(block_positions[i], 'R');
            break;
        case 1:
            add_to_colour(block_positions[i], 'G');
            break;
        case 2:
            add_to_colour(block_positions[i], 'B');
            break;
        case 3:
            add_to_colour(block_positions[i], 'Y');
            break;
        default:
            std::cout << "ERROR " << colour_position << std::endl;
            break;
        }
        colour_position = (colour_position + 1) % 4;
    }
}

char Board::move_player(int initial_position, int final_position, char agent_char) {
    board_string[block_positions[initial_position][0]] = empty_char;
    board_string[block_positions[final_position][0]] = agent_char;
    if (std::find(mystery_positions.begin(), mystery_positions.end(), final_position) != mystery_positions.end()) {
        return 'm';
    }
    else if (std::find(enemies_positions.begin(), enemies_positions.end(), final_position) != enemies_positions.end()) {
        return 'e';
    }
    else if (std::find(portals_positions.begin(), portals_positions.end(), final_position) != portals_positions.end()) {
        return 'p';
    }
    else if (final_position == 0) { return 'w'; }
    else {
        return 'n';
    }
}

std::vector<int> Board::get_mystery_positions() { return mystery_positions; }

std::vector<int> Board::get_enemies_positions() { return enemies_positions; }

std::vector<int> Board::get_portals_positions() { return portals_positions; }