import csv
import numpy as np

fl_id = []
fl_pass = []
n_pass = []

with open("/Users/harshsharan/Documents/Cloud Computing/Data/AComp_Passenger_data_no_error.csv", "r") as csv_file:
    csv_reader1 = csv.reader(csv_file, delimiter=',')
    for line in csv_reader1:
        if line[1] not in fl_id:
            fl_id.append(line[1])
            fl_pass.append(0)

with open("/Users/harshsharan/Documents/Cloud Computing/Data/AComp_Passenger_data_no_error.csv", "r") as csv_file:
    csv_reader1 = csv.reader(csv_file, delimiter=',')
    for lines in csv_reader1:
        # print(lines[1],lines[2])
        for idx, val in enumerate(fl_id):

            if (lines[1] == val):
                fl_pass[idx] = fl_pass[idx] + 1

fin = np.column_stack((fl_id, fl_pass))
print("Flight ID    No_of_Passenger")
print(fin)

# Writing the result in a text file
with open("/Users/harshsharan/Documents/Cloud Computing/Data/output_3.txt", "w") as f:
    fin = np.column_stack((fl_id, fl_pass))
    print("Flight ID    No_of_Passenger", file=f)
    print(fin, file=f)

f.close()