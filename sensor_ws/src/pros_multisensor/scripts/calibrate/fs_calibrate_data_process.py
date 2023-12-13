import numpy as np
import os
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit



save_path = "/home/yuxuan/Desktop/cal_fp/left/"

def Fun(x, a1, a2, a3):
    return a1*x**2+a2*x+a3

def error(p, x, y):
    return Fun(p, x)-y


plt.ion()
fig = plt.figure()
ax = fig.add_subplot()
plt.xlabel('Foot Plate Force/kg',fontweight='bold')
plt.ylabel('Six Force/kg',fontweight='bold')
for i in range(18):
    fp_data = np.load(save_path+"{}/fp_{}.npy".format(i+1,i+1))
    six_data = np.load(save_path+"{}/six_{}.npy".format(i+1, i+1))
    ax.scatter(fp_data, six_data/10)
    para, pcov = curve_fit(Fun, fp_data, six_data/10)
    x = np.linspace(0, 65, 100)
    y = Fun(x, para[0], para[1], para[2])
    ax.plot(x, y)
    print(i+1)
    print(para)
    plt.show()
    print()

    
    