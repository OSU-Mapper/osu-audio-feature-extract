#python tp_to_mis.py "dynamic_bpm.csv" "mis.csv"
import sys
import csv
import argparse

def getMIS(dy_bpm):
    mis_result = []
    count = 1
    division = 8
    for i in range(len(dy_bpm)):
        srat_t, next_t, bpm = dy_bpm[i]
        srat_t = 1000 * float(srat_t)
        next_t = 1000 * float(next_t)
        bpm = float(bpm)
        simu_t = srat_t
        delt = 1000 / (division * (bpm / 60)) 
        while (simu_t < next_t):
            mis_result.append([count, simu_t])
            simu_t += delt
            count += 1
    return mis_result

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print( "usage: inputfile outputfile")
        raise argparse.ArgumentTypeError('the number of argument has to be 3')
        exit(-1)

    with open(sys.argv[1], 'r') as my_file:
        csvreader = csv.reader(my_file)
        dy_bpm = list(csvreader)

    mis_result = getMIS(dy_bpm)

    with open(sys.argv[2], "w") as file:
        writer = csv.writer(file)
        writer.writerows(mis_result)