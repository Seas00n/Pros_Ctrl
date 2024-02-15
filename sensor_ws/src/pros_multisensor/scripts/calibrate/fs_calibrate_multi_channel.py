import numpy as np
import scipy.io as scio
import matplotlib.pyplot as plt
import os
from scipy.ndimage import gaussian_filter1d
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
save_path = "/media/yuxuan/My Passport/test_hps/test_moco/"

exp_idx = 3

force_moca = scio.loadmat(save_path+"force{}.mat".format(exp_idx))["Trimmeddata{}".format(exp_idx)]
sample_rate = 1200

idx_moca = np.arange(0, np.shape(force_moca)[0])
t_moca = idx_moca*1/sample_rate

force_moca = force_moca[0::40]
t_moca = t_moca[0::40]
idx_moca = np.arange(0, np.shape(t_moca)[0])

plt.ion()
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)


ax1.plot(idx_moca[0:500], force_moca[0:500,2])
ax1.plot(idx_moca[0:500], force_moca[0:500,-1])
ax3.plot(idx_moca[-500:], force_moca[-500:,2])
ax3.plot(idx_moca[-500:], force_moca[-500:,-1])


f_l_data = []
f_r_data = []
t_pc = []
file_list = os.listdir(save_path+"{}/".format(exp_idx))
total_num = int(len(file_list)/2)

para_cal_l = np.load("./scripts/calibrate/left_cal.npy",allow_pickle=True)
para_cal_r = np.load("./scripts/calibrate/right_cal.npy",allow_pickle=True)

def Fun(x, paras):
    return paras[0]*x**2+paras[1]*x+paras[2]


for i in range(total_num):
    raw_data_l = np.load(save_path+"{}/fs_l_{}.npy".format(exp_idx, i+1),allow_pickle=True)
    raw_data_r = np.load(save_path+"{}/fs_r_{}.npy".format(exp_idx, i+1),allow_pickle=True)
    data_l = raw_data_l[1:]
    data_r = raw_data_r[1:]
    t_pc.append(raw_data_l[0])
    for j in range(18):
        if data_l[j] < 2:
            data_l[j] = 0
        if data_r[j] < 2:
            data_r[j] = 0
        # data_l[j] = Fun(data_l[j], paras=para_cal_l[j,:])*9.8
        # data_r[j] = Fun(data_r[j], paras=para_cal_r[j,:])*9.8
    f_l_data.append(data_l)
    f_r_data.append(data_r)

f_l_data = np.array(f_l_data)
f_l_data = gaussian_filter1d(f_l_data, 2,axis=0)
f_r_data = np.array(f_r_data)
f_r_data = gaussian_filter1d(f_r_data, 2,axis=0)
t_pc = np.array(t_pc)


f_l_net = f_l_data[:,3]*15.150+f_l_data[:,7]*30.836+f_l_data[:,10]*31.446+f_l_data[:,13]*8.001-18
f_r_net = -18+f_r_data[:,7]*30.836+f_r_data[:,13]*8.001+f_r_data[:,10]*31.446+f_r_data[:,3]*15.150

idx_pc = np.arange(0, np.shape(t_pc)[0])
ax2.plot(idx_pc[0:500], f_l_net[0:500])
ax2.plot(idx_pc[0:500], f_r_net[0:500])
ax4.plot(idx_pc[-500:],f_l_net[-500:])
ax4.plot(idx_pc[-500:],f_r_net[-500:])



idx_align = []
def on_press(event):
    global idx_align
    global ax1, ax2
    if len(idx_align) == 0:
        idx_align.append(int(event.xdata))
        idx = idx_align[-1]
        print("动捕起点:{}".format(idx))
        ax1.scatter(idx,force_moca[idx, -1], linewidths=5)
    elif len(idx_align) == 1:
        idx_align.append(int(event.xdata))
        idx = idx_align[-1]
        print("pc起点:{}".format(idx))
        ax2.scatter(idx, f_r_net[idx], linewidths=5)
    elif len(idx_align) == 2:
        idx_align.append(int(event.xdata))
        idx = idx_align[-1]
        print("动捕终点:{}".format(idx))
        ax3.scatter(idx,force_moca[idx, 2], linewidths=5)
    elif len(idx_align) == 3:
        idx_align.append(int(event.xdata))
        idx = idx_align[-1]
        print("pc终点:{}".format(idx))
        ax4.scatter(idx,f_l_net[idx], linewidths=5)   

fig.canvas.mpl_connect('button_press_event', on_press)
print("依次按下动捕起点(第一个橙色的起点)，pc起点(第二个橙色的起点)，动捕终点(最后一个蓝色的的终点)，pc终点（倒数第二个蓝色的终点）：")
try:
    while(len(idx_align)<4):
        plt.pause(0.5)
except KeyboardInterrupt:
    plt.close()

def Fun(x, a1, a2, a3, a4, a5):
    return a1*x[0]+a2*x[1]+a3*x[2]+a4*x[3]+a5

def error(p, x, y):
    return abs(Fun(p, x)-y)

a = input("是否存储【Y/N】")
if a == "Y":
    np.save("align_{}.npy".format(exp_idx),idx_align)
else:
    idx_align = np.load("align_{}.npy".format(exp_idx), allow_pickle=True)

print(idx_align)

idx_pc_chosen = np.arange(idx_align[1],idx_align[-1])-idx_align[1]
idx_moca_chosen = np.arange(idx_align[0], idx_align[2])-idx_align[0]
x = idx_moca_chosen
y = force_moca[idx_align[0]:idx_align[2], 2]
fun = interp1d(x, y, 'cubic')
xx = idx_pc_chosen
force_moca_align = fun(xx)

idx_fz_predictor = [3,7,10,13]
f_l_predictor = f_l_data[idx_align[1]:idx_align[-1], idx_fz_predictor].T
para, _ = curve_fit(Fun, f_l_predictor, force_moca_align, p0 = [15,30,31,8,-18])
print(para)

plt.close()
plt.ioff()
fig = plt.figure()
fz_l_new = []
# para = [15,30,31,8,-18]
for i in range(np.shape(f_l_predictor)[1]):
    fz_l_new.append(Fun(f_l_predictor[:,i], para[0],para[1],para[2],para[3],para[4]))

fz_l_new = np.array(fz_l_new)
plt.plot(xx, force_moca_align)
plt.plot(xx, fz_l_new)
plt.show()
