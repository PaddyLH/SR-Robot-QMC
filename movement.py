
import time
import constants

motor_board = constants.motor_board
#servo_board = constants.servo_board

def forward(power):
    motor_board.motors[0].power = -power
    motor_board.motors[1].power = power

def backward(power):
    motor_board.motors[0].power = power
    motor_board.motors[1].power = -power

def left(power):
    motor_board.motors[0].power = power
    motor_board.motors[1].power = power

def right(power):
    motor_board.motors[0].power = -power
    motor_board.motors[1].power = -power

def stop():
    motor_board.motors[0].power = 0
    motor_board.motors[1].power = 0

def drive_forward(seconds):
    forward(constants.forward_power)
    time.sleep(seconds)
    stop()

def drive_backward(seconds):
    backward(constants.backward_power)
    time.sleep(seconds)
    stop()

def drive_left(seconds):
    left(constants.turn_power)
    time.sleep(seconds)
    stop()

def drive_right(seconds):
    right(constants.turn_power)
    time.sleep(seconds)
    stop()

def drive_left_a(angle):
    left(constants.turn_power)
    time.sleep(constants.drive_turn_time_est(angle))
    stop()

def drive_right_a(angle):
    right(constants.turn_power)
    time.sleep(constants.drive_turn_time_est(angle))
    stop()

def drive_forward_d(distance):
    forward(constants.forward_power)
    time.sleep(constants.drive_forward_time_est(distance))
    stop()


def check_interupt():
    mode = constants.Data.mode

    # this will check the sensors for a drive cancel 
    return False

def careful_drive_forward(distance):
    endTime = time.time() + constants.drive_forward_time_est(distance)
    interupted = False
    while True:
        forward()
        if (time.time() > endTime) or check_interupt():
            interupted = True
            break
    stop()

    return interupted
    
def smart_turn(angle):
    # angle needs to have -negative being left
    # and positive being right

    right_angle = angle % 360
    left_angle = 360 - angle

    if right_angle < left_angle: 
        drive_right_a(right_angle)
    else:
        drive_left_a(left_angle)



