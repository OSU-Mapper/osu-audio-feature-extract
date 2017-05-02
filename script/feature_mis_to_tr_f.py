#python feature_mis_to_tr_f.py "onset.csv" "mfcc.csv" "mis.csv" "tr_f.csv" "o_env.csv"
import sys
import librosa
import argparse
import csv
def mis_onset_strenghth(o_env, mis):
    return [o_env[librosa.core.time_to_frames(e[1]/1000, sr=sr)[0]] for e in mis]

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print( "usage: osufile csvFile outputfile")
        raise argparse.ArgumentTypeError('the number of argument has to be 6')
        exit(-1)

    with open(sys.argv[6], 'r') as my_file:
        csvreader = csv.reader(my_file)
        o_env = list(csvreader)
        o_env = o_env[0]
        
    with open(sys.argv[3], 'r') as my_file:
        csvreader = csv.reader(my_file)
        mis = list(csvreader)
    
    onset_strenghth = mis_onset_strenghth(o_env, mis)