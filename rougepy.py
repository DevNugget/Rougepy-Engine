# Rougepy-Engine: devnugget\
# Main library

import os;
import sys;
import player;
import wall;
import map_data;
import keyboard;
from time import sleep;

colliders = ["WALL"];

# Screen size, visuals depends on terminal char size
screen_w = 0;
screen_h = 0;

frame_input = True; # Per frame input check

# gen_tables is a dictionary which holds the data for
# each individual line drawn vertically and build the canvas
# ex:
# gen_tables[1] = [".", ".", "."]
# gen_tables[2] = [".", ".", "."]
# gen_tables[3] = [".", ".", "."]
gen_tables = {};

identity_tables = {};

frame = 0; # General purpose frame counter

# Allows to change char that represents player
# via main (dec.py) file
def _change_player_char(char):
    player.character = char;

# Creates verticle/horizontal chars to create canvas
# This adapts with the screen size provided
def _generate_gen_tables():
    for i in range(0, screen_h):
        gen_table = [];
        for j in range(0, screen_w):
            gen_table.append(".");
        gen_tables[i] = gen_table;

# Identity tables store the tag given to a specific object
# AIR = Free space for player to move
# PLAYER = player
def _generate_identity_tables():
    for i in range(0, screen_h):
        iden_table = [];
        for j in range(0, screen_w):
            iden_table.append("AIR");
        identity_tables[i] = iden_table;

# Reset all gen tables
def _clear_gen_table():
    for i in range(0, screen_h):
        for j in range(0, len(gen_tables[i])):
            if gen_tables[i][j] == player.character:
                gen_tables[i][j] = ".";

# Reset identity table which is the pos of player
def _clear_identity_table():
    for i in range(0, screen_h):
        for j in range(0, len(identity_tables[i])):
            if identity_tables[i][j] == player.ID:
                identity_tables[i][j] = "AIR";

# Draws player at appropriate location
def _draw_player():
    _clear_gen_table(); # Clearing previous draw
    _clear_identity_table(); # CLearing previous player identity table
    gen_tables[player.pos_y][player.pos_x] = player.character;
    identity_tables[player.pos_y][player.pos_x] = player.ID;

# Updating player after input
def _update_player_pos():
    global frame_input, screen_h, screen_w
    if frame_input == True: # Frame input check
        if keyboard.is_pressed("d"):
            if player.pos_x < screen_w - 1: # Boundry check (adapts to screen size)
                if identity_tables[player.pos_y][player.pos_x+1] not in colliders:
                    player.pos_x += 1;
                    frame_input = False;
        if keyboard.is_pressed("a"):
            if player.pos_x > 0:            # Boundry check (adapts to screen size)
                if identity_tables[player.pos_y][player.pos_x-1] not in colliders:
                    player.pos_x -= 1;
                    frame_input = False;
        if keyboard.is_pressed("w"):
            if player.pos_y > 0:            # Boundry check (adapts to screen size)
                if identity_tables[player.pos_y-1][player.pos_x] not in colliders:
                    player.pos_y -= 1;
                    frame_input = False;
        if keyboard.is_pressed("s"):
            if player.pos_y < screen_h - 1: # Boundry check (adapts to screen size)
                if identity_tables[player.pos_y+1][player.pos_x] not in colliders:
                    player.pos_y += 1;
                    frame_input = False;

# Print all the gen tables, essentially the draw canvas
def _display_canvas():
    for i in range(0, screen_h):
        print(*gen_tables[i]);

def _display_identity_tables():
    for i in range(0, screen_h):
        print(*identity_tables[i]);

# Sets the screen size
def _screen_size(w, h):
    global screen_h, screen_w;
    screen_w = w;
    screen_h = h;

# Redraw/Update screen everyframe
def _clear_screen(mode = 0):
    os.system("clear");
    if mode == 0: _display_canvas();
    else: _display_identity_tables();
    sys.stdout.write(str(frame));
    sys.stdout.write("\n");

# Enables frames per second shifting
def _set_frames_mode(fps):
    delay = round(1000/fps, 5)/1000;
    sleep(delay);

def _create_wall(xp, yp):
    gen_tables[yp][xp] = wall.character;
    identity_tables[yp][xp] = wall.ID;

def _load_map_data():
    _generate_gen_tables();
    _generate_identity_tables();
    for i in range(0, screen_h):
        for j in range(0, len(map_data.map_index[i])):
            if map_data.map_index[i][j] == 1:
                _create_wall(j, i);
            elif map_data.map_index[i][j] == 2:
                player.pos_x, player.pos_y = j, i;
