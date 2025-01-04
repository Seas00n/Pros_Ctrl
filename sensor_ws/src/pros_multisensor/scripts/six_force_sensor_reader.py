import serial
import time
import struct
import numpy as np

ser = serial.Serial(
    port='/dev/ttyUSB0',
    #port='com7',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS, timeout=1e-2
)
time.sleep(1e-2)

def init_force():

    # 设置采样频率 100hz
    set_update_rate = "AT+SMPF=300\r\n".encode('utf-8')
    ser.write(bytearray(set_update_rate))
    # 上传数据格式
    set_recieve_format = "AT+SGDM=(A01,A02,A03,A04,A05,A06);E;1;(WMA:1)\r\n".encode('utf-8')
    ser.write(bytearray(set_recieve_format))
    get_data_once = "AT+GSD\r\n".encode('utf-8')
    ser.write(bytearray(get_data_once))
    init_f=[]
    fx_init = 0
    fy_init = 0
    fz_init = 0
    mx_init = 0
    my_init = 0
    mz_init = 0
    j = 0
    for i in range(10):
        ser.read(31)
        time.sleep(5e-2)
    for i in range(50):
        init_data = ser.read(31)
        if len(init_data) > 30:
            if 0xAA == init_data[0] and 0x55 == init_data[1]:
                fx_init = struct.unpack('f', init_data[6:10])[0] + fx_init
                fy_init = struct.unpack('f', init_data[10:14])[0] + fy_init
                fz_init = struct.unpack('f', init_data[14:18])[0] + fz_init
                mx_init = struct.unpack('f', init_data[18:22])[0] + mx_init
                my_init = struct.unpack('f', init_data[22:26])[0] + my_init
                mz_init = struct.unpack('f', init_data[26:30])[0] + mz_init
                j = j + 1
        time.sleep(5e-2)
    print("init")
    fx_init = fx_init / j
    fy_init = fy_init / j
    fz_init = fz_init / j
    mx_init = mx_init / j
    my_init = my_init / j
    mz_init = mz_init / j
    init_f[0:6] = fx_init, fy_init, fz_init, mx_init, my_init, mz_init
    return init_f

def main_force(init_f_m):
    print('begin')
    flag = 0
    start_time = time.time()
    duration_time = 60000   #  设置采集时间，单位s
    F_memmap = np.memmap('/home/yuxuan/Project/Pros_Ctrl/sensor_ws/src/pros_multisensor/scripts/six_force_data.npy', 
                         dtype='float32', mode='w+', shape=(6,))
    fff = np.zeros(6)
    count = 0
    try:
    # while time.time() < start_time + duration_time:
        while True:
            data = ser.read(31)
            if data[0:4] == bytearray([0xAA, 0x55, 0x00, 0x1B]) and len(data)==31:
                f_data = np.frombuffer(data[6:30], dtype=np.dtype('<f4'))
                fx = f_data[0]-init_f_m[0]
                fy = f_data[1]-init_f_m[1]
                fz = f_data[2]-init_f_m[2]
                mx = my = mz = 0
                fff[0:6] = fx, fy, fz, mx, my, mz
                print("\r Fz = "+format(fz, ">6.2f"),end='')
                F_memmap[:] = fff
            else:
                print("Fail")
    except KeyboardInterrupt:
        set_update_rate = "AT+GSD=STOP\r\n".encode('utf-8')
        ser.write(bytearray(set_update_rate))
        ser.close()

if __name__ == '__main__':

    init_ff = init_force()
    main_force(init_ff)
