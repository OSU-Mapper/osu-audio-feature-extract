#python target_mis_to_tr_t.py hitobject.csv mis.csv
import sys
import argparse
import csv
from mp3_mis_to_tr_f import closestindex

def ishitobject(x, y):
    y_copy = [[] for i in range(len(y))]
    startindex = 0
    for i in range(len(x)):
        index = closestindex(int(x[i][2]), y)
        if len(y_copy[index + startindex]) == 0:
            y_copy[index + startindex] = [int(x[i][0]), int(x[i][1]), 1]
        startindex += index
        y = y[index:]
    for i in range(len(y_copy)):
        if len(y_copy[i]) == 0:
            y_copy[i] = [0, 0, 0]
    return y_copy


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise argparse.ArgumentTypeError('the number of argument has to be 3')
        exit(-1)
    
    with open(sys.argv[1], 'r') as my_file:
        csvreader = csv.reader(my_file)
        hitobject = list(csvreader)
    
    with open(sys.argv[2], 'r') as my_file:
        csvreader = csv.reader(my_file)
        mis = list(csvreader)
        mis = [[int(m[0]), float(m[1])]for m in mis]
    tr_t = ishitobject(hitobject, mis)


    writer = csv.writer(sys.stdout)
    writer.writerows(tr_t)

    # with open("tr_t.csv", "w") as file:
    #     writer = csv.writer(file)
    #     writer.writerows(tr_t)