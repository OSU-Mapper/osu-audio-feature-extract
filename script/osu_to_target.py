# python osu_to_target.py "Demetori - Hoshi no Utsuwa ~ Casket of Star (happy30) [Yoeri's Easy].osu" 

import sys
import argparse
from osu_getInfo import search
import csv

def getHitobject(file):
    hitobject = []
    with open(file, 'r') as my_file:
        csvreader = csv.reader(my_file)
        target = "[HitObjects]"
        for line in csvreader:
            if target in line:
                break
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

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise argparse.ArgumentTypeError('the number of argument has to be 2')
        exit(-1)
    # timing_point = search("TimingPoints", sys.argv[1])
    # with open(sys.argv[2], "w") as file:
    #     writer = csv.writer(file)
    #     writer.writerows(timing_point)
    hitobject = getHitobject(sys.argv[1])
    writer = csv.writer(sys.stdout)
    writer.writerows(hitobject)
    # with open("hitobject.csv", "w") as file:
    #     writer = csv.writer(file)
    #     writer.writerows(hitobject)