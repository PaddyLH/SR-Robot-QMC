from numpy import exp, array, dot
import math
import time

from constants import *
import tracking
import movement
import calibration
import music
import image



def l1_search_marker_display():
    while True:
        Data.x, Data.y, Data.bearing = tracking.get_position()
        d,a,g,v = tracking.get_closest_token()

        if (not v): print("No Tokens")
        elif g: print("Gold")
        else: print("Bronze/Silver")
        print("-------------------")

        Richard.wait_start()

def l2_vision_challenge():
    mode = 1
    l = 0
    while True:
        Richard.wait_start()
        l += 1
        x,y,o = tracking.get_position()
        x -= 50

        x_target = 1436
        o_target = 180
        o_diff = o_target - o
        x_diff = x_target - x
        print(x_diff, o_diff)

        Richard.kch.leds[UserLED.A] = Colour.OFF
        Richard.kch.leds[UserLED.B] = Colour.OFF
        Richard.kch.leds[UserLED.C] = Colour.OFF

        if mode == 1:
            if x_diff < -200:
                Richard.kch.leds[UserLED.A] = Colour.RED
            elif x_diff > 200:
                Richard.kch.leds[UserLED.C] = Colour.RED
            else:
                Richard.kch.leds[UserLED.B] = Colour.BLUE

        if mode == 2:
            if o_diff > 32: # 30 deg left
                Richard.kch.leds[UserLED.A] = Colour.BLUE
            elif o_diff < -32: # 30 deg right
                Richard.kch.leds[UserLED.C] = Colour.BLUE
            else: # -30 < o < 30
                Richard.kch.leds[UserLED.B] = Colour.BLUE

        if l >= 6: mode = 2

def l3_token_detection_challenge():
    while True:
        dist, ang, is_gold, is_there = tracking.get_closest_token()
        if is_there == False: print("No Tokens Found")
        else:
            if is_gold: print("Closest is Gold")
            else: print ("Closest is Bronze/Silver")
        print("D2",dist,ang,is_gold,is_there)

        Richard.kch.leds[UserLED.A] = Colour.OFF
        Richard.kch.leds[UserLED.C] = Colour.OFF
        if is_there:
            if is_gold:
                Richard.kch.leds[UserLED.C] = Colour.CYAN
            else:
                Richard.kch.leds[UserLED.A] = Colour.CYAN
        Richard.wait_start()

def l4_movement_challenge():
    for i in range(3):
        movement.drive_forward_d(1000)
        movement.drive_left_a(90 + 45)
        movement.drive_forward_d(math.sqrt(2000000))
        movement.drive_left_a(90 + 45)
        movement.drive_forward_d(1000)
        movement.drive_left_a(90)

def l5_map_enviroment():
    movement.drive_left_a(45)
    fr = []
    for i in range(6):
        r = tracking.get_all_token_positions()
        for item in r: fr.append(item)
        if i != 100:
            movement.drive_right_a(15)

    image.image = image.reset_image(image.image)
    image.draw_zone(image.image)
    image.process_raw(fr)
    image.add_robot(Data.x,Data.y,Data.bearing,image.image)
    image.save_image(image.image, "messy.png")

    image.image = image.reset_image(image.image)
    image.draw_zone(image.image)
    fr = image.process_data(fr, True)
    image.add_robot(Data.x,Data.y,Data.bearing,image.image)
    image.save_image(image.image, "clean.png")

def l6_track_cube():
    while True:
        dist, ang, t, f = tracking.get_closest_token()
        print(dist,ang,t,f,"TARGET")
        ang = math.degrees(ang)
        if f:
            if (dist < 400): continue 
            if (ang < -1): movement.drive_left_a(-ang)
            elif (ang > 1): movement.drive_right_a(ang) 
            movement.drive_forward_d(dist / 0.70)
        else:
            movement.drive_right_a(25)


def l7_laps():

    while True:

        movement.drive_forward_d(3000)
        movement.smart_turn(90)
        movement.drive_forward_d(3300)
        movement.smart_turn(90)
        movement.drive_forward_d(10000)
        movement.smart_turn(90)
        movement.drive_forward_d(3300)
        movement.smart_turn(90)
        movement.drive_forward_d(7000)


def l8_turn_camera():
    time.sleep(2)
    Richard.wait_start()
    camera_servo.position = 1.0
    time.sleep(2)
    Richard.wait_start()
    camera_servo.position = -1.0
    time.sleep(2)
    Richard.wait_start()
    camera_servo.position = 0.5
    time.sleep(2)
    Richard.wait_start()
    camera_servo.position = -0.5
    time.sleep(2)
    Richard.wait_start()
    camera_servo.position = 0
    time.sleep(2)
    Richard.wait_start()
    camera_servo.position = -0.5
    time.sleep(2)


def l9_getdata(gg):

    d = []
    m = []
    while True:
        m = tracking.get_all_raw()

        f = open("out.txt")
        exec(f.read())
        f.close()

        file = open("out.txt","a")
        for item in m:
            print(item)
            file.write(str(item[0])+","+str(item[1])+","+str(item[2])+","+str(item[3])+","+str(gg)+ "\n")
        file.close()
        time.sleep(0.2)
