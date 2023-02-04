import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import csv
from numpy import log 
import math
import os 
pi  = 3.1415
e = 2.71828

for filename in os.listdir('File directory'):
    print (filename)
    
    path_1 = 'Directory'
    
    #Read data from R&S file 
    file1 = path_1 + filename
    with open(file1) as fp:

        rows = []
        xval = []
        yval = []
        tval = [[]]
        n = 28
        while n>0:
            line = fp.readline()
            n = n -1
        x = str(line).split(';')
        m = int(x[1])
        i = 0
        while m > 0:
            line = fp.readline()
            x = str(line).split(';')
            xval.append(float(x[0]))
            yval.append(float(x[1]))
            m = m - 1
            i = i+ 1
    print(len(xval))
    
    f_name = filename.split('.')
    print (f_name)
    
    path = 'directory' + f_name[0] + '-2csv.csv'
    
    file = open(path, 'w')
    
    writer = csv.writer(file)
    n = 625
    i = 0
    array = []
    while n >0:
        data = []
        data.append(xval[i])
        data.append(yval[i])
        i= i+1
        writer.writerow(data)
        n = n - 1

    file.close()
    
file1 = path_1 + filename
with open(file1) as fp:

    rows = []
    xval = []
    yval = []
    tval = [[]]
    n = 28
    while n>0:
        line = fp.readline()
        n = n -1
    x = str(line).split(';')
    m = int(x[1])
    i = 0
    while m > 0:
        line = fp.readline()
        x = str(line).split(';')
        xval.append(float(x[0]))
        yval.append(float(x[1]))
        m = m - 1
        i = i+ 1
print(len(xval))
    
f_name = filename.split('.')
print (f_name)
path = 'directory' + f_name[0] + '-2csv.csv'
    
file = open(path, 'w')
    
writer = csv.writer(file)
n = 625
i = 0
array = []
while n >0:
    data = []
    data.append(xval[i])
    data.append(yval[i])
    i= i+1
    writer.writerow(data)
    n = n - 1

file.close()
    