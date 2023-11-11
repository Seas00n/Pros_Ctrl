import numpy as np
import matplotlib.pyplot as plt
from damper_interp import *

save_path = "/media/yuxuan/My Passport/testFootPlate/"  
bag_idx = 3

force_l = np.load(save_path+"data{}/{}_l.npy".format(bag_idx,0))
force_r = np.load(save_path+"data{}/{}_r.npy".format(bag_idx,0))

time = force_l[:2000,0]
f_net_l = force_l[:2000,-3]
f_net_r = force_r[:2000,-3]

dt = time[1]-time[0]
f_net_l_interp = np.zeros_like(f_net_l)
f_net_l_interp[0] = f_net_l[0]
f_net_r_interp = np.zeros_like(f_net_r)
f_net_r_interp[0] = f_net_r[0]
for i in range(np.shape(time)[0]-1):
    if f_net_l[i+1] == 0:
        f_net_l_interp[i+1] = 0
    else:
        f_net_l_interp[i+1],_ = critical_spring_damper_exact(f_net_l_interp[i],0,f_net_l[i+1],0,halflife=0.02,dt=dt*1.2)

    if f_net_r[i+1] == 0:
        f_net_r_interp[i+1] = 0
    else:
        f_net_r_interp[i+1],_ = critical_spring_damper_exact(f_net_r_interp[i],0,f_net_r[i+1],0,halflife=0.02,dt=dt*1.2)


plt.plot(time,f_net_l_interp)
# plt.plot(time,f_net_l)
plt.show()
print()