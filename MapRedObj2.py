import csv
import numpy as np
import datetime as DT

Ufl_ID = []
FL_ID =[]
P_ID = []
A_Code = []
D_Code = []
D_Time = []
F_Time = []

with open("/Users/harshsharan/Documents/Cloud Computing/Data/AComp_Passenger_data_no_error.csv", "r") as csv_file:
    csv_reader1 = csv.reader(csv_file, delimiter=',')
    for line in csv_reader1:
        if line[1] not in Ufl_ID:
            Ufl_ID.append(line[1])

with open("/Users/harshsharan/Documents/Cloud Computing/Data/AComp_Passenger_data_no_error.csv", "r") as csv_file:
    csv_reader1 = csv.reader(csv_file, delimiter=',')
    for line in csv_reader1:
        FL_ID.append(line[1])
        P_ID.append(line[0])
        D_Code.append(line[2])
        A_Code.append(line[3])
        D_Time.append(DT.datetime.utcfromtimestamp(int(line[4])).strftime('%H:%M:%S'))
        F_Time.append(str(DT.timedelta(minutes=int(line[5]))))


P_Data = np.column_stack((FL_ID ,P_ID ,D_Code ,A_Code ,D_Time ,F_Time))

for fid in Ufl_ID:
    for i in P_Data:
        if (i[0] == fid):
            print(i)

    print("\n\n\n\n")

with open("/Users/harshsharan/Documents/Cloud Computing/Data/output_2.txt", "w") as f:
    for fid in Ufl_ID:
        for i in P_Data:
            if(i[0]==fid):
                print(i, file=f)

        print("\n\n\n\n", file=f)