import numpy as np
from numpy import genfromtxt
from decimal import *

c = genfromtxt(open(raw_input("Enter the name of the csv file containing origin zones target trips: " ),'r'), delimiter=',')
cc = genfromtxt(open(raw_input("Enter the name of the csv file containing destination zones target trips: " ),'r'), delimiter=',')
e = genfromtxt(open(raw_input("Enter the name of the csv file containing current network trips: " ),'r'), delimiter=',')

ci = np.array([0])
cci = np.array([0])

a = np.subtract(ci, c)
b = np.subtract(cci, cc)

if np.size(c,0) != np.size(e,0):
    print "target matrix row numbers not the same as initial matrix row numbers"
    exit
elif (cc.shape[0] != e.shape[1]):
    print "target matrix column numbers not the same as initial matrix column numbers"
    exit
elif np.sum(c,0) != np.sum(cc,0):
    print "target origin trips sum not equal target destination trips sum"
    exit
else:
    filepathLog1 = "results1.txt"
    file_object1 = open(filepathLog1, 'w')
    def writeReport(file_object,info):
        file_object1.write(info)
        file_object1.flush()
    count = 0
    while (a.all>0.001) and (b.all>0.001):
        for row in range (0, np.size(e,1)):
            for column in range (0,np.size(e,0)):
                e2 = e * c[:, np.newaxis]
                denom = e.sum(axis=1, keepdims=True)
                denom = 1/denom
                e3 = e2 * denom
                row += row
                #----------------------------------------
                e4= e3 * cc[np.newaxis,:]
                denom2 = e3.sum(axis=0, keepdims=True)
                denom2 = 1/denom2
                e = e4 * denom2
                ci=e.sum(axis=1, keepdims=True)
                a = np.subtract(ci, c)
                cci=e.sum(axis=0, keepdims=True)
                b = np.subtract(cci, cc)
                count = count+1
                column += column
            n = np.matrix(e)
            np.savetxt('results1.txt', n)
        break
