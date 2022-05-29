
import rougepy;

running = True;

while running:
    rougepy._60_frames_mode();
    rougepy._update_player_pos();
    rougepy._draw_player();
    rougepy._clear_screen();
    print(rougepy.frame);
    rougepy.frame += 1;

