import csv

data_rows=[]

with open('data.csv','r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        data_rows.append(row)

if __name__ == "__main__":
    for i in range(0,15):
        print(data_rows[i])

    input = data_rows[17]
    for i in range(0,15):
        sum = 0
        for j in range(1,7):
            sum+=(float(data_rows[i][j])-float(input[j]))*(float(data_rows[i][j])-float(input[j]))
        print(data_rows[i][0],sum)

