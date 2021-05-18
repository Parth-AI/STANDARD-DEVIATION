import csv
import math

with open('Data.csv', newline = '') as f:
     reader = csv.reader(f)
     file_data = list(reader)

data = file_data[0]
print(data)
def mean(data):
     n = len(data)
     total = 0
     for i in data:
          total += int(i)
     mean = total/n
     return mean

squared_list = []
for j in data:
     a = int(j)-mean(data)
     a = a**2
     squared_list.append(a)

sum = 0
for b in squared_list:
     sum = sum+b
result = sum/(len(data)-1)

std = math.sqrt(result)
print(std)
