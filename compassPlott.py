# Code for reading multiple files containging coordinates, calculating the 
# angle between the coordinates for each file, 
# and plotting the max and min differense in angles for each file
# Written by Håkon Høksnes

import csv
from matplotlib import pyplot as plt
import numpy as np

# Function for calculating the angle between two coordinates
def get_angle(x, y):
    # First quadrant
    if x >= 0 and y >= 0:
        rad = np.arctan(y/x)
        deg = np.rad2deg(rad)

    # Second quadrant
    if x <= 0 and y >= 0:
        rad = np.arctan(y/x)
        deg = 180 + np.rad2deg(rad)

    # Third quadrant
    if x <= 0 and y <= 0:
        rad = np.arctan(y/x)
        deg = 180 + np.rad2deg(rad)

    # Fourth quadrant
    if x >= 0 and y <= 0:
        rad = np.arctan(y/x)
        deg = 360 + np.rad2deg(rad)

    return deg

def getAngleList(number):
    filename = f"klasserom{number}compass1.csv"

    number_list = []
    x1List = []
    y1List = []
    x2List = []
    y2List = []

    with open(filename, newline='') as csvfile:
            positionReader = csv.reader(csvfile, delimiter=',')
            for row in positionReader:
                try:
                    number = [int(s) for s in row[0].split() if s.isdigit()][0]
                    x1 = [int(s) for s in row[1].split() if s.lstrip("-").isdigit()][0]
                    y1 = [int(s) for s in row[2].split() if s.lstrip("-").isdigit()][0]
                    x2 = [int(s) for s in row[3].split() if s.lstrip("-").isdigit()][0]
                    y2 = [int(s) for s in row[4].split() if s.lstrip("-").isdigit()][0]
                    
                    number_list.append(number)
                    x1List.append(x1)
                    y1List.append(y1)
                    x2List.append(x2)
                    y2List.append(y2)
                except:
                    pass


    angleList = []
    raduisList = []
    x_list = []
    y_list = []
    i = 0
    for _ in x1List:
        x = x1List[i] - x2List[i]
        y = y1List[i] - y2List[i]
        x_list.append(x)
        y_list.append(y)
        raduisList.append(1)
        i += 1

        angle = get_angle(x, y)
        angleList.append(angle)
    return angleList

numbers = [25, 50, 100, 150, 260]
difference = []

for number in numbers:
    angleList = getAngleList(number)
    max = np.max(angleList)
    min = np.min(angleList)
    
    diff = max-min
    print(f"max: {max}, min: {min}, diff: {diff}, cm: {number}")
    difference.append(diff)

plt.plot(numbers, difference)
plt.show()
