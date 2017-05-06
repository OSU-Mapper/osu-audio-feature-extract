#python createmaps.py "537310_ly.osu"
import sys
import librosa
import argparse
import csv
import numpy as np
import os
# from mp3_mis_to_tr_f import closestindex


# def ishitobject(x, y):
#     y_copy = [[] for i in range(len(y))]
#     startindex = 0
#     for i in range(len(x)):
#         index = closestindex(int(x[i][2]), y)
#         if len(y_copy[index + startindex]) == 0:
#             y_copy[index + startindex] = [int(x[i][0]), int(x[i][1]), 1]
#         startindex += index
#         y = y[index:]
#     for i in range(len(y_copy)):
#         if len(y_copy[i]) == 0:
#             y_copy[i] = [0, 0, 0]
#     return y_copy

# def closestindex(x, y):
#     for i in range(len(y)):
#         if y[i][2] == x:
#             return i
#         elif y[i][2] > x:
#             if i == 0 or abs(y[i][2] - x) <= abs(y[i-1][2] - x):
#                 return i
#             else:
#                 return i - 1
#     if i == len(y) - 1:
#         return i

# def ishitobject(x, y):
#     # print (y[:50])
#     y_copy = [[] for i in range(len(y))]
#     startindex = 0
#     for i in range(len(x)):
#         index = closestindex(x[i][2], y)
#         # print (x[i][2])
#         # print (index)
#         if len(y_copy[index + startindex]) == 0:
#             y_copy[index + startindex] =  y[index] +  [1, int(x[i][4]), str(int(x[i][5])) + ":" + str(int(x[i][6])) + ":" + str(int(x[i][7])) + ":" + str(int(x[i][8])) + ":"]
#         startindex += index
#         y = y[index:]
#     res = []
#     # print (y_copy)
#     for e in y_copy:
#         if e != []:
#             res.append(e)
#     # print (x[:10])
#     # print (res)
#     return res

def merge(mis, res):
    # print (len(mis))
    # print (len(res))
    res = np.hstack([res, mis])
    # print (res)
    mis = []
    for i in range(len(res)):
        if (res[i][2] == 1):
            mis.append([int(res[i][0]), int(res[i][1]), int(float(res[i][3]))] + [1,0,"0:0:0:0:"])
    # print (mis)
    return mis

def read(filepath, mis, bpm, res):
    contents = []
    # mis = [x[1] for x in mis]
    tp = [[int(1000 * x[3]), 60000 / x[2]] for x  in bpm]
    # print (tp)

    with open(filepath, 'r') as my_file:
        csvreader = csv.reader(my_file)
        target = "Creator"
        for line in csvreader:
            if len(line) == 0:
                contents.append(line)
            else:
                l = line[0].split(':')
                if target not in l[0]:
                    contents.append(line)
                else:
                    contents.append(['Creator:Luying and Mengwei'])
                    break
        target = "Version"
        for line in csvreader:
            if len(line) == 0:
                contents.append(line)
            else:
                l = line[0].split(':')
                if target not in l[0]:
                    contents.append(line)
                else:
                    contents.append(['Version:Luying and Mengwei'])
                    break
        target = "BeatmapID"
        for line in csvreader:
            l = line[0].split(':')
            if target not in l[0]:
                contents.append(line)
            else:
                break
        target = "[TimingPoints]"
        for line in csvreader:
            if target not in line:
                contents.append(line)
            else:
                contents.append(line)
                break
        next_row = next(csvreader) 
        timing_poing_extra = next_row[2:]
        for x in tp:
            contents.append(x + timing_poing_extra)
        for line in csvreader:
            if len(line) == 0:
                contents.append(line)
                break
        target = "[HitObjects]"
        for line in csvreader:
            if target not in line:
                contents.append(line)
            else:
                contents.append(line)
                break
        
        # print (contents)
        hits = merge(mis, res)
        # hitobjects = ishitobject(hitobject, mis)
        contents += hits
        # print (contents)
        return (contents)


def recover_coor(col, min_bound, max_bound):
    for i in range(len(col)):
        col[i] = col[i] * (max_bound - min_bound) + min_bound
    return col

def target_norm(col):
    min_bound = min(col)
    max_bound = max(col)
    for i in range(len(col)):
        col[i] = (col[i] - min_bound) / (max_bound - min_bound)
    return col

def small_norm(col):
    min_bound = min(col)
    max_bound = max(col)
    for i in range(len(col)):
        col[i] = 0.8 * (col[i] - min_bound) / (max_bound - min_bound) + 0.1
    return col

def threshold(col, thresh):
    for i in range(len(col)):
        if col[i] >= thresh:
            col[i] = 1
        else:
            col[i] = 0
    return col

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise argparse.ArgumentTypeError('the number of argument has to be 2')
        exit(-1)

    path = "/Users/yanmingjun/Documents/osu-audio-feature-extract/Data/Beatmaps/537310 TO-MAS feat. Chima - FLIP FLAP FLIP FLAP/Trainings/"
    output_path = "/Users/yanmingjun/Documents/osu-audio-feature-extract/Data/Trainables/"
    osu_path = "/Users/yanmingjun/Documents/osu-audio-feature-extract/Data/Beatmaps/537310 TO-MAS feat. Chima - FLIP FLAP FLIP FLAP/"
    output_file = os.path.join(output_path, "refined_predict.csv")
    mis_file = os.path.join(path, "mis.v1.csv")
    dy_bpm_file = os.path.join(path, "timing_points.v1.csv")
    osu_file = os.path.join(osu_path, "TO-MAS feat. Chima - FLIP FLAP FLIP FLAP (Lanturn) [1.71].osu")
    # hitobject_file = os.path.join(path, "Oyasumi.target_features.v1.csv")
    # with open(mis_file, 'r') as my_file:
    #     csvreader = csv.reader(my_file)
    #     mis = list(csvreader)
    #     mis = np.array(mis)
        
    
    mis = np.loadtxt(mis_file, delimiter = ',')
    mis = mis[:,1:2]

    # with open(dy_bpm_file, 'r') as my_file:
    #     csvreader = csv.reader(my_file)
    #     bpm = list(csvreader)
    bpm = np.loadtxt(dy_bpm_file, delimiter = ',')

    
    # with open(output_file, 'r') as my_file:
    #     csvreader = csv.reader(my_file)
    #     res = list(csvreader)
    #     res = np.array(res)
    #     res = res[:,15:18]
    

    res = np.loadtxt(output_file, delimiter = ',')
    # res = res[:,15:18]
    x_coor = res[:,0]
    x_coor = small_norm(x_coor)
    # print (x_coor)
    x_coor = recover_coor(x_coor, 0, 512)

    y_coor = res[:,1]
    y_coor = small_norm(y_coor)
    
    y_coor = recover_coor(y_coor, 0, 384)
    # print (y_coor)
    is_hit = res[:,2]
    is_hit = target_norm(is_hit)
    # is_hit = threshold(is_hit, 0.9)
    # is_hit = threshold(is_hit, 0.75)
    is_hit = threshold(is_hit, 0.5)

    res = np.vstack([x_coor, y_coor, is_hit]).transpose() 
    # is_hit = threshold(is_hit, 0.75)
    # is_hit = threshold(is_hit, 0.9)
    # with open(hitobject_file, 'r') as my_file:
    #     csvreader = csv.reader(my_file)
    #     hitobject = list(csvreader)
    
    # hitobject = np.loadtxt(hitobject_file, delimiter = ',')
    text = read(osu_file, mis, bpm, res)

    with open(sys.argv[1], "w") as file:
        writer = csv.writer(file)
        writer.writerows(text)