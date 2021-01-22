import csv
import numpy as np

arr2 = []
arr = []
arr1 = []

# Open the file
with open('/Users/harshsharan/Documents/Cloud Computing/Data/Top30_airports_LatLong(1).csv', 'r') as csvfile:


    csvReader2 = csv.reader(csvfile, delimiter = ',')

# Reading each row from the file
    for row in csvReader2:
# Check if row is empty
        if not (row):
            continue
    # Save Airport name and Airport code in Array
        arr2.append(row[0])
        arr.append(row[1])
        arr1.append(0)


with open("/Users/harshsharan/Documents/Cloud Computing/Data/AComp_Passenger_data_no_error.csv", "r") as csv_file:
    csv_reader1 = csv.reader(csv_file, delimiter=',')

    for lines in csv_reader1:
# Getting index and its value from array elements
        for idx,val in enumerate(arr):
# Comparing Airport Code with Flight Data
            if(lines[2]==val):
                arr1[idx] = arr1[idx]+ 1

        for idx,val in enumerate(arr):
# Calculating number of flight for each airport
            if(lines[3]==val):
                arr1[idx] = arr1[idx]+ 1

# Creating a list of objective 1
obj1 = np.column_stack((arr2,arr,arr1))
obj2 = []

# Creating a list of unused airport
for i in obj1:
    k = 0;
    if (i[2]=='0'):
        obj2.insert(k, i)
        k = k+1

print("Number of Flights on Each Airport")
print(obj1)

print("Number of Airports not used")
for val in obj2:
    print(val)

# Writing the outputs in file
with open("/Users/harshsharan/Documents/Cloud Computing/Data/output_1.txt", "w") as f:
    print("Number of Flights on Each Airport", file=f)
    print(obj1, file=f)

    print("Number of Airports not used", file=f)
    for val in obj2:
        print(val, file=f)
f.close()


