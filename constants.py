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
        
gold_height = (255 / 2)
bronze_height = (110 / 2)

Richard = Robot(auto_start=True)
Data = data()

#io_board = Richard.ruggeduino
power_board = Richard.power_board
counter = 0
camera = Richard.camera
camera_bias = -(math.pi / 2)

motor_board = Richard.motor_boards["SR0WH1J"]
#utility_board = Richard.motor_boards["SR0JFG"]
#servo_board = Richard.servo_board
#camera_servo = servo_board.servos[0]

home_base_increment = 0

marker_positions = [[0, 718], [0, 1436], [0, 2154], [0, 2872], [0, 3590], [0, 4308], [0, 5026],
                    [718, 5744], [1436, 5744], [2154, 5744], [2872, 5744], [3590, 5744], [4308, 5744], [5026, 5744],
                    [5744, 5026], [5744, 4308], [5744, 3590], [5744, 2872], [5744, 2154], [5744, 1436], [5744, 718],
                    [5026, 0], [4308, 0], [3590, 0], [2872, 0], [2154, 0], [1436, 0], [718, 0]]

forward_power = 0.3
backward_power = 0.3
turn_power = 0.15

img_x, img_y = 2875 * 2, 2875 * 2

def drive_forward_time_est(distance):
    return (distance / 1000) * 2.95

def drive_backward_time_est(distance):
    return (distance / 1000) * 1

def drive_turn_time_est(angle):
    if (angle <= 45): return (angle / 45) * 1.4
    if (angle > 45): return (angle / 90) * 2.5
    return (angle / 90) * 2.14

