# python extract_bpm.py "Chasers - Lost (ktgster) [Normal].osu"

import sys
import argparse
from osu_getInfo import search

def deduplicate(bpm):
    dynamic_bpm = []
    dynamic_bpm.append(bpm[0])
    for i in range(1, len(bpm)):
        if bpm[i][1] != bpm[i - 1][1]:
            dynamic_bpm.append(bpm[i])
    return dynamic_bpm

def createBPM(input):
    time_point = search("TimingPoints", input)
    bpm = [x[:2] for x in time_point]
    bpm = [[int(x[0]), float(x[1])] for x in bpm]
    bpm = [(x[0], 60000 / ((-100 / x[1]) * float(time_point[0][1]))) if x[1] < 0 else (x[0], 60000 / x[1]) for x in bpm] 
    dynamic_bpm = deduplicate(bpm)
    return dynamic_bpm

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print( "usage: inputfile outputfile")
        raise argparse.ArgumentTypeError('the number of argument has to be 2')
        exit(-1)
    createBPM(sys.argv[1])
