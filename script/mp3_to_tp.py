# python mp3_to_tp.py "Chasers - Lost.mp3" 
import sys
import argparse
import librosa
import librosa.display
import csv
    


def getbpm(y, sr):
    dynamic_bpm = librosa.beat.dynamic_tempo_summary(y=y, sr=sr, precise=True, units='time')
    return dynamic_bpm


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise argparse.ArgumentTypeError('the number of argument has to be 2')
        exit(-1)
    y, sr = librosa.load(sys.argv[1], sr = None)
    dynamic_bpm = getbpm(y, sr)
    
    writer = csv.writer(sys.stdout)
    writer.writerows(dynamic_bpm)
