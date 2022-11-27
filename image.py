
#import constants
import cv2
import numpy as np
import time 
from random import * 
from constants import *
from math import trunc
import math


def rotate_point(x,y,o):
    r = math.radians(o)
    tx = (math.cos(r) * x) - (math.sin(r) * y)
    ty = (math.sin(r) * x) + (math.cos(r) * y)
    return tx, ty

def save_image(image, location):
    cv2.imwrite(location,image)

def reset_image(image):
    image = np.zeros((2875*2,2875*2,3), dtype="uint8")
    return image

def draw_zone(image):
    x1, y1 = 0,2875
    x2, y2 = 0,1875
    x3, y3 = 1000,1875
    x4, y4 = 1000, 2875

    points = np.array( [[ [x1,img_y - y1], [x2,img_y - y2], [x3,img_y - y3], [x4,img_y - y4], [x1,img_y - y1] ]], np.int32)
    cv2.polylines(image, [points], True, (0,255,0), 3 )
    
    x1, y1 = 2875,2875
    x2, y2 = 1875,2875
    x3, y3 = 1875,2850
    x4, y4 = 2575,2850
    x5, y5 = 2575,2575
    x6, y6 = 2850,2575
    x7, y7 = 2850,1875
    x8, y8 = 2875,1875

    points = np.array( [[ [x1,img_y - y1], [x2,img_y - y2], [x3,img_y - y3], [x4,img_y - y4], 
        [x5,img_y - y5],[x6,img_y - y6],[x7,img_y - y7],[x8,img_y - y8],[x1,img_y - y1] ]], np.int32)
    cv2.polylines(image, [points], True, (0,0,255), 3 )
    



def add_marker(id, image):
    x = marker_positions[id][0]
    y = marker_positions[id][1]
    o = 0
    if (0 <= id <= 6): o = 0
    elif (7 <= id <= 13): o = 90
    elif (13 <= id <= 20): o = 0
    elif (id <= 27): o = 90
    x1, y1 = rotate_point(20, 100, o)
    x1, y1 = x1 + x, y1 + (img_y - y)
    x2, y2 = rotate_point(-20, 100, o)
    x2, y2 = x2 + x, y2 + (img_y - y)
    x3, y3 = rotate_point(-20, -100, o)
    x3, y3 = x3 + x, y3 + (img_y - y)
    x4, y4 = rotate_point(20, -100, o)
    x4, y4 = x4 + x, y4 + (img_y - y)
    

    points = np.array( [[ [x1,y1], [x2,y2], [x3,y3], [x4,y4], [x1,y1] ]], np.int32)
    image = cv2.polylines(image, [points], True, (255,0,0), 3 )
    disp = "("+str(id)+")"
    if (o == 0): 
        cv2.putText(image, disp, (x + 10,img_y - y), cv2.FONT_ITALIC, 0.85, (200,200,200), 3)
    elif (id <= 14): 
        cv2.putText(image, disp, (x - 40,img_y - y + 30), cv2.FONT_ITALIC, 0.85, (200,200,200), 3)
    else: 
        cv2.putText(image, disp, (x - 40,img_y - y - 30), cv2.FONT_ITALIC, 0.85, (200,200,200), 3)

def add_robot(x,y,o,image):
    x,y = trunc(x), trunc(y)
    o = o - 90
    x1, y1 = rotate_point(110, 185, o)
    x1, y1 = x1 + x, y1 + (img_y - y)
    x2, y2 = rotate_point(-310, 185, o)
    x2, y2 = x2 + x, y2 + (img_y - y)
    x3, y3 = rotate_point(-310, -185, o)
    x3, y3 = x3 + x, y3 + (img_y - y)
    x4, y4 = rotate_point(110, -185, o)
    x4, y4 = x4 + x, y4 + (img_y - y)

    points = np.array( [[ [x1,y1], [x2,y2], [x3,y3], [x4,y4], [x1,y1] ]], np.int32)
    image = cv2.polylines(image, [points], True, (255,0,0), 3 )
    disp = "("+str(math.trunc(x))+","+str(math.trunc(y))+")"
    print(disp,"img")
    cv2.putText(image, disp, (x - 75,img_y - y), cv2.FONT_ITALIC, 0.85, (200,200,200))

