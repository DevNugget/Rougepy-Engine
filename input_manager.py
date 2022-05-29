import keyboard

def _check_input(xp, yp):
    if keyboard.is_pressed("d"):
        xp += 1