import os
import numpy as np 
import csv
import sys
import argparse
def update(rootDir): 
    dir = os.path.dirname(rootDir)
    newdir_path = os.path.join(dir, "norm_data")
    os.makedirs(newdir_path)
    for lists in os.listdir(rootDir): 
        print (os.path.splitext(lists)[1])
        if os.path.splitext(lists)[1] == ".csv":
            path = os.path.join(rootDir, lists)
            matrix = np.loadtxt(path, delimiter = ',')
            matrix = np.array(matrix)
            
            res = []
            for i in range (len(matrix[0])):
                col = matrix[:, i]
                # print (col)
                # print (norm(col))
                if i == 0 or (i >= 3 and i <= 14):
                    col = norm(col)
                res.append(col)
            
            res = list(map(list, zip(*res)))

            path_file = os.path.join(newdir_path, lists)
            with open(path_file, "w") as file:
                writer = csv.writer(file)
                writer.writerows(res)


def norm(col):
    min_bound = min(col)
    max_bound = max(col)
    print (min_bound)
    print (max_bound)
    for i in range(len(col)):
        col[i] = (col[i] - min_bound) / (max_bound - min_bound)
    # print (col)
    return col

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise argparse.ArgumentTypeError('the number of argument has to be 2')
        exit(-1)
    
    update(sys.argv[1])