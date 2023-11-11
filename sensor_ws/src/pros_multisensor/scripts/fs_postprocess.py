import numpy as np
import matplotlib.pyplot as plt
from damper_interp import *

save_path = "/media/yuxuan/My Passport/testFootPlate/"  
bag_idx = 5
mg = 700

force_l = np.load(save_path+"data{}/{}_l.npy".format(bag_idx,0))
force_r = np.load(save_path+"data{}/{}_r.npy".format(bag_idx,0))

time = force_l[:3000,0]
f_net_l = force_l[:3000,-3]
f_net_r = force_r[:3000,-3]

dt = time[1]-time[0]
fig = plt.figure()
grid = plt.GridSpec(2,4,wspace=0.5,hspace=0.5)
ax0 = plt.subplot(grid[0,:])
ax1 = plt.subplot(grid[1,0])
plt.ion()

ax0.plot(time,f_net_l)
ax0.set_xlabel("Time(s)")
ax0.set_ylabel("Fz(N)")


stance_buffer = []
stance_0 = 0
stance_end = 0
stance_threshold = 50
stance_min_frame = 60
swing_min_frame = 20
phase = "stance"
num_stance = 0
for i in range(np.shape(f_net_l)[0]):
    f_i = f_net_l[i]
    if phase == "stance":
        stance_buffer.append(f_i)
    if f_i < stance_threshold and phase == "stance":
        stance_end = i #此刻已进入swing，当前时刻0已存储
        if stance_end-stance_0>stance_min_frame:
            print("Left Foot Change to Swing Phase")
            phase = "swing"
            if num_stance > 0:
                ax0.scatter(time[stance_0],f_net_l[stance_0],c="r",marker="o",linewidths=2)
                ax0.scatter(time[stance_end],f_net_l[stance_end],c="g",marker="o",linewidths=2)
                ax0.plot(time[stance_0:stance_end],np.array(stance_buffer),linewidth=2)
                ax1.cla()
                ax1.plot(np.linspace(0,100,len(stance_buffer)),np.array(stance_buffer)/mg)
                ax1.set_xlabel("Phase(%)")
                ax1.set_ylabel("Fz/Mg")
                plt.show()
            stance_buffer = []
            num_stance += 1
    elif f_i > stance_threshold and phase == "swing":
        stance_0 = i-1 #此刻已经进入stance, 从前一时刻存储0
        if stance_0-stance_end>swing_min_frame:
            print("Left Foot Change to Stance Phase")
            phase = "stance"
            stance_buffer.append(0)# stance_0
    
print()