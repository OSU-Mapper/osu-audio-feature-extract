#python tr_f_tr_t_to_trainable.py "tr_f.csv" "tr_t.csv"
import csv 
import sys
import argparse

def merge(tr_f, tr_t):
    return [tr_f[i] + tr_t[i] for i in range(len(tr_t))]


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise argparse.ArgumentTypeError('the number of argument has to be 3')
        exit(-1)
    
    with open(sys.argv[1], 'r') as my_file:
        csvreader = csv.reader(my_file)
        tr_f = list(csvreader)
    
    with open(sys.argv[2], 'r') as my_file:
        csvreader = csv.reader(my_file)
        tr_t = list(csvreader)
    
    Train_result = merge(tr_f, tr_t)

    writer = csv.writer(sys.stdout)
    writer.writerows(Train_result)

    # with open("Train_result.csv", "w") as file:
    #     writer = csv.writer(file)
    #     writer.writerows(Train_result)