# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 19:12:47 2017

@author: mw352
"""

#config InlineBackend.figure_format='retina'
#matplotlib notebook
# We'll need numpy for some mathematical operations
import numpy as np
import csv
import sys
import argparse
# matplotlib for displaying the output
import matplotlib.style as ms
import librosa
import librosa.display
ms.use('seaborn-muted')

if len(sys.argv) is not 2:
    raise argparse.ArgumentTypeError('the number of argument has to be 2')
    exit(-1)


# and IPython.display for audio output
# Librosa for audio
import librosa
# And the display module for visualization
import librosa.display

#audio_path = librosa.util.example_audio_file()

# or uncomment the line below and point it at your favorite song:
#
#audio_path = 'Data/test.wav'
audio_path = sys.argv[1]

y, sr = librosa.load(audio_path)

onset_env = librosa.onset.onset_strength(y, sr=sr)
tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)
# print (tempo)

dtempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr,
                            aggregate=None)
# print (len(dtempo))
arr_bpm = []
arr_bpm.append((dtempo[0],0))
pre = dtempo[0]
# print (pre)
timeframe = []
for i in range(1, len(dtempo)):
    tmp = dtempo[i]
    if (dtempo[i] != pre):
        pre = tmp
        arr_bpm.append((tmp,i))
        timeframe.append(i)
# print (arr_bpm)

o_env = librosa.onset.onset_strength(y, sr=sr)
times = librosa.frames_to_time(np.arange(len(o_env)), sr=sr)
onset_frames = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr)

# print (onset_frames)

p = 1
l = len(arr_bpm)
lo = len(onset_frames)
offset = 0
off = []
for i in range(len(onset_frames)):
    if p > l:
        break
    arr_off = []
    unit_bpm = arr_bpm[p - 1][0] / 8
    if (p == l):
        while (i < lo):
            arr_off.append((onset_frames[i] - arr_bpm[p - 1][1]) % unit_bpm)
            i = i + 1
        off.append(np.median(arr_off))
        break
    while(i < lo and onset_frames[i] < arr_bpm[p][1]):
        arr_off.append((onset_frames[i] - arr_bpm[p - 1][1]) % unit_bpm)
        i = i + 1
    i = i - 1
    p = p + 1
    #arr_bpm[p - 1][2] = 1
    if (len(arr_off) == 0):
        off.append(0)
    else:
        off.append(np.median(arr_off))

bpm_result = []
for i in range(l):
    bpm_result.append((times[arr_bpm[i][1]]+times[int(off[i])],arr_bpm[i][0]))
print (bpm_result)

with open("time_point_2.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerows(bpm_result)
# endtime = times[len(o_env)-1]
#bpm expension
matrix = []
count = 1
division = 1
for i in range(len(bpm_result)):
    t, bpm = bpm_result[i]
    simu_t = t
    if i < len(bpm_result) - 1:
        next_t = bpm_result[i+1][0]
    else:
        next_t = times[len(o_env)-1]
    delt = 1 / (division * (bpm / 60))
    while (simu_t < next_t):
        matrix.append((count, simu_t))
        simu_t += delt
        count += 1

# for i in range(len(matrix)):
#         if i < len(matrix) - 1:
#             print (matrix[i][1] - matrix[i+1][1])

bpm_result = [(i, 1000*t, o_env[librosa.core.time_to_frames(t, sr=sr)[0]]) for (i, t) in matrix] 

# print(bpm_result)
# np.savetxt('bpm_dynamic_2.csv', bpm_result, delimiter=',')
with open("bpm_dynamic_3.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerows(bpm_result)
