import math
import csv

with open ("data.csv", newline='') as f:
    reader= csv.reader(f)
    file_data= list(reader)

data=file_data[0]

def mean(data):
    l=len(data)
    entries=0
    for i in data:
        entries += int(i)
    mean= entries/l
    return mean

squaredList=[]
for i in data:
    value=int(i) - mean(data)
    value=value**2
    squaredList.append(i)

sum=0
for i in squaredList:
    sum += int(i)

result=sum/(len(data)-1)

std=math.sqrt(result)
print("Std_deviation =",std)