# python mp3_to_feature.py "Chasers - Lost.mp3" "onset.csv" "mfcc.csv" "dynamic_bpm.csv" 
import sys
import argparse
import librosa
import numpy as np
import librosa.display
import csv
    

def getOnset(y, sr):
    onset_result = librosa.onset.onset_detect(y=y, sr=sr, precise=True, units='time')
    onset_result = [[1000 * e] for e in onset_result]
    return onset_result
   

def getmfcc(y, sr):
    # Let's make and display a mel-scaled power (energy-squared) spectrogram
    S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)

    # Convert to log scale (dB). We'll use the peak power as reference.
    log_S = librosa.logamplitude(S, ref_power=np.max)

    # Next, we'll extract the top 13 Mel-frequency cepstral coefficients (MFCCs)
    mfcc = librosa.feature.mfcc(S=log_S, n_mfcc=13)

    return mfcc

    # a = mfcc[librosa.core.time_to_frames(t/1000, sr=sr)[0]] 
    # print (a)
    # feature = [mfcc[librosa.core.time_to_frames(f[1]/1000, sr=sr)[0]] for f in prefeature]
    # print (mfcc)
    # print (feature)
    # return feature

def getbpm(y, sr):
    dynamic_bpm = librosa.beat.dynamic_tempo_summary(y=y, sr=sr, precise=True, units='time')
    return dynamic_bpm

def onset_strength(sr):
    return [o_env[librosa.core.time_to_frames(e[1]/1000, sr=sr)[0]] for e in mis]

if __name__ == "__main__":
    if len(sys.argv) != 7:
        print( "usage: inputfile outputfile")
        raise argparse.ArgumentTypeError('the number of argument has to be 7')
        exit(-1)
    y, sr = librosa.load(sys.argv[1], sr = None)
    o_env = librosa.onset.onset_strength(y, sr=sr)
    times = librosa.frames_to_time(np.arange(len(o_env)), sr=sr) 

    onset = getOnset(y, sr)
    with open(sys.argv[2], "w") as file:
        writer = csv.writer(file)
        writer.writerows(onset)
    mfcc = getmfcc(y, sr)
    with open(sys.argv[3], "w") as file:
        writer = csv.writer(file)
        writer.writerows(mfcc)
    
    dynamic_bpm = getbpm(y, sr)
    with open(sys.argv[4], "w") as file:
        writer = csv.writer(file)
        writer.writerows(dynamic_bpm)
    

