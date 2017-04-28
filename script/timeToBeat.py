import sys
import argparse
import numpy as np
import csv
def search(input, file):
    hitobject = []
    with open(file, 'r') as my_file:
        # lines = my_file.readlines()
        # line_iter = iter(lines)
        csvreader = csv.reader(my_file)
        find = False
        target = "[" + input + "]"
        for line in csvreader:
            if target in line:
                find = True
                break
        if (find):
            for tmp in csvreader:
                if len(tmp) != 0:
                    if len(tmp) == 5:
                        tmp = list(map(int, tmp))
                        for i in range(4):
                            tmp.append(0)
                    else:
                        lastele = tmp[len(tmp)-1]
                        tmp = tmp[0:5]
                        tmp = list(map(int, tmp))
                        addition = lastele.split(":")
                        if len(addition) == 4:
                            for i in range(4):
                                tmp.append(int(addition[i]))
                        else:
                            for i in range(4):
                                tmp.append(0)
                    hitobject.append(tmp)
                else: 
                    break	
            return hitobject	
        else:
            print("No such infomation in file")

def getbeat(input):
    beats = []
    with open(input, 'r') as my_file:
        csvreader = csv.reader(my_file)
        for line in csvreader:
            line = list(map(float, line))
            beats.append(line)
    return beats

def closestindex(x, y):
    for i in range(len(y)):
        if y[i][1] == x:
            return i
        elif y[i][1] > x:
            if i == 0:
                return i
            elif abs(y[i][1] - x) <= abs(y[i-1][1] - x):
                return i
            else:
                return i - 1
    if i == len(y) - 1:
        return i

def merge(x, y):
    for i in range(len(x)):
        index = closestindex(x[i][2], y)
        x[i][2] = int(y[index][1])
        y[index] = [int(y[index][0])] + x[i] + [y[index][2]]
    for i in range(len(y)):
        if len(y[i]) == 3:
            y[i] = [int(y[i][0]),0,0,int(y[i][1]),0,0,0,0,0,0,y[i][2]]
    return y
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print( "usage: inputfile outputfile")
        raise argparse.ArgumentTypeError('the number of argument has to be 3')
        exit(-1)
    filePath = sys.argv[1]
    csvPath  = sys.argv[2]
    hitobject = search("HitObjects", filePath)
    # print (hitobject)
    beats = getbeat(csvPath)
    # print(beats)
    result = merge(hitobject, beats)
    # print(result)
    with open("labeledFeature.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerows(result)
    