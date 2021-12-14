#Import Libraries Needed For Special Functions
from fractions import Fraction
import math
import numpy as np 
import copy

#Define 'b' as an Array Containing the Coordinates of the Beacons
b = np.array([(0,0), (0, 25), (25, 0), (25, 25), (-25, 0), (0, -25), (-25, -25), (-25, 25), (25, -25)])

#Define 'beacons' as a List Which Can be Formed into an Array
beacons = list()

#Defines Destination
p1, p2 = 13, 3

#Change Text Color to Dark Blue
print("\033[34m")

#Ask How Many Beacons are in Range and Defines the Input as 'n'
n = input("How many beacons are in range: ")

#If There are Fewer than Three Beacons...
if(int(n)<3):

    #Prints Error Message in Red
    print("\033[31mWARNING!! Not enough beacons in range!")

#If There are Three or More Beacons...
else:

    #Change Text Color to Teal 
    print("\033[36m")

    #Ask for Distance Between 'n' Beacons and the Device, and then inputs those values in Array 'beacons'
    for i in range(int(n)):
        print(f"Beacon", i+1, ": ", end="")
        n2 = float(input())
        beacons.append(n2)

    #Create a Copy of the Array 'beacons' and Define it as 'c'
    c = copy.deepcopy(beacons)

    #Reorganize the Origional Array in Order of Smallest to Largest
    list.sort(beacons)

    #Change Text Color to Green
    print("\033[32m")

    #Print Arrays 'c' and 'beacons' for Troubleshooting Purposes
    print("Beacons by order: ", c)
    print("Beacons by closeness: ", beacons)

    #Define the Distances Closest to the Robot
    d1 = beacons[0]
    d2 = beacons[1]
    d3 = beacons[2]

    #Finding Position of Cell to Reference Which Beacon is Being Utilized
    w1 = c.index(d1)
    w2 = c.index(d2)
    w3 = c.index(d3)

    #Change Text Color to Magenta
    print("\033[35m")

    #Print Array Position of Used Beacons
    print(w1, w2, w3)

    #Assign the Position of the Beacons Based on their Initial Input
    x1, y1 = b[w1]
    x2, y2 = b[w2]
    x3, y3 = b[w3]

    #print(x1, y1, x2, y2, x3, y3)

    #Calculating Coordinates of Unknown Point
    x = ((d1**2 - d2**2 - x1**2 + x2**2 - y1**2 + y2**2)*(2*y3 - 2*y2) - (d2**2 - d3**2 - x2**2 + x3**2 - y2**2 + y3**2)*(2*y2 - 2*y1)) / ((2*y3 - 2*y2)*(2*x2 - 2*x1) - (2*y2 - 2*y1)*(2*x3 - 2*x2))
    y = ((d1**2 - d2**2 - x1**2 + x2**2 - y1**2 + y2**2)*(2*x3 - 2*x2) - (2*x2 - 2*x1)*(d2**2 - d3**2 - x2**2 + x3**2 - y2**2 + y3**2)) / ((2*y2 - 2*y1)*(2*x3 - 2*x2) - (2*x2 - 2*x1)*(2*y3 - 2*y2))

    #Rounding Coordinates to the Nearest Decimal Point
    x4 = round(x, 1)
    y4 = round(y, 1)

    #Calculating Slope Between Current Point and Destination 
    s = (p2-y4)/(p1-x4)

    #Calculate the Angle in Degrees Between the Current Point and Destination
    m = round(math.degrees(math.atan(s)), 2)

    #Printing Coordinates of New Point and Degrees to Face Destination in Yellow
    print("\033[33m")
    print(x4, y4)
    print(m)