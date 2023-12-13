import numpy as np
import matplotlib.pyplot as plt
from damper_interp import *
from gmm_kmp.algo import *
import time

save_path = "/media/yuxuan/My Passport/testFootPlate/"
gif_path = "/media/yuxuan/My Passport/testFootPlate/gif/"
bag_idx = 5
mg = 60

force_l = np.load(save_path+"data{}/{}_l.npy".format(bag_idx,0))
force_r = np.load(save_path+"data{}/{}_r.npy".format(bag_idx,0))

t = force_l[150:2000,0]
f_net_l = force_l[150:2000,-3]
f_net_r = force_r[150:2000,-3]
gk = kernel(2,2)

dt = t[1]-t[0]
fig = plt.figure(figsize=(10,6))
plt.ion()
plt.show(block=False)
grid = plt.GridSpec(2,4,wspace=0.5,hspace=0.5)
ax0 = plt.subplot(grid[0,:])
scan_ = ax0.plot(np.array([t[0],t[0]+0.01]),
                 np.array([f_net_l[0],f_net_l[0]+0.01]),
                 c='black',linewidth=5)[0]
ax0.plot(t[0:-1], f_net_l[0:-1],color="gray")
kmp_state_ = ax0.text(10,620,"")
ax0.set_xlabel("Time(s)")
ax0.set_ylabel("Fz(N)")

ax1 = plt.subplot(grid[1,0])
smooth_ = ax1.plot(np.zeros(1, ),np.zeros(1, ), "b--", linewidth=2,label="smooth")[0]
origin_ = ax1.plot(np.zeros(1, ),np.zeros(1, ), linewidth=2, color='gray',alpha=0.5,label="raw")[0]
ax1.set_xlim([-0.2,1.5])
ax1.set_ylim([0,12])
ax1.legend(loc="lower center",prop={'size':8},labelspacing=0.4)
ax1.set_title("Online Smooth Result")
ax1.set_xlabel("Time(s)")
ax1.set_ylabel("Fz/M(m·s-2)")

ax2 = plt.subplot(grid[1,1])
ax2.set_xlabel("Phase(%)")
ax2.set_ylabel("Fz/M(m·s-2)")
ax2.set_title("Feature Point")

ax3 = plt.subplot(grid[1,2])
ax3.set_xlabel("Phase(%)")
ax3.set_ylabel("Fz/M(m·s-2)")
ax3.set_title("KMP Result")




stance_buffer = []
stance_buffer_online_filter = np.zeros((0,))
stance_0 = 0
stance_end = 0
stance_threshold = 50
stance_min_frame = 60
swing_min_frame = 20
phase = "stance"
num_stance = 0
num_swing = 0

fp_pipeline = gmm_kmp_fp_pipeline()

for i in range(np.shape(f_net_l)[0]):
    try:
        f_i = f_net_l[i]
        if num_swing > 0:
            stance_buffer_online_filter = np.hstack([stance_buffer_online_filter,
                                                    online_gaussian_filter(f_net_l[i-4:i+1],gk)/mg])
            smooth_.set_xdata(t[stance_0:stance_0+np.shape(stance_buffer_online_filter)[0]]-t[stance_0])
            smooth_.set_ydata(stance_buffer_online_filter)
            origin_.set_xdata(t[stance_0:stance_0+np.shape(stance_buffer_online_filter)[0]]-t[stance_0])
            origin_.set_ydata(f_net_l[stance_0:stance_0+np.shape(stance_buffer_online_filter)[0]]/mg)
        if np.mod(i,5) == 0:
            scan_.set_xdata([t[i]-0.005,t[i]+0.005])
            scan_.set_ydata([f_net_l[i]-0.005,f_net_l[i]+0.005])
        if phase == "stance" and num_swing>0:
            kmp_state_.set_text("Stance Store Current Gait")
            kmp_state_.set_color("r")
        elif phase=="swing" and num_swing>0:
            kmp_state_.set_text("Enter Swing KMP Rebuild Last Gait")
            kmp_state_.set_color("g")



        if phase == "stance":
            stance_buffer.append(f_i)
        if f_i < stance_threshold and phase == "stance":
            stance_end = i #此刻已进入swing，当前时刻0已存储
            if stance_end-stance_0>stance_min_frame:
                print("Left Foot Change to Swing Phase")
                phase = "swing"
                if num_stance > 0:
                    #############################################
                    # 提取和重构
                    #############################################
                    stance_vec = np.array(stance_buffer)/mg
                    # fp_pipeline.fast_fea(stance_vec=stance_vec)
                    fp_pipeline.extract_fea(stance_vec=stance_vec)
                    fp_pipeline.kmp_rebuild()
                    #########################################################################
                    # 下面全是画图的
                    #########################################################################
                    col = (np.random.random(), np.random.random(), np.random.random())
                    ax0.scatter(t[stance_0],f_net_l[stance_0],c="r",marker="o",linewidths=1)
                    ax0.scatter(t[stance_end],f_net_l[stance_end],c="g",marker="o",linewidths=1)
                    ax0.plot(t[stance_0:stance_end],np.array(stance_buffer),linewidth=2,c=col)
                    #########################################################################
                    ax2.cla()
                    ax2.plot(np.linspace(0,100,len(stance_buffer)),stance_vec,c=col,linewidth=5,alpha=0.4)
                    ax2.plot(fp_pipeline.Phase*100,fp_pipeline.stance_cubic,'b--')
                    ax2.scatter(fp_pipeline.Phase[fp_pipeline.via_idx]*100,
                                fp_pipeline.via_point[:,0],c='b',linewidths=1,label="fea point")
                    ax2.set_xlabel("Phase(%)")
                    ax2.set_ylabel("Fz/M(m·s-2)")
                    ax2.set_title("Feature Point")
                    ax2.legend(loc="lower center")
                    #########################################################################
                    ax3.cla()
                    ax3.plot(fp_pipeline.Phase*100,fp_pipeline.stance_cubic,'b--')
                    ax3.plot(fp_pipeline.Phase*100,fp_pipeline.DataNew[:,0],'r',lw=5,alpha=0.2,label="GMR ref")
                    ax3.plot(fp_pipeline.Phase*100,fp_pipeline.fz_rebuild,'m',lw=2,label='KMP traj')
                    ax3.scatter(fp_pipeline.Phase[fp_pipeline.via_idx]*100,
                                fp_pipeline.via_point[:,0],c='b',linewidths=1)
                    ax3.set_xlabel("Phase(%)")
                    ax3.set_ylabel("Fz/M(m·s-2)")
                    ax3.set_title("KMP Result")
                    ax3.legend(loc="lower center",prop={'size':8},labelspacing=0.4)
                stance_buffer = []
                num_stance += 1
        elif f_i > stance_threshold and phase == "swing":
            stance_0 = i-1 #此刻已经进入stance, 从前一时刻存储0
            if stance_0-stance_end>swing_min_frame:
                print("Left Foot Change to Stance Phase")
                phase = "stance"
                stance_buffer.append(0)# stance_0
                stance_buffer_online_filter = np.array(stance_buffer_online_filter[-2:])
                num_swing += 1
        

        plt.draw()
        plt.pause(0.0005)
        plt.savefig(gif_path+"{}.png".format(i))
    except KeyboardInterrupt:
        plt.close()
        break

