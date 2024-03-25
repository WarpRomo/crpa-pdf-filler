# Code to check if left or right mouse buttons were pressed
import win32api
from ctypes import windll, Structure, c_long, byref

import time

state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128


relative = (0,0);

lower_factor = 1.0;

def get_mouse_pos():
    return win32api.GetCursorPos()


i = 0;

while True:
    a = win32api.GetKeyState(0x01)
    b = win32api.GetKeyState(0x02)

    if a != state_left:  # Button state changed
        state_left = a
        if a < 0:
            pos = get_mouse_pos();


            adjusted = [pos[0] - relative[0], pos[1] - relative[1]];

            adjusted[0] *= lower_factor;
            adjusted[1] *= -lower_factor;

            adjusted[0] = int(adjusted[0]);
            adjusted[1] = int(adjusted[1]);

            print( "{'coordinates': (" + str(adjusted[0]) + "," + str(adjusted[1]) + "), 'value': '" + str(i) + "', 'color': colors[0]}," );

            i += 1;






    if b != state_right:  # Button state changed
        state_right = b
        if b < 0:
            relative = get_mouse_pos();

    time.sleep(0.001)