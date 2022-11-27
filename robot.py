
import math
import time

# Our custom librarys that deal with navigation and
# location tracking in the standard enviroment 
# as well as auto-callibration features for match day

from constants import *
import tracking
import movement
import calibration
import music
import image
import scripts



Data.x, Data.y, Data.bearing = tracking.get_position()
Data.target_x, Data.target_y, Data.target_bearing = 0, 0, 0
Data.home_base = Richard.zone

camera.save(Richard.usbkey / "IMG.png")
music.tune()

Richard.wait_start()

#scripts.l1_search_marker_display()
#scripts.l2_vision_challenge()
#scripts.l3_token_detection_challenge()
#scripts.l4_movement_challenge()
#scripts.l5_map_enviroment()
#scripts.l6_track_cube()
#scripts.l7_laps()
#scripts.l8_turn_camera()
scripts.l9_getdata(1)

tracking.set_camera_bearing(0)
time.sleep(2)
tracking.set_camera_bearing(90)
time.sleep(2)
tracking.set_camera_bearing(180)
time.sleep(2)
tracking.set_camera_bearing(270)
time.sleep(2)
tracking.set_camera_bearing(0)


music.shut_down()
