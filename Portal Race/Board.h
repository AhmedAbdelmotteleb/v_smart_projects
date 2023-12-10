#ifndef BOARD_H
#define BOARD_H
#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <windows.h>

class Board {
private:
    std::string board_string = R"(
 _1_ _2_ _3_ _4_ _5_ _6_ _7_ _8_ _9_ 1_0
|   |   |   |   |   |   |   |   |   |   |
|___|___|___|___|___|___|___|___|___|___|
|   |   |   |   |   |   |   |   |   |   |
|___|___|___|___|___|___|___|___|___|___|
|   |   |   |   |   |   |   |   |   |   |
|___|___|___|___|___|___|___|___|___|___|
|   |   |   |   |   |   |   |   |   |   |
|___|___|___|___|___|___|___|___|___|___|
|   |   |   |   |   |   |   |   |   |   |
|___|___|___|___|___|___|___|___|___|___|
|   |   |   |   |   |   |   |   |   |   |
|___|___|___|___|___|___|___|___|___|___|
|   |   |   |   |   |   |   |   |   |   |
|___|___|___|___|___|___|___|___|___|___|
|   |   |   |   |   |   |   |   |   |   |
|___|___|___|___|___|___|___|___|___|___|
|   |   |   |   |   |   |   |   |   |   |
|___|___|___|___|___|___|___|___|___|___|
|   |   |   |   |   |   |   |   |   |   |
|___|___|___|___|___|___|___|___|___|___|
)";
    std::vector<std::vector<int>> block_positions;
    std::vector<int> mystery_positions;
    std::vector<int> enemies_positions;
    std::vector<int> portals_positions;
    std::vector<int> red_positions;
    std::vector<int> blue_positions;
    std::vector<int> green_positions;
    std::vector<int> yellow_positions;
    int char_value = 0;
    int line_value = 0; //start from line 1
    int block_value = 0;
    unsigned char empty_char = 219;
    HANDLE hconsole;

public:
    Board();

    void intialise_block_positions();
    void print_board();
    void add_to_colour(std::vector<int> input, char colour);
    void randomise_mystery();
    void randomise_enemies();
    void randomise_portals();
    void colourise_blocks();
    char move_player(int initial_position, int final_position, char agent_char);
    std::vector<int> get_mystery_positions();
    std::vector<int> get_enemies_positions();
    std::vector<int> get_portals_positions();


};
#endif