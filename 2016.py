import numpy as np, matplotlib.pyplot as plt, math as m
alpha = 5.670373e-8 #Wm-2K-4
date_16 = np.arange(1,367,1)
TS00n_16 = [float(line.rstrip('\n')) for line in open('TS00n_16.txt')]
FCn_16 = [float(line.rstrip('\n')) for line in open('FCn_16.txt')]
LWOn_16 = [float(line.rstrip('\n')) for line in open('LWOn_16.txt')]
Tn_16 = np.zeros(len(date_16))

for i in range(len(date_16)):
    Tn_16[i] = m.pow(float(LWOn_16[i])/alpha,1/4) - 273.15

plt.plot(date_16,TS00n_16,c='r')
plt.plot(date_16,Tn_16)