
import constants
import math

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
    else: # Wall D
        bearing = (math.pi * 1.5) + oy
        x = marker_position[0] + (distance * math.sin(theta))
        y = marker_position[1] + (distance * math.cos(theta))
    
    bearing += constants.camera_bias
    
    print(id,'marker = ', marker_position, 'x = ',math.trunc(x), 'y = ', math.trunc(y), 'bearing = ',round(math.degrees(bearing),1), "theta = ", round(math.degrees(theta),1))
    bearing = bearing % (math.pi * 2)
    
    # returns positiion and bearing from given marker
    return x, y, math.degrees(bearing)


def get_position():
    # default values for calcs
    avg_x, avg_y, avg_o = 0, 0, 0
    mx, my, mo = 0, 0, 0
    markers = constants.camera.see()
    total_markers = len(markers)

    for marker in markers:
        # process each marker individually
        mx, my, mo = process_marker(marker)
        avg_x += mx
        avg_y += my
        avg_o += mo

    if total_markers > 0: # average the position across all marker readings
        mx = avg_x / total_markers
        my = avg_y / total_markers
        mo = avg_o / total_markers
    # return the average position and orientation for use

    print("X: %.2f, Y: %.2f, O: %.1f"%(mx, my, mo))

    return mx, my, mo


def calc_direction_to_point(sX, sY, eX, eY):
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
