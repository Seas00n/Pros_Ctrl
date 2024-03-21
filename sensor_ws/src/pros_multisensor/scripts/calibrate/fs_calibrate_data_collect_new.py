import numpy as np
import pyqtgraph as pg
import time
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import serial
import threading
win = pg.GraphicsLayoutWidget(show=True)


p1 = win.addPlot()
p1.setYRange(-0.1,5)

data1 = np.zeros((100,))

curve1 = p1.plot(data1, pen=pg.mkPen(color=(255,0,0,150), width=3))

data2 = np.zeros((100,))

curve2 = p1.plot(data2, pen=pg.mkPen(color=(0,255,0,150), width=3))

master = modbus_rtu.RtuMaster(
    serial.Serial(
        port="/dev/ttyUSB0", baudrate=9600,
        bytesize=8, parity="N",
        stopbits=1, xonxoff=0
    )
)
master.set_timeout(1.0)

master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 0, output_value=[0,0,0,0])

save_path = "/home/yuxuan/Desktop/cal_fp/fp_new_right/"
fp_buffer_path =  "/home/yuxuan/Project/HPS_Perception/map_ws/src/HPS_Perception/hps_moco/scripts/fp/log/right45.npy"

fp_buffer = np.memmap(fp_buffer_path, mode='r', dtype='float16', shape=(45,))

chosen_idx = 41

save_list = []
max_save_len = 200
save_begin = False

f = 0

fp_slow_buffer = np.zeros(20,)
def update():
    global data1, data2, curve1, curve2, fp_buffer, chosen_idx, save_list, save_begin, master
    global f, fp_slow_buffer
    if chosen_idx <45:
        fp_slow_buffer[:-1] = fp_slow_buffer[1:]
        fp_slow_buffer[-1] = fp_buffer[chosen_idx]
        fp = fp_slow_buffer[-7]
        if save_begin:
            data1[:-1] = data1[1:]
            data2[:-1] = data2[1:]
            data1[-1] = f
            data2[-1] = fp*0.001
            if len(save_list) < max_save_len:
                save_list.append([f, fp])
                curve1.setData(data1)
                curve2.setData(data2)

pg_close = False

def f_collect_job():
    global f, master, pg_close
    while not pg_close:
        res_tuple = master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 2)
        if res_tuple[0] == 65535:
            f_bytes = b'\x00'
        else:
            f_bytes = int(res_tuple[0]).to_bytes(2,byteorder='big')+int(res_tuple[1]).to_bytes(2,byteorder='big')
        f = 0.01*int.from_bytes(f_bytes, byteorder="big",signed=True)

def update_test():
    global data1, data2, curve1, curve2, fp_buffer, chosen_idx, save_list, save_begin, master
    if chosen_idx < 45:
        if save_begin:
            data1[:-1] = data1[1:]
            data2[:-1] = data2[1:]
            data1[-1] = len(save_list)*0.005
            data2[-1] = len(save_list)*0.01
            if len(save_list) < max_save_len:
                save_list.append([0, 0])
                curve1.setData(data1)
                curve2.setData(data2)


def cmd_job():
    global data1, data2, chosen_idx, save_begin, save_list, pg_close, save_path
    while not pg_close:
        if not save_begin:
            input("请将传感器贴在第{}片".format(chosen_idx))
            save_begin = True
        else:
            print(len(save_list))
            if len(save_list) == max_save_len:
                cmd = input("存储第{}片数据".format(chosen_idx))
                if cmd == 'y':
                    np.save(save_path+"{}.npy".format(chosen_idx), np.array(save_list))
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
            

if __name__=="__main__":
    timer = pg.QtCore.QTimer()
    timer.timeout.connect(update)
    timer.start(50)
    f_collect_thread = threading.Thread(target=f_collect_job)
    f_collect_thread.start()
    cmd_thread = threading.Thread(target=cmd_job)
    cmd_thread.start()
    pg.exec()
    pg_close = True

                    
