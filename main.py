import numpy as np
from trafficSim import *
import csv

sim = Simulation()

# Play with these
n = 15      # Iterations for road turns
a = 2       # Indicates start node point a 
b = 12      # Indicates end node point b
l = 300     # Length of road

NUM_OF_ROADS = 36 # Number of roads
VEHICLE_RATE = 400 # Vehicle spawn rate per minute
STEPS_PER_UPDATE = 1   # Number of steps per update

# coordinate y is opposite

# Nodes
WEST_RIGHT_START = (-b-l, a)    # -13, 2
WEST_LEFT_END =	(-b-l, -a)      # -13, -2

SOUTH_RIGHT_START = (a, b+l)    #   2, 13
SOUTH_LEFT_END = (-a, b+l)      #  -2, 13

EAST_RIGHT_START = (b+l, -a)    #  13, -2
EAST_LEFT_END = (b+l, a)        #  13, 2

NORTH_RIGHT_START = (-a, -b-l)  #  -2, -13
NORTH_LEFT_END = (a, -b-l)      #   2, -13

WEST_RIGHT = (-b, a)            # -12, 2
WEST_LEFT =	(-b, -a)            # -12, -2

SOUTH_RIGHT = (a, b)            #   2, 12
SOUTH_LEFT = (-a, b)            #  -2, 12

EAST_RIGHT = (b, -a)            #  12, -2
EAST_LEFT = (b, a)              #  12, 2

NORTH_RIGHT = (-a, -b)          #  -2, -12
NORTH_LEFT = (a, -b)            #   2, -12

# Create Nodes with offset to avoid overlapping
WEST_RIGHT_START2 = (WEST_RIGHT_START[0], WEST_RIGHT_START[1] + 4)
WEST_LEFT_END2 = (WEST_LEFT_END[0], WEST_LEFT_END[1] - 4)

SOUTH_RIGHT_START2 = (SOUTH_RIGHT_START[0] + 4, SOUTH_RIGHT_START[1])
SOUTH_LEFT_END2 = (SOUTH_LEFT_END[0] - 4, SOUTH_LEFT_END[1])

EAST_RIGHT_START2 = (EAST_RIGHT_START[0], EAST_RIGHT_START[1] - 4)
EAST_LEFT_END2 = (EAST_LEFT_END[0], EAST_LEFT_END[1] + 4)

NORTH_RIGHT_START2 = (NORTH_RIGHT_START[0] - 4, NORTH_RIGHT_START[1])
NORTH_LEFT_END2 = (NORTH_LEFT_END[0] + 4, NORTH_LEFT_END[1])

# Create Nodes with offset to avoid overlapping
WEST_RIGHT_START3 = (WEST_RIGHT_START[0], WEST_RIGHT_START[1] + 8)
WEST_LEFT_END3 = (WEST_LEFT_END[0], WEST_LEFT_END[1] - 8)

SOUTH_RIGHT_START3 = (SOUTH_RIGHT_START[0] + 8, SOUTH_RIGHT_START[1])
SOUTH_LEFT_END3 = (SOUTH_LEFT_END[0] - 8, SOUTH_LEFT_END[1])

EAST_RIGHT_START3 = (EAST_RIGHT_START[0], EAST_RIGHT_START[1] - 8)
EAST_LEFT_END3 = (EAST_LEFT_END[0], EAST_LEFT_END[1] + 8)

NORTH_RIGHT_START3 = (NORTH_RIGHT_START[0] - 8, NORTH_RIGHT_START[1])
NORTH_LEFT_END3 = (NORTH_LEFT_END[0] + 8, NORTH_LEFT_END[1])

# Create Nodes with offset to avoid overlapping
WEST_RIGHT2 = (WEST_RIGHT[0], WEST_RIGHT[1] + 4)
WEST_LEFT2 =	(WEST_LEFT[0], WEST_LEFT[1] - 4)

SOUTH_RIGHT2 = (SOUTH_RIGHT[0] + 4, SOUTH_RIGHT[1])
SOUTH_LEFT2 = (SOUTH_LEFT[0] - 4, SOUTH_LEFT[1])

EAST_RIGHT2 = (EAST_RIGHT[0], EAST_RIGHT[1] - 4)
EAST_LEFT2 = (EAST_LEFT[0], EAST_LEFT[1] + 4)

NORTH_RIGHT2 = (NORTH_RIGHT[0] - 4, NORTH_RIGHT[1])
NORTH_LEFT2 = (NORTH_LEFT[0] + 4, NORTH_LEFT[1])

# Create Nodes with offset to avoid overlapping
WEST_RIGHT3 = (WEST_RIGHT[0], WEST_RIGHT[1] + 8)
WEST_LEFT3 =	(WEST_LEFT[0], WEST_LEFT[1] - 8)

