import csv
from matplotlib import pyplot as plt
import numpy as np


def addAnchors(test):
    if test == 1:
        plt.plot([0, 3050], [0, 0], 'k-')
        plt.plot([0, 3050], [1950 , 1950], 'k-')
        plt.plot([3050 , 3050], [1950 , 0], 'k-')
        plt.plot([0 , 0], [0, 1950], 'k-')
    elif test == 2:
        plt.plot([0, 0], [0, 5000], 'k-')
        plt.plot([0, 5000], [5000, 5000], 'k-')
        plt.plot([5000, 5000], [5000, 0], 'k-')
        plt.plot([5000, 0], [0, 0], 'k-')
    elif test == 3:
        plt.plot([0, 0], [0, 12000], 'k-')
        plt.plot([0, 12000], [12000, 12000], 'k-')
        plt.plot([12000, 12000], [12000, 0], 'k-')
        plt.plot([12000, 0], [0, 0], 'k-')

def getPunkt(punkt):
    if punkt == 1:
        _punkt = [1500, 1500]
    elif punkt == 2:
        _punkt = [2500, 2000]
    elif punkt == 3:
        _punkt = [-2000, 2000]
    elif punkt == 4:
        _punkt = [0, 15000]
    return _punkt

def getData(filename):
    xList = []
    yList = []
    number_list = []
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
                    xList.append(x1)
                    yList.append(y1)

                except:
                    pass

def saveFigure(filename, test, punkt):
    number_list = []
    x1List = []
    y1List = []
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
                    x1List.append(x2)
                    y1List.append(y2)

                except:
                    pass
    
    plt.clf()
    plt.scatter(y1List, x1List)
    plt.xlabel("x (mm)")
    plt.ylabel("y (mm)")
    x_std = round(np.std(y1List), 0)
    y_std = round(np.std(x1List), 0)
    _punkt = getPunkt(punkt)
    x_error = np.abs(x_std - _punkt[0])
    y_error = np.abs(y_std - _punkt[1])
    plt.scatter(_punkt[0], _punkt[1], c='r')

    grid = ""
    if test == 1:
        grid = "2x3"
    elif test == 2:
        grid = "5x5"
    elif test == 3:
        grid = "12x12"

    plt.title(f"Grid: {grid}. Punkt: {punkt}.", fontweight='bold')
    addAnchors(test)
    plt.axis('equal')
    plt.legend(["Målte punkter", "Faktisk punkt"], loc ="lower right")
    #plt.rcParams.update({'font.size': 25})
    plt.savefig(f"Grid{grid}punkt{punkt}.jpg")
    
    x_mean = round(np.average(y1List), 0)
    y_mean = round(np.average(x1List), 0)
    x_std = round(np.std(y1List), 2)
    y_std = round(np.std(x1List), 2)
    _punkt = getPunkt(punkt)
    x_error = np.abs(x_mean - _punkt[0])
    y_error = np.abs(y_mean - _punkt[1])
    print(f"Test: {test} Punkt: {punkt}, xStd: {x_std}, yStd: {y_std}")


def saveFigures(tester, punkter):
    test = 1
    punkt = 1
    run = True
    while run:
        filename = f"hamnatest{test}_punkt{punkt}_1.csv"
        saveFigure(filename, test, punkt)
        punkt += 1
        if punkt > punkter:
            punkt = 1
            test += 1
            if test > tester:
                run = False
        
            
tester = 3
punkter = 4
saveFigures(tester, punkter)



"""
mybool = True
nextFileNumber = 0
while mybool == True:
    nextFileNumber += 1
    mybool = os.path.isfile(filename + str(nextFileNumber) + '.csv')

def plotFigure():
    with open(filename, newline='') as csvfile:
            positionReader = csv.reader(csvfile, delimiter=',')
            for row in positionReader:
                try:
                    number = [int(s) for s in row[0].split() if s.isdigit()][0]
                    x1 = [int(s) for s in row[1].split() if s.lstrip("-").isdigit()][0]
                    y1 = [int(s) for s in row[2].split() if s.lstrip("-").isdigit()][0]
                    x2 = [int(s) for s in row[3].split() if s.lstrip("-").isdigit()][0]
                    y2 = [int(s) for s in row[4].split() if s.lstrip("-").isdigit()][0]
                    
                        #print(f"number: {number}, distance: {distance}, rssi: {rssi}")
                    number_list.append(number)
                    x1List.append(x1)
                    y1List.append(y1)
                    x1List.append(x2)
                    y1List.append(y2)

                except:
                    pass

    plt.scatter(x1List, y1List)
    plt.grid(True)
    plt.plot([0, 0], [0, 5000], 'k-')
    plt.plot([0, 5000], [5000, 5000], 'k-')
    plt.plot([5000, 5000], [5000, 0], 'k-')
    plt.plot([5000, 0], [0, 0], 'k-')
    plt.show()
"""