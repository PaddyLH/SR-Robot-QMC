from numpy import exp, array, dot
import constants
import math


def locate_token_position(marker): # reverse locates the coords for a token
    o = constants.Data.bearing
    oR = math.radians(o) + marker.spherical.rot_y
    oR = oR % (math.pi * 2)
    dist = marker.distance
    tx, ty = 0, 0
    x, y = constants.Data.x, constants.Data.y

    ig = is_gold_nnue_v2(marker)
    h = 0
    if ig: h = 255 / 2
    else: h = 110 / 2

    tx = x + (dist * math.sin(oR))
    ty = y + (dist * math.cos(oR))
    fixed_turn = math.radians(constants.Data.bearing) - marker.orientation.rot_y
    tx = tx + (h * math.sin(math.radians(fixed_turn)))
    ty = ty + (h * math.cos(math.radians(fixed_turn)))
    fixed_turn = math.degrees(fixed_turn)

    oy = round(math.degrees(marker.orientation.rot_y),1)
    sy = round(math.degrees(marker.spherical.rot_y),1)
    b = round(constants.Data.bearing,1)

    print("Token","X:",tx,"Y:",ty,"O:",round(fixed_turn,1),ig)
    print("OY:",oy,"SY",sy,"B",b,math.trunc(dist))

    return tx,ty,fixed_turn


def is_tokens(ids): # returns true if a token is visible
    for i in ids:
        if i > 27: return True
    return False

def is_gold_token(marker): # returns true if a token is thought to be gold
    height = math.sin(marker.spherical.rot_x) * marker.spherical.dist
    height = -marker.cartesian.y + 238
    print(height,"G",(127.5 + (110 / 2)) / 2)
    if height > ((127.5 + (110 / 2)) / 2): return True
    return False

def is_gold_nnue(marker):
    synaptic_weights = [[-1.90039562],[0.45394811],[-26.32615836]]
    data = [marker.spherical.rot_x, marker.spherical.rot_y, marker.spherical.dist / 1000]
    s =  1 / (1 + exp(-(dot(array(data), synaptic_weights))))
    if s[0] >= 0.5: return True
    return False

def sigmoid(x):
    return 1 / (1 + exp(-x))

def is_gold_nnue_v2(marker):
    data = [marker.spherical.rot_x, marker.spherical.rot_y, marker.spherical.dist / 1000]
    sw1 = [[-0.6064617, 0.20342416,-1.09102744,-0.57047574],
    [-1.30138794,-1.15128156,-0.76101207,-0.56659755],
    [-6.39473,-3.30871447,-1.48672465,-2.51370525]]
    sw2 = [[2.29403438, -1.69362272, 1.38013792, 0.99152414],
    [3.79162556, -3.24233361,2.46902791, 0.28807306],
    [3.46152777, -1.4951184, -1.953514675, 1.02946229],
    [5.65667782, -3.3823607, 3.13071676,0.18321887]]
    sw3 = [[-29.67384277],[-36.48485489],[-10.48949446],[-17.06478123]]
    output_from_layer1 = sigmoid(dot(data, sw1))
    output_from_layer2 = sigmoid(dot(output_from_layer1, sw2))
    output_from_layer3 = sigmoid(dot(output_from_layer2, sw3))
    if output_from_layer3[0] > 0.5: 
        return True
    return False

def get_closest_token(excludeGold = False): # returns distance, angle, type, found for closest token in the arena, index 3 is wether a value was found
    if is_tokens(constants.camera.see_ids()):
        markers = constants.camera.see()
        distance, angle_diff, bg, is_gold = 1000000000, 0, False, False
        for marker in markers:
            if marker.id > 27:
                print(marker.id, marker.distance, math.degrees(marker.spherical.rot_y), math.degrees(marker.spherical.rot_x))
                if (distance > marker.distance):
                    is_gold = is_gold_nnue_v2(marker)
                    if (excludeGold):
                        if not is_gold:
                            bg = is_gold
                            distance = marker.distance
                            angle_diff = marker.spherical.rot_y
                    else:
                        bg = is_gold
                        distance = marker.distance
                        angle_diff = marker.spherical.rot_y
        if (distance == 1000000000): return 0,0,False,False
        return distance, angle_diff, bg, True
    return 0, 0, False, False

