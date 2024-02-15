import serial
import numpy as np
import time
import datetime

import matplotlib.pyplot as plt

k_int2float = 10.0
b_int2float = 30000.0

chosen_idx = 3

save_path = "/home/yuxuan/Desktop/cal_fp/left/{}/".format(chosen_idx)

para_cal_l = np.load("./scripts/calibrate/left_cal.npy",allow_pickle=True)

total_count = 500


t0 = datetime.datetime.now()

p = np.zeros((19,))


def analyse_read_data(data_read):
    if data_read[0] == int(0xAA) and np.shape(data_read)[0]==37:
        for i in range(18):
            # print(2*(i-1)+4,data_read[2*(i-1)+4])
            # print(2*(i-1)+3,data_read[2*(i-1)+3])
            p[i] = data_read[2*(i-1)+4]*256+data_read[2*(i-1)+3]
            p[i] = (p[i]-b_int2float)/k_int2float*100.0/1000.0
        p[18] = (datetime.datetime.now()-t0).total_seconds()*0.001
    return p

def fifo_vec(data_vec, data):
    data_vec[0:-1] = data_vec[1:]
    data_vec[-1] = data
    return data_vec

def Fun(x, para):
    return para[0]*x+para[1]*np.exp(x)


if __name__ == "__main__":
    try:
        ser = serial.Serial(
            port = "/dev/ttyUSB0",
            baudrate=115200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=0.01
        )
        if ser.is_open:
            print("\033[32m [LOG]Serial is open\033[0m")
        else:
            print("\033[31m [ERROR]Serial not Open \033[0m")    
    except Exception as e:
        print("\033[31m [ERROR]Serial not Open | {}\033[0m".format(e))

    num_read_bytes = 37

    count_read = 2

    six_force_buf = np.memmap('/home/yuxuan/Project/Pros_Ctrl/sensor_ws/src/pros_multisensor/scripts/six_force_data.npy', 
                    dtype='float32', mode='r', shape=(6,))

    data_save = []
    six_force_data_save = []

    fig = plt.figure(figsize=(10,10))
    plt.ion()
    plt.grid(True)
    ax = fig.add_subplot(111)
    ax.set_xlabel('Frame(0-100)')
    ax.set_ylabel('Mass/kg')
    x_data = np.linspace(0,100,100)
    y1_data = np.zeros_like(x_data)
    y2_data = np.zeros_like(x_data)
    line1 = ax.plot(x_data, y1_data, linewidth=5)[0]
    line2 = ax.plot(x_data, y2_data,'--',linewidth=5)[0]
    ax.plot(x_data, np.ones_like(x_data)*65,linewidth=5)
    text = ax.text(10,50,"0",fontsize=40)
    plt.yticks(size=15)

    read_begin = False
    count = 0
    while not read_begin:
        bytes_read = ser.read(size=num_read_bytes)
        bytes_read = np.frombuffer(bytes_read, dtype=np.uint8)
        if np.shape(bytes_read)[0] == num_read_bytes and bytes_read[0] == 0xAA:
            count += 1
            print(bytes_read)
        print(count)
        if count > 50:
            read_begin = True
        time.sleep(0.01)

    try:
        while count_read < total_count:
            bytes_read = ser.read(size=num_read_bytes)
            bytes_read = np.frombuffer(bytes_read, dtype=np.uint8)
            print(np.shape(bytes_read))
            if np.shape(bytes_read)[0] == num_read_bytes and bytes_read[0]==int(0xAA):
                # print(bytes_read)
                p_fp = analyse_read_data(bytes_read)[chosen_idx-1]
                count_read += 1
                if p_fp >= 65:
                    p_fp = 65
                data_save.append(p_fp)
                print("FootPlate in Kg:", p_fp)
                six_force_p = np.copy(six_force_buf[:])[2]
                six_force_data_save.append(six_force_p)
                print("SixForce in Kg:", six_force_p/10)
                p_fp_cal = Fun(p_fp, para_cal_l[chosen_idx-1,:])
                y1_data = fifo_vec(y1_data, p_fp_cal)
                y2_data = fifo_vec(y2_data, six_force_p/10)
                text.set_text("{}".format(count_read))
            line1.set_ydata(y1_data)
            line2.set_ydata(y2_data)
            ax.set_xlim([0, 100])
            ax.set_ylim([-20, 80])
            plt.pause(0.01)
    except KeyboardInterrupt:
        plt.close()

    ser.close()
    np.save(save_path+"fp_{}.npy".format(chosen_idx),np.array(data_save))
    # np.save(save_path+"six_{}.npy".format(chosen_idx),np.array(six_force_data_save))