import numpy as np
import matplotlib.pyplot as plt

f_p = np.load("/home/yuxuan/Desktop/cal_fp/left_multi_step.npy", allow_pickle=True)

t = f_p[:,-1]

plt.ion()
fig = plt.figure()
ax = plt.subplot(211)
ax2 = plt.subplot(212)

for i in range(np.shape(f_p)[1]-1):
    ax.plot(t, f_p[:,i])
    print("[{}]".format(i),max(f_p[:,i]),min(f_p[:,i]))
    plt.show()
    ax.cla()
f_net = np.sum(f_p[:,0:-1],axis=1)
# f_net = f_net - f_net[0]
ax2.plot(t, f_net)
plt.show()
print()
