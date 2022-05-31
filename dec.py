# Rougepy-Engine: devnugget
# Game file

import rougepy;

running = True;

# Screen init --------------------------
rougepy._screen_size(10, 10);
rougepy._load_map_data();

while running:
    # Limit FPS ------------------------
    rougepy._set_frames_mode(10);
    # Updates --------------------------
    rougepy._update_player_pos();
    # Drawing --------------------------
    rougepy._draw_player();
    # Clearing frame  ------------------
    rougepy._clear_screen(0);
    print(rougepy.frame);
    # Frame increment ------------------
    rougepy.frame += 1;
    rougepy.frame_input = True; # Allow input only per frame