SOUTH_RIGHT3 = (SOUTH_RIGHT[0] + 8, SOUTH_RIGHT[1])
SOUTH_LEFT3 = (SOUTH_LEFT[0] - 8, SOUTH_LEFT[1])

EAST_RIGHT3 = (EAST_RIGHT[0], EAST_RIGHT[1] - 8)
EAST_LEFT3 = (EAST_LEFT[0], EAST_LEFT[1] + 8)

NORTH_RIGHT3 = (NORTH_RIGHT[0] - 8, NORTH_RIGHT[1])
NORTH_LEFT3 = (NORTH_LEFT[0] + 8, NORTH_LEFT[1])

# Roads
WEST_INBOUND = (WEST_RIGHT_START, WEST_RIGHT)
SOUTH_INBOUND = (SOUTH_RIGHT_START, SOUTH_RIGHT)
EAST_INBOUND = (EAST_RIGHT_START, EAST_RIGHT)
NORTH_INBOUND = (NORTH_RIGHT_START, NORTH_RIGHT)

WEST_OUTBOUND = (WEST_LEFT, WEST_LEFT_END)
SOUTH_OUTBOUND = (SOUTH_LEFT, SOUTH_LEFT_END)
EAST_OUTBOUND = (EAST_LEFT, EAST_LEFT_END)
NORTH_OUTBOUND = (NORTH_LEFT, NORTH_LEFT_END)

WEST_STRAIGHT = (WEST_RIGHT, EAST_LEFT)
SOUTH_STRAIGHT = (SOUTH_RIGHT, NORTH_LEFT)
EAST_STRAIGHT = (EAST_RIGHT, WEST_LEFT)
NORTH_STRAIGHT = (NORTH_RIGHT, SOUTH_LEFT)

WEST_LEFT_TURN = turn_road(SOUTH_RIGHT, WEST_LEFT, TURN_LEFT, n)

SOUTH_LEFT_TURN = turn_road(EAST_RIGHT, SOUTH_LEFT, TURN_LEFT, n)

EAST_LEFT_TURN = turn_road(NORTH_RIGHT, EAST_LEFT, TURN_LEFT, n)

NORTH_LEFT_TURN = turn_road(WEST_RIGHT, NORTH_LEFT, TURN_LEFT, n)

# Create Roads
WEST_INBOUND2 = (WEST_RIGHT_START2, WEST_RIGHT2)
SOUTH_INBOUND2 = (SOUTH_RIGHT_START2, SOUTH_RIGHT2)
EAST_INBOUND2 = (EAST_RIGHT_START2, EAST_RIGHT2)
NORTH_INBOUND2 = (NORTH_RIGHT_START2, NORTH_RIGHT2)

WEST_OUTBOUND2 = (WEST_LEFT2, WEST_LEFT_END2)
SOUTH_OUTBOUND2 = (SOUTH_LEFT2, SOUTH_LEFT_END2)
EAST_OUTBOUND2 = (EAST_LEFT2, EAST_LEFT_END2)
NORTH_OUTBOUND2 = (NORTH_LEFT2, NORTH_LEFT_END2)

WEST_STRAIGHT2 = (WEST_RIGHT2, EAST_LEFT2)
SOUTH_STRAIGHT2 = (SOUTH_RIGHT2, NORTH_LEFT2)
EAST_STRAIGHT2 = (EAST_RIGHT2, WEST_LEFT2)
NORTH_STRAIGHT2 = (NORTH_RIGHT2, SOUTH_LEFT2)

# Create Roads
WEST_INBOUND3 = (WEST_RIGHT_START3, WEST_RIGHT3)
SOUTH_INBOUND3 = (SOUTH_RIGHT_START3, SOUTH_RIGHT3)
EAST_INBOUND3 = (EAST_RIGHT_START3, EAST_RIGHT3)
NORTH_INBOUND3 = (NORTH_RIGHT_START3, NORTH_RIGHT3)

WEST_OUTBOUND3 = (WEST_LEFT3, WEST_LEFT_END3)
SOUTH_OUTBOUND3 = (SOUTH_LEFT3, SOUTH_LEFT_END3)
EAST_OUTBOUND3 = (EAST_LEFT3, EAST_LEFT_END3)
NORTH_OUTBOUND3 = (NORTH_LEFT3, NORTH_LEFT_END3)

WEST_STRAIGHT3 = (WEST_RIGHT3, EAST_LEFT3)
SOUTH_STRAIGHT3 = (SOUTH_RIGHT3, NORTH_LEFT3)
EAST_STRAIGHT3 = (EAST_RIGHT3, WEST_LEFT3)
NORTH_STRAIGHT3 = (NORTH_RIGHT3, SOUTH_LEFT3)

