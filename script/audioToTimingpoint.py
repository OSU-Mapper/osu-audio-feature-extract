# We'll need numpy for some mathematical operations
import numpy as np
import csv
import sys

import librosa

if len(sys.argv) is not 2:
    raise argparse.ArgumentTypeError('''the number of argument has to be 4
    Usage py filename.py audio timing feature 
        example: .py path/to/audio.wav path/to/timing_points.v{version}.csv path/to/all_features.v{version}.csv
            Audio: audio file
            Timeing: path to timing file csv
            Feature: path to feature file csv
    '''.format(version=version))
    exit(-1)

audio_path = sys.argv[1]

y, sr = librosa.load(audio_path)

o_env = librosa.onset.onset_strength(y, sr=sr)

dtempo = librosa.beat.tempo(onset_envelope=o_env, sr=sr,
                            aggregate=None)
# print (len(dtempo))

times = librosa.frames_to_time(np.arange(len(o_env)), sr=sr)

arr_bpm = []
pre = dtempo[0]
# print (pre)
for i in range(1, len(dtempo)):
    tmp = dtempo[i]
    if (dtempo[i] != pre):
        arr_bpm.append((60/pre,times[i]))
        pre = tmp

arr_bpm.append((60/pre, times[len(dtempo)-1]))
#print (arr_bpm)
#arr_bpm = [(spb, endtime)]
# [(0.25541950113378681, 1.1145578231292517), (0.46439909297052157, 199.85414965986394), (0.53405895691609973, 203.08172335600906), (0.46439909297052157, 204.0801814058957), (0.4411791383219954, 205.68235827664398), (0.46439909297052157, 206.10031746031746), (0.37151927437641724, 206.51827664399093)]

onset_frames = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr)

onset_times = times[onset_frames]

whichBPM = 0
thisTuple = arr_bpm[whichBPM]
arr_statistics = []
thisOnset = [0]
for onsetTime in onset_times:
    if onsetTime > thisTuple[1]:
        arr_statistics.append([np.median(thisOnset[0])])
        whichBPM += 1
        thisTuple = arr_bpm[whichBPM]
    #thisSPB = thisTuple[0]
    thisOnset = [
        onsetTime % thisTuple[0]
    ]

arr_statistics.append([np.median(thisOnset[0])])
