#python tp_to_mis.py "dynamic_bpm.csv" 
import sys
import csv
import argparse

def getMIS(dy_bpm):
    mis_result = []
    count = 1
    division = 4
    for i in range(len(dy_bpm)):
        start, next_t, bpm, start_t = dy_bpm[i]
        start_t = 1000 * float(start_t)
        next_t = 1000 * float(next_t)
        bpm = float(bpm)
        simu_t = start_t
        delt = 1000 / (division * (bpm / 60)) 
        while (simu_t < next_t):
            mis_result.append([count, simu_t])
            simu_t += delt
            count += 1
    return mis_result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print( "usage: inputfile outputfile")
        raise argparse.ArgumentTypeError('the number of argument has to be 2')
        exit(-1)

    with open(sys.argv[1], 'r') as my_file:
        csvreader = csv.reader(my_file)
        dy_bpm = list(csvreader)

    mis_result = getMIS(dy_bpm)

    # with open(sys.argv[2], "w") as file:
    #     writer = csv.writer(file)
    #     writer.writerows(mis_result)

    writer = csv.writer(sys.stdout)
    writer.writerows(mis_result)