WEST_RIGHT_TURN3 = turn_road(NORTH_RIGHT3, WEST_LEFT3, TURN_RIGHT, n)

SOUTH_RIGHT_TURN3 = turn_road(WEST_RIGHT3, SOUTH_LEFT3, TURN_RIGHT, n)

EAST_RIGHT_TURN3 = turn_road(SOUTH_RIGHT3, EAST_LEFT3, TURN_RIGHT, n)

NORTH_RIGHT_TURN3 = turn_road(EAST_RIGHT3, NORTH_LEFT3, TURN_RIGHT, n)

sim.create_roads([
    WEST_INBOUND,   #0
    SOUTH_INBOUND,  #1
    EAST_INBOUND,   #2
    NORTH_INBOUND,  #3

    WEST_OUTBOUND,  #4
    SOUTH_OUTBOUND, #5
    EAST_OUTBOUND,  #6
    NORTH_OUTBOUND, #7

    WEST_STRAIGHT,  #8
    SOUTH_STRAIGHT, #9
    EAST_STRAIGHT,  #10
    NORTH_STRAIGHT, #11

    # NEW ROADS ----------------------------------------------
    WEST_INBOUND2,  #12
    SOUTH_INBOUND2, #13
    EAST_INBOUND2,  #14
    NORTH_INBOUND2, #15

    WEST_OUTBOUND2,  #16
    SOUTH_OUTBOUND2, #17
    EAST_OUTBOUND2,  #18
    NORTH_OUTBOUND2, #19

    WEST_STRAIGHT2,  #20
    SOUTH_STRAIGHT2, #21
    EAST_STRAIGHT2,  #22
    NORTH_STRAIGHT2, #23
    #----------------------------------------------------------------

    WEST_INBOUND3,   #24
    SOUTH_INBOUND3,  #25
    EAST_INBOUND3,   #26
    NORTH_INBOUND3,  #27

    WEST_OUTBOUND3,  #28
    SOUTH_OUTBOUND3, #29
    EAST_OUTBOUND3,  #30
    NORTH_OUTBOUND3, #31

    WEST_STRAIGHT3,  #32
    SOUTH_STRAIGHT3, #33
    EAST_STRAIGHT3,  #34
    NORTH_STRAIGHT3, #35

    *WEST_LEFT_TURN,   #0n

    *SOUTH_LEFT_TURN,  #1n

    *EAST_LEFT_TURN,   #2n

    *NORTH_LEFT_TURN,  #3n

    *WEST_RIGHT_TURN3, #4n

    *SOUTH_RIGHT_TURN3,#5n

    *EAST_RIGHT_TURN3, #6n

    *NORTH_RIGHT_TURN3 #7n
])

def road(a):
    if isinstance(a, int):
        return list(range(a, a + n))
    elif isinstance(a, list):
        return a
    else:
        raise TypeError("Input should be either an integer or a list")

sim.create_gen({
'vehicle_rate': VEHICLE_RATE,
'vehicles':[
    # 1st Lane
    [2, {'path': [0, 8, 6]}],
    #[2, {'path': [0, *road([2, 4, 6]), 8]}],
    [2, {'path': [0, *road(NUM_OF_ROADS+3*n), 7]}],

    [2, {'path': [1, 9, 7]}],
    [2, {'path': [1, *road(NUM_OF_ROADS), 4]}],

    [3, {'path': [2, 10, 4]}],
    [3, {'path': [2, *road(NUM_OF_ROADS+1*n), 5]}],

    [3, {'path': [3, 11, 5]}],
    [3, {'path': [3, *road(NUM_OF_ROADS+2*n), 6]}],

    # 2nd Lane
    [2, {'path': [12, 20, 18]}],

    [2, {'path': [13, 21, 19]}],

    [3, {'path': [14, 22, 16]}],

    [3, {'path': [15, 23, 17]}],

    # 3rd Lane (no red light/turn right only)
    [2, {'path': [24, *road(NUM_OF_ROADS+5*n), 29]}],

    [2, {'path': [25, *road(NUM_OF_ROADS+6*n), 30]}],

    [2, {'path': [26, *road(NUM_OF_ROADS+7*n), 31]}],

    [2, {'path': [27, *road(NUM_OF_ROADS+4*n), 28]}]

]})

sim.create_signal([[0], [1], [2], [3]])
sim.create_signal([[12], [13], [14], [15]])

# Create Green Light for 3rd Lane
sim.create_signal([[24]])
sim.create_signal([[25]])
sim.create_signal([[26]])
sim.create_signal([[27]])

# Start simulation
win = Window(sim)
win.zoom = 10
if(sim.isPaused == False):
    win.run(steps_per_update=STEPS_PER_UPDATE)
