import serial
import numpy as np
import rospy
from pros_multisensor.msg import Foot_Plate
import time

k_int2float = 10.0
b_int2float = 30000.0


def analyse_read_data(data_read):
    force_data = np.zeros((9,))
    if data_read[0]==int(0xAA):
        for i in range(9):
            force_data[i] = data_read[2*(i-1)+4]*256 + data_read[2*(i-1)+3]
            force_data[i] = (force_data[i]-b_int2float)/k_int2float
    return force_data



if __name__ == "__main__":
    try:
        ser = serial.Serial(
            port = "/dev/ttyUSB2",
            baudrate=115200,
            timeout=0.01
        )
        if ser.is_open:
            print("\033[32m [LOG]Serial is open\033[0m")
        else:
            print("\033[31m [ERROR]Serial not Open \033[0m")    
    except Exception as e:
        print("\033[31m [ERROR]Serial not Open | {}\033[0m".format(e))

    num_read_bytes = 19


    msg_pub = Foot_Plate()
    rospy.init_node("fs_publisher_left")
    pub = rospy.Publisher("fs_pub_left", Foot_Plate, queue_size=10)
    rate = rospy.Rate(20) 
    time.sleep(2)

    force_msg = np.zeros((9,))

    while not rospy.is_shutdown():
        bytes_read = ser.read(size=num_read_bytes)
        bytes_read = np.frombuffer(bytes_read, dtype=np.uint8)
        if np.shape(bytes_read)[0] == num_read_bytes:
            force_msg = analyse_read_data(bytes_read)
        msg_pub.F_area1 = force_msg[0]*100/1000*9.8
        msg_pub.x_area1 = force_msg[1]*0.01
        msg_pub.y_area1 = force_msg[2]*0.01
        msg_pub.F_area2 = force_msg[3]*100/1000*9.8
        msg_pub.x_area2 = force_msg[4]*0.01
        msg_pub.y_area2 = force_msg[5]*0.01
        msg_pub.F_area3 = force_msg[6]*100/1000*9.8
        msg_pub.x_area3 = force_msg[7]*0.01
        msg_pub.y_area3 = force_msg[8]*0.01
        msg_pub.F_net = msg_pub.F_area1+msg_pub.F_area2+msg_pub.F_area3
        if msg_pub.F_net < 100:
            msg_pub.F_net = 0
            msg_pub.x_net = 0
            msg_pub.y_net = 0
            msg_pub.contact = 0
        else:
            msg_pub.x_net = (msg_pub.F_area1*msg_pub.x_area1+
                             msg_pub.F_area2*msg_pub.x_area2+
                             msg_pub.F_area3*msg_pub.x_area3)/msg_pub.F_net
            msg_pub.y_net = (msg_pub.F_area1*msg_pub.y_area1+
                             msg_pub.F_area2*msg_pub.y_area2+
                             msg_pub.F_area3*msg_pub.y_area3)/msg_pub.F_net
            msg_pub.contact = 1
        pub.publish(msg_pub)
        rospy.loginfo("F1=%.3f,x1=%.3f,y1=%.3f,F2=%.3f,x2=%.3f,y2=%.3f,F3=%.3f,x3=%.3f,y3=%.3f,F=%.3f",
                      force_msg[0],force_msg[1],force_msg[2],
                      force_msg[3],force_msg[4],force_msg[5],
                      force_msg[6],force_msg[7],force_msg[8],
                      msg_pub.F_net)
    ser.close()