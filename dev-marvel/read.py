import csv 
import sys
# echo 'backend: TkAgg' > ~/.matplotlib/matplotlibrc
# 
import matplotlib.pyplot as plt

x_v = []
y_v = []
 
f = open('positions.txt', 'r')
reader = csv.reader(f)

name=0
x=1
y=2
for row in reader:
    print (row)
    row[name] = int(row[name])
    print (row[name])
    for i in [x,y]:
        row[i] = float(row[i])
    print (row[x], type(row[x]))
    x_v.append(row[x])
    y_v.append(row[y])

f.close()




print (x_v)
print(y_v)
plt.scatter(x_v, y_v)

plt.show()
