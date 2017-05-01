# python audioMIS.py "Chasers - Lost (ktgster) [Normal].osu" "Chasers - Lost.mp3" 
import sys
from extract_bpm import createBPM
import argparse
import librosa
import numpy as np
import librosa.display

#bpm expension
def createMIS(bpm_result, sr, times, o_env):
    matrix = []
    count = 1
    division = 8
    for i in range(len(bpm_result)):
        t, bpm = bpm_result[i]
        sequence = 0
        simu_t = t
        if i < len(bpm_result) - 1:
            next_t = bpm_result[i+1][0]
        else:
            next_t = 1000 * times[len(o_env)-1]
        delt = 1000 / (division * (bpm / 60)) 
        while (simu_t < next_t):
            if sequence % division == 0:
                matrix.append((count, simu_t, 1))
            else:
                matrix.append((count, simu_t, 0))
            simu_t += delt
            count += 1
            sequence += 1
    

    mis_result = [(i, t, o_env[librosa.core.time_to_frames(t/1000, sr=sr)[0]], b) for (i, t, b) in matrix] 
    return mis_result

def getOnset(sr, times):
    onset_frames = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr)
    onset_result = [times[i] for i in onset_frames]
    return onset_result
   

def closestindex(x, y):
    for i in range(len(y)):
        if y[i][1] == x:
            return i
        elif y[i][1] > x:
            if i == 0 or abs(y[i][1] - x) <= abs(y[i-1][1] - x):
                return i
            else:
                return i - 1
    if i == len(y) - 1:
        return i

def isonset(x, y):
    x = [1000 * e for e in x]
    feature_copy = y
    startindex = 0
    for i in range(len(x)):
        index = closestindex(x[i], y)
        if len(feature_copy[index + startindex]) == 4:
            feature_copy[index + startindex] = (feature_copy[index + startindex][0], feature_copy[index + startindex][1], feature_copy[index + startindex][2], feature_copy[index + startindex][3], 1) 
        startindex += index
        y = y[index:]
    for i in range(len(feature_copy)):
        if len(feature_copy[i]) == 4:
            feature_copy[i] = (feature_copy[i][0], feature_copy[i][1], feature_copy[i][2], feature_copy[i][3], 0)
    return feature_copy

# def addmfcc(y, sr, prefeature):
#     # Let's make and display a mel-scaled power (energy-squared) spectrogram
#     S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)

#     # Convert to log scale (dB). We'll use the peak power as reference.
#     log_S = librosa.logamplitude(S, ref_power=np.max)

#     # Next, we'll extract the top 13 Mel-frequency cepstral coefficients (MFCCs)
#     mfcc = librosa.feature.mfcc(S=log_S, n_mfcc=13)

#     print (len(mfcc))
#     print (librosa.core.time_to_frames(210337.47058824223/1000, sr=sr)[0])
    # a = mfcc[librosa.core.time_to_frames(210337.47058824223/1000, sr=sr)[0]] 
    # print (a)
    # feature = [mfcc[librosa.core.time_to_frames(f[1]/1000, sr=sr)[0]] for f in prefeature]
    # print (mfcc)
    # print (feature)
    # return feature



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print( "usage: inputfile outputfile")
        raise argparse.ArgumentTypeError('the number of argument has to be 3')
        exit(-1)
    y, sr = librosa.load(sys.argv[2])
    o_env = librosa.onset.onset_strength(y, sr=sr)
    times = librosa.frames_to_time(np.arange(len(o_env)), sr=sr) 
    dynamic_bpm = createBPM(sys.argv[1])
    mis_result = createMIS(dynamic_bpm, sr, times, o_env)
    onset = getOnset(sr, times)
    # sequence_number, t, onset_strength, isbeat, isOnset 
    prefeature = isonset(onset, mis_result)
    # addmfcc(y, sr, prefeature)