def add_token_gold(x,y,o,image):
    x,y = trunc(x), trunc(y)
    print(x,y,o,"IMG")
    x1, y1 = rotate_point(125.5, 125.5, o)
    x1, y1 = x1 + x, y1 + (img_y - y)
    x2, y2 = rotate_point(-125.5, 125.5, o)
    x2, y2 = x2 + x, y2 + (img_y - y)
    x3, y3 = rotate_point(-125.5, -125.5, o)
    x3, y3 = x3 + x, y3 + (img_y - y)
    x4, y4 = rotate_point(125.5, -125.5, o)
    x4, y4 = x4 + x, y4 + (img_y - y)

    points = np.array( [[ [x1,y1], [x2,y2], [x3,y3], [x4,y4], [x1,y1] ]], np.int32)
    image = cv2.polylines(image, [points], True, (0,255,255), 3 )
    disp = "("+str(math.trunc(x))+","+str(math.trunc(y))+")"
    cv2.putText(image, disp, (x - 75,img_y - y), cv2.FONT_ITALIC, 0.85, (200,200,200), 3)

def add_token_bronze(x,y,o, image):
    print(x,y,o,"IMG")
    x,y = trunc(x), trunc(y)
    x1, y1 = rotate_point(55, 55, o)
    x1, y1 = x1 + x, y1 + (img_y - y)
    x2, y2 = rotate_point(-55, 55, o)
    x2, y2 = x2 + x, y2 + (img_y - y)
    x3, y3 = rotate_point(-55, -55, o)
    x3, y3 = x3 + x, y3 + (img_y - y)
    x4, y4 = rotate_point(55, -55, o)
    x4, y4 = x4 + x, y4 + (img_y - y)

    points = np.array( [[ [x1,y1], [x2,y2], [x3,y3], [x4,y4], [x1,y1] ]], np.int32)
    image = cv2.polylines(image, [points], True, (0,133,226), 3 )
    disp = "("+str(math.trunc(x))+","+str(math.trunc(y))+")"
    cv2.putText(image, disp, (x - 75,img_y - y), cv2.FONT_ITALIC, 0.85, (200,200,200), 3)
    
image = np.zeros((2875*2,2875*2,3), dtype="uint8")

def test():
    reset_image(image)
    draw_zone(image)
    add_token_bronze(randint(100, 2700),randint(100,2700),randint(0,90),image)
    add_token_bronze(randint(100, 2700),randint(100,2700),randint(0,90),image)
    add_token_gold(randint(300, 2500),randint(300,2500),randint(0,90),image)
    add_robot(1500, 1200,randint(0,90),image)
    save_image(image,"map.png")
    reset_image(image)
    draw_zone(image)
    save_image(image,"t.png")

def process_raw(r):
    for item in r:
        if item[2]: add_marker(item[0], image)
        elif item[1]: add_token_gold(item[0][0], item[0][1], item[0][2], image)
        else: add_token_bronze(item[0][0], item[0][1], item[0][2], image)

def process_data(r, finalR):
    s = []
    groups = []

    for item in r:
        if item[2]: add_marker(item[0], image)
        else: s.append(item)

    while len(s) > 0:
        item = s[0]
        x,y,o,g = item[0][0], item[0][1], item[0][2],item[1]
        groups.append([[x,y,o % 90,g]])
        dels = 0
        del s[0]
        for j in range(len(s)):
            item2 = s[j - dels]
            x2,y2,o2,g2 = item2[0][0], item2[0][1], item2[0][2],item[1]
            dist = math.sqrt((x - x2)**2 + (y - y2)**2)
            if g2 != g: continue

            md = 0
            if (g): md = 250
            else: md = 110

            if dist < md: 
                groups[-1].append([x2,y2,o2 % 90])
                del s[j - dels]
                dels += 1

    f = []
    for item in groups:
        x,y,o,t = 0,0,0,0
        for d in item:
            x += d[0]
            y += d[1]
            o += d[2]
            t += 1
        x = x / t
        y = y / t
        o = o / t
        o = o % 90
        f.append([(x,y,o), item[0][1], False])
        if finalR:
            if item[0][1]: add_token_gold(x, y, o, image)
            else: add_token_bronze(x, y, o, image)
    print(len(r),len(f),f)
    return f

