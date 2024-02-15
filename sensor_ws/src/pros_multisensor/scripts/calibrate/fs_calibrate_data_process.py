import numpy as np
import os
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit


left_or_right = "left"
save_path = "/home/yuxuan/Desktop/cal_fp/"+left_or_right+"/"

def Fun(x, a1, a2,a3,a4):
    return a1*x+a2*np.exp(x)

# def error(p, x, y):
#     return Fun(x, p)-y


# plt.ion()
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax = fig.add_subplot(212)
plt.xlabel('Foot Plate Force/kg',fontweight='bold')
plt.ylabel('Six Force/kg',fontweight='bold')
para_list = []
for i in range(18):
    fp_data = np.load(save_path+"{}/fp_{}.npy".format(i+1,i+1))
    fp_data = fp_data-fp_data[0]
    six_data = np.load(save_path+"{}/six_{}.npy".format(i+1, i+1))
    six_data = six_data-six_data[0]
    ax.scatter(fp_data, six_data/10)
    para, pcov = curve_fit(Fun, fp_data, six_data/10)
    x = np.linspace(0, 65, 100)
    y = Fun(x, para[0], para[1],para[2],para[3])
    ax.plot(x, y)
    idx = np.arange(0,np.shape(fp_data)[0])
    ax1.cla()
    ax1.plot(idx, Fun(fp_data, para[0], para[1],para[2],para[3]))
    ax1.plot(idx, six_data/10)
    print(i+1)
    print(para)
    para_list.append(para)
    ax.set_xlim([0, 65])
    ax.set_ylim([0, 65])
    print()
plt.show()
np.save(left_or_right+"_cal.npy",np.array(para_list))    
    