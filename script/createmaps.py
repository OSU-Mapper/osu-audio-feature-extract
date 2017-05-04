#python createmaps.py "/Users/yanmingjun/Documents/osu-audio-feature-extract/Data/Trainables/Oyasumi.138554 livetune feat.Hatsune Miku - Last Night, Good Night.trainable_all.v1.csv" "timing_points.v1.csv" > "Oyasumi.138554 livetune feat.Hatsune Miku - Last Night, Good Night.osu"
import sys
import librosa
import argparse
import csv
import numpy as np

def createosu(hitobject, bpm):
    print("osu file format v5\n\n[General]\n...\n\n[Metadata]\n...\n\n[Difficulty]\n...\n\n[TimingPoints]")
    for i in range(len(bpm)):
        print("{time},{bpm},{extra}".format(
            time = int(1000*float(bpm[i][3])),
            bpm  = int(60000/float(bpm[i][2])),
            extra="4,2,1,10,1,0"
        ))
    print ("\n[HitObjects]")
    for x in hitobject:
        print (x)

def gethitobject(res):
    extra = ",26,5,6,0:0:0:0:"
    hits = [] 
    for x in res:
        if x[2] == '1':
            hits.append(x[0] + "," + x[1] + extra)
    return hits
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print( "usage: osufile csvFile outputfile")
        raise argparse.ArgumentTypeError('the number of argument has to be 3')
        exit(-1)

    with open(sys.argv[1], 'r') as my_file:
        csvreader = csv.reader(my_file)
        res = list(csvreader)
    
    with open(sys.argv[2], 'r') as my_file:
        csvreader = csv.reader(my_file)
        bpm = list(csvreader)
    
    res = np.array(res)[:,15:18]
    hitobject = gethitobject(res.tolist())
    createosu(hitobject, bpm)
