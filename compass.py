# Code for reading coordinates from arduino and saving the coordinates as an CSV file
# Written by Håkon Skau Høksnes

import numpy as np
import os
import csv
import serial
import time

# Creating two arduino objects with coresponding read functions
arduino1 = serial.Serial(port='COM15', baudrate=115200, timeout=.1)
def read1():
    data = arduino1.readline()
    return data

arduino2 = serial.Serial(port='COM16', baudrate=115200, timeout=.1)
def read2():
    data = arduino2.readline()
    return data


start_time = time.time()
i = 1
i_list = []
angle_list = []
value_list = []
xList = []
yList = []
this = []
thisList = []
while (time.time() - start_time) < 30:
    try:
        this = []
        value = read1().decode("UTF-8").split(',') # Transelating the arduino string to UTF-8, and splitting the string into a list
        this.append(value)
        value.append("1")
        value = read2().decode("UTF-8").split(',')
        this.append(value)
        value.append("2")
        x1 = this[0][0]
        y1 = [int(s) for s in this[0][1].split() if s.isdigit()]
        x2 = this[1][0]
        y2 = [int(s) for s in this[1][1].split() if s.isdigit()]
        thisList.append(int(x1))
        thisList.append(int(y1[0]))
        thisList.append(int(x2))
        thisList.append(int(y2[0]))
        value_list.append(thisList)
        print(f"{x1}, {y1[0]}, {x2}, {y2[0]}")

    except:
        pass

location = "location_"
description = "description_"

# Creating a new CSV file with the data with increasing numbering
createNewFile = True
mybool = True
nextFileNumber = 0
while mybool == True:
    nextFileNumber += 1
    mybool = os.path.isfile(location + description + str(nextFileNumber) + '.csv')

if createNewFile:
        with open(location+description+f'{nextFileNumber}.csv', 'w', newline='') as csvfile:
                try:
                    rangewriter = csv.writer(csvfile, delimiter=',',
                                        quotechar=' ', quoting=csv.QUOTE_MINIMAL)
                    rangewriter.writerow(['count'] + ['x1'] + ['y1'] + ['x2'] + ['y2'])
                    i = 0
                    for item in value_list:
                        x1 = int(item[0])
                        y1 = int(item[1])
                        x2 = int(item[2])
                        y2 = int(item[3])
                        rangewriter.writerow([i, x1, y1, x2, y2])
                        i += 1
                except:
                    pass

print(f"{len(value_list)} rows.")