
import math
import time

# Our custom librarys that deal with navigation and
# location tracking in the stand enviroment

import tracking
import constants
import movement
import calibration
import music

Rich = constants.Richard2
Bot = constants.Data

Bot.x, Bot.y, Bot.bearing = tracking.get_position()
Bot.target_x, Bot.target_y, Bot.target_bearing = 0, 0, 0
Bot.home_base = Rich.zone()

movement.stop()
music.wake_up()

Rich.wait_start()

#calibration.forward_calib_marker()

movement.drive_forward(2)
movement.drive_left(2)
movement.drive_right(2)
movement.drive_backward(2)

music.shut_down()