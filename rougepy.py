import os;
import sys;
import player;
import input_manager;
from time import sleep
from unittest import case;

gen_table_1 = [
    ".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
];
gen_table_2 = [
    ".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
];
gen_table_3 = [
    ".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
];
gen_table_4 = [
    ".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
];
gen_table_5 = [
    ".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
];
gen_table_6 = [
    ".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
];

scanline_1 = [
    ".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
];
scanline_2 = [
    ".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
];
scanline_3 = [
    ".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
];
scanline_4 = [
    ".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
];
scanline_5 = [
    ".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
];
scanline_6 = [
    ".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
];

frame = 0;

def clear_scanlines(exception):
    match exception:
        case 1:
            gen_table_2 = scanline_2;
            gen_table_3 = scanline_3;
            gen_table_4 = scanline_4;
            gen_table_5 = scanline_5;
            gen_table_6 = scanline_6;
        case 2:
            gen_table_1 = scanline_2;
            gen_table_3 = scanline_3;
            gen_table_4 = scanline_4;
            gen_table_5 = scanline_5;
            gen_table_6 = scanline_6;
        case 3:
            gen_table_1 = scanline_2;
            gen_table_3 = scanline_3;
            gen_table_4 = scanline_4;
            gen_table_5 = scanline_5;
            gen_table_6 = scanline_6;
        case 4:
            gen_table_1 = scanline_2;
            gen_table_2 = scanline_3;
            gen_table_3 = scanline_4;
            gen_table_5 = scanline_5;
            gen_table_6 = scanline_6;
        case 5:
            gen_table_1 = scanline_1;
            gen_table_2 = scanline_2;
            gen_table_3 = scanline_3;
            gen_table_4 = scanline_4;
            gen_table_6 = scanline_6;
        case 6:
            gen_table_1 = scanline_1;
            gen_table_2 = scanline_2;
            gen_table_3 = scanline_3;
            gen_table_4 = scanline_4;
            gen_table_5 = scanline_5;

def _draw_player():
    if player.pos_y == 0:
        gen_table_1[player.pos_x] = player.character;
        clear_scanlines(1);
    elif player.pos_y == 1:
        gen_table_2[player.pos_x] = player.character;
        clear_scanlines(2);
    elif player.pos_y == 2:
        gen_table_3[player.pos_x] = player.character;
        clear_scanlines(3);
    elif player.pos_y == 3:
        gen_table_4[player.pos_x] = player.character;
        clear_scanlines(4);
    elif player.pos_y == 4:
        gen_table_5[player.pos_x] = player.character;
        clear_scanlines(5);
    elif player.pos_y == 5:
        gen_table_6[player.pos_x] = player.character;
        clear_scanlines(6);

def _update_player_pos():
    input_manager._check_input(player.pos_x, player.pos_y)

def _60_frames_mode():
    sleep(0.01667);

def _print_ripple():
    print(*gen_table_1);
    print(*gen_table_2);
    print(*gen_table_3);
    print(*gen_table_4);
    print(*gen_table_5);
    print(*gen_table_6);

def _clear_screen():
    os.system("clear");
    _print_ripple();
    sys.stdout.write(str(frame));
    sys.stdout.write("\n");