def process_marker(marker): # Location Calculation Function
    # calculates position with given marker
    distance = marker.distance
    bearing = 0
    oy = marker.orientation.rot_y
    theta = marker.spherical.rot_y + oy
    id = (marker.id + constants.home_base_increment) % 28
    marker_position = constants.marker_positions[id]

    if (id <= 6): # Wall A
        bearing = oy
        x = marker_position[0] + (distance * math.cos(theta))
        y = marker_position[1] - (distance * math.sin(theta))
    elif (id <= 13): # Wall B
        bearing = (math.pi * 0.5) + oy
        x = marker_position[0] - (distance * math.sin(theta))
        y = marker_position[1] - (distance * math.cos(theta))
    elif (id <= 20): # Wall C
        bearing = (math.pi) + oy
        x = marker_position[0] - (distance * math.cos(theta))
        y = marker_position[1] + (distance * math.sin(theta))
    elif (id <= 27): # Wall D
        bearing = (math.pi * 1.5) + oy
        x = marker_position[0] + (distance * math.sin(theta))
        y = marker_position[1] + (distance * math.cos(theta))
    
    bearing += constants.camera_bias
    bearing = bearing % (math.pi * 2)
    
    print(id,'marker = ', marker_position, 'x = ',math.trunc(x), 'y = ', math.trunc(y), 'bearing = ',round(math.degrees(bearing),1), "theta = ", round(math.degrees(theta),1))
    
    # returns positiion and bearing from given marker
    return x, y, math.degrees(bearing)

def see_markers(): # display details of stuff seen
    markers = constants.camera.see()
    for marker in markers:
        process_marker(marker)


def get_position(): # work out where the camera is relative to markers
    # default values for calcs
    avg_x, avg_y, avg_o = 0, 0, 0
    mx, my, mo = 0, 0, 0
    markers = constants.camera.see()
    total_markers = 0

    for marker in markers:
        # process each marker individually
        if (0 <= marker.id <= 27):
            total_markers += 1
            mx, my, mo = process_marker(marker)
            avg_x += mx
            avg_y += my
            avg_o += mo
        else:
            print("Token Found",marker.id,"Gold:",is_gold_nnue_v2(marker),is_gold_nnue(marker),is_gold_token(marker))

    if total_markers > 0: # average the position across all marker readings
        mx = avg_x / total_markers
        my = avg_y / total_markers
        mo = avg_o / total_markers
    # return the average position and orientation for use

    print("X: %.2f, Y: %.2f, O: %.1f"%(mx, my, mo))

    return mx, my, mo


def calc_direction_to_point(sX, sY, eX, eY): # calculates distance and bearing from location to point
    # calculate relative distances
    deltaX = (eX - sX)
    deltaY = (eY - sY)
    distance = math.sqrt((deltaX)**2 + (deltaY)**2)

    # calculate the bearing to the point 
    if (deltaX > 0 and deltaY > 0): #Q1
        theta = abs(math.atan(deltaX / deltaY))
    elif (deltaX > 0 and deltaY < 0): #Q2
        theta = abs(math.atan(deltaY / deltaX)) + (math.pi * 0.5)
    elif (deltaX < 0 and deltaY < 0): #Q3
        theta = abs(math.atan(deltaX / deltaY)) + (math.pi)
    else: #Q4
        theta = abs(math.atan(deltaY / deltaX)) + (math.pi * 1.5)
    # return the bearing and distance
    theta = theta % (math.pi * 2)
    return distance, math.degrees(theta)

def get_all_token_positions(): # get a list of all token position and types found from camera
    x,y,b = get_position()
    if x == 0 or y == 0: return []
    else: constants.Data.x, constants.Data.y, constants.Data.bearing = x,y,b
    markers = constants.camera.see()
    result = []
    for marker in markers:
        if marker.id > 27:
            f = [locate_token_position(marker), is_gold_nnue_v2(marker), False]
            result.append(f)
        else:
            result.append([(marker.id),False,True])
    return result

def get_all_raw():
    markers = constants.camera.see()
    result = []
    for marker in markers:
        if marker.id > 27:
            f = [marker.spherical.rot_x, marker.spherical.rot_y, marker.orientation.rot_y, marker.spherical.dist]
            result.append(f)
    return result

def set_camera_bearing(bearing):
    # do math
    value = 0

    if (0 <= bearing <= 180):
        value = bearing / 180
    elif (180 <= bearing <= 360):
        value = -(360 - bearing) / 180

    if (value < -1): value = -1
    if (value > 1): value = 1

    constants.camera_servo.position = value
    constants.camera_bias = -bearing
    