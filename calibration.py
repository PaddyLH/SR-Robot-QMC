import time

import constants
import movement
import tracking
import music

def forward_calib_marker():
    print("Starting Forward Cal")

    for power_level in range(20):
        power = (power_level + 1) / 20
    
        constants.forward_power = 0.3
        x,y,b = tracking.get_position()
        while (x == 0 and y == 0):
            movement.drive_forward(0.5)
            x,y,b = tracking.get_position()

        starting_position = [x,y]

        constants.forward_power = power
        movement.drive_forward(2)
        x,y,b = tracking.get_position()

        distance = (starting_position[0] - x)**2 + (starting_position[1] - y)**2
        distance = constants.math.sqrt(distance)

        print("Forward Cal, Power:",power,"Distance:",distance)

        constants.backward_power = power
        movement.drive_backward(2)
    print()

def forward_calib(t):
    music.tune1()
    saved_power = constants.forward_power
    for power_level in range(10):
        power = (power_level + 1) / 10
        constants.forward_power = power
        movement.drive_forward(t)
        time.sleep(6)
    constants.forward_power = saved_power


