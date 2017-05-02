import sys
import argparse
import csv
def gettime(input):
    res = []
    zeros = [1,2,4,5,6,7,8,9]
    length = 11
    for i in range(len(input)):
        part = [input[i][j] for j in zeros]
        #print (part)
        if (not all(x == '0' for x in part)):
            tmp = input[i]
            addition = tmp[6]+":"+tmp[7]+":"+tmp[8]+":"+tmp[9]+":"
            tmp = tmp[1:6]
            tmp.append(addition)
            res.append(tmp)
    return res

def createosu(x):
    # print("osu file format v5\n\n[General]\n...\n\n[Metadata]\n...\n\n[Difficulty]\n...\n\n[TimingPoints]")
    # for i in range(len(y)):
    #     print("{time},{bpm},{extra}".format(
    #         time = str(int(1000*float(y[i][0]))),
    #         bpm  = int(60000/y[i][1]),
    #         extra="4,2,1,60,1,0"
    #     ))
    print("osu file format v5\n\n[General]\n...\n\n[Metadata]\n...\n\n[Difficulty]\n...\n\n[TimingPoints]\n...\n\n[HitObjects]")

    for i in range(len(x)):
        print(x[i][0]+","+x[i][1]+","+x[i][2]+","+x[i][3]+","+x[i][4]+","+x[i][5])

def getMatrix(input):
    with open(input, 'r') as csv_file:
        csvreader = csv.reader(csv_file)
        labeledFeature = list(csvreader)
    return labeledFeature

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise argparse.ArgumentTypeError('the number of argument has to be 2')
        exit(-1)
    labeledFeature = getMatrix(sys.argv[1])
    res = gettime(labeledFeature)
    # time = []
    # with open(sys.argv[2], 'r') as my_file:
    #     csvreader = csv.reader(my_file)
    #     for line in csvreader:
    #         line = list(map(float, line))
    #         time.append(line)
    createosu(res)