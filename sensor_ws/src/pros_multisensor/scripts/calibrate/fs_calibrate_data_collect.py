import serial
import numpy as np
import time
import datetime
import pyqtgraph as pg
import threading

left_or_right = "right"

save_path = "/home/yuxuan/Desktop/cal_fp/fp_new_{}/".format(left_or_right)
fp_buffer_path =  "/home/yuxuan/Project/HPS_Perception/map_ws/src/HPS_Perception/hps_moco/scripts/fp/log/{}45.npy".format(left_or_right)
six_force_buffer_path = '/home/yuxuan/Project/Pros_Ctrl/sensor_ws/src/pros_multisensor/scripts/six_force_data.npy'
six_force_buffer = np.memmap(six_force_buffer_path, dtype='float32', mode='r', shape=(6,))
fp_buffer = np.memmap(fp_buffer_path, mode='r', dtype='float16', shape=(45,))

save_list = []
max_save_len = 400
save_begin = False


win = pg.GraphicsLayoutWidget(show=True)


p1 = win.addPlot()
p1.setYRange(-0.2, 200)

data1 = np.zeros((100,))

curve1 = p1.plot(data1, pen=pg.mkPen(color=(255,0,0,150), width=3))

data2 = np.zeros((100,))

curve2 = p1.plot(data2, pen=pg.mkPen(color=(0,255,0,150), width=3))

chosen_idx = 34

def update():
    global data1, data2, curve1, curve2, fp_buffer, chosen_idx, save_list, save_begin
    global fp_buffer, six_force_buffer
    if chosen_idx <45:
        if save_begin:
            data1[:-1] = data1[1:]
            data2[:-1] = data2[1:]
            data1[-1] = six_force_buffer[2]
            data2[-1] = fp_buffer[chosen_idx]
            if len(save_list) < max_save_len:
                save_list.append([data1[-1], data2[-1]])
                curve1.setData(data1)
                curve2.setData(data2*0.02)
pg_close = False

def cmd_job():
    global data1, data2, chosen_idx, save_begin, save_list, pg_close, save_path
    while not pg_close:
        if not save_begin:
            input("请将传感器贴在第{}片,按回车开始".format(chosen_idx))
            save_begin = True
        else:
            print(len(save_list))
            if len(save_list) == max_save_len:
                cmd = input("存储第{}片数据按y,其他重新采集".format(chosen_idx))
                if cmd == 'y':
                    # np.save(save_path+"{}.npy".format(chosen_idx), np.array(save_list))
                    chosen_idx += 1
                else:
                    print("重新采集")
                data1[:] = 0
                data2[:] = 0
                save_list = []
                save_begin = False
                if chosen_idx == 45:
                    print("采集完毕")
                    return
            time.sleep(0.01)

if __name__ == "__main__":
    timer = pg.QtCore.QTimer()
    timer.timeout.connect(update)
    timer.start(50)
    cmd_thread = threading.Thread(target=cmd_job)
    cmd_thread.start()
    pg.exec()
    pg_close = True

    