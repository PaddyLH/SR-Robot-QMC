from sr.robot3 import *
import math 
import time

# Add different stage enums here
IDLE = 0

class data:
    def __init__(self):
        self.home_base = 0

        self.x = 0
        self.y = 0
        self.bearing = 0

        self.target_x = 0
        self.target_y = 0
        self.target_bearing = 0

        self.mode = IDLE
        

Richard2 = Robot(auto_start=True)
Data = data()

io_board = Richard2.ruggeduino
power_board = Richard2.power_board

camera = Richard2.camera
camera_bias = 0

motor_board = Richard2.motor_board
#utitlity_board = Richard2.motor_boards[""]

home_base_increment = 0

marker_positions = [[0, 718], [0, 1436], [0, 2154], [0, 2872], [0, 3590], [0, 4308], [0, 5026],
                    [718, 5744], [1436, 5744], [2154, 5744], [2872, 5744], [3590, 5744], [4308, 5744], [5026, 5744],
                    [5744, 5026], [5744, 4308], [5744, 3590], [5744, 2872], [5744, 2154], [5744, 1436], [5744, 718],
                    [5026, 0], [4308, 0], [3590, 0], [2872, 0], [2154, 0], [1436, 0], [718, 0]]

forward_power = 0.5
backward_power = 0.4
turn_power = 0.3



def drive_forward_time_est(distance):
    return distance / (forward_power / 0.5 * 1200)

def drive_backward_time_est(distance):
    return distance / (backward_power / 0.4 * 1000)

def drive_turn_time_est(angle):
    return angle / (turn_power / 0.3 * 90)

