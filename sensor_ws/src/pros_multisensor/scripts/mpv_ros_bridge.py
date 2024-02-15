import rospy
import message_filters
from sensor_msgs.msg import Imu, PointCloud2

import numpy as np
from scipy.spatial.transform import Rotation as R


import sys
sys.path.append("/home/yuxuan/Project/Pros_Ctrl/sensor_ws/src/pros_multisensor/scripts/")
# print(sys.path)


import lcm
from pcd_lcm.pcd_xyz import *

down_sample_rate = 5
if down_sample_rate % 2 == 1:
    num_points = int(38528/down_sample_rate)+1
    if num_points > 38528:
        num_points = 38528
else:
    num_points = int(38528/down_sample_rate)

path_to_imu_thigh = "/home/yuxuan/Project/MPV_2024/Sensor/IM948/imu_thigh.npy"
path_to_imu_knee = "/home/yuxuan/Project/MPV_2024/Sensor/IM948/imu_knee.npy"
path_to_imu_ankle = "/home/yuxuan/Project/MPV_2024/Sensor/IM948/imu_ankle.npy"
path_to_pcd_buffer = "/home/yuxuan/Project/MPV_2024/Sensor/RoyaleSDK/pcd_buffer.npy"

imu_thigh_buffer = np.memmap(path_to_imu_thigh, dtype='float32', mode='r+', shape=(14,))
imu_knee_buffer = np.memmap(path_to_imu_knee, dtype='float32', mode='r+', shape=(14,))
imu_ankle_buffer = np.memmap(path_to_imu_ankle, dtype='float32', mode='r+', shape=(14,))
pcd_data_buffer = np.memmap(path_to_pcd_buffer, dtype="float32", mode='r+',shape=(num_points,3))



pcd_lc = lcm.LCM()
pcd_msg = pcd_xyz()







def pcd_callback(data:PointCloud2):
    pcd_data = np.frombuffer(data.data, dtype=np.float32).reshape((-1,3))
    # pcd = (pcd_data*300+10000).astype(np.int16)
    # pcd_msg.pcd_x = list(pcd[:,0])
    # pcd_msg.pcd_y = list(pcd[:,1])
    # pcd_msg.pcd_z = list(pcd[:,2])
    # pcd_lc.publish("PCD_DATA",pcd_msg.encode())
    
    pcd_data_buffer[:,0] = pcd_data[:,0]
    pcd_data_buffer[:,1] = pcd_data[:,1]
    pcd_data_buffer[:,2] = pcd_data[:,2]
    pcd_data_buffer.flush()



def imu_thigh_callback(data:Imu):
    t = data.header.stamp.to_sec()
    t = t - int(t/100000)*100000
    imu_thigh_buffer[0] = t
    imu_thigh_buffer[0] = data.header.stamp.to_sec()
    imu_thigh_buffer[1] = data.linear_acceleration.x
    imu_thigh_buffer[2] = data.linear_acceleration.y
    imu_thigh_buffer[3] = data.linear_acceleration.z
    imu_thigh_buffer[4] = data.angular_velocity.x
    imu_thigh_buffer[5] = data.angular_velocity.y
    imu_thigh_buffer[6] = data.angular_velocity.z
    r = R.from_quat([data.orientation.x, data.orientation.y, data.orientation.z, data.orientation.w])
    eular = r.as_euler("xyz",degrees=True)
    imu_thigh_buffer[7] = eular[0]
    imu_thigh_buffer[8] = eular[1]
    imu_thigh_buffer[9] = eular[2]
    imu_thigh_buffer[10] = data.orientation.w
    imu_thigh_buffer[11] = data.orientation.x
    imu_thigh_buffer[12] = data.orientation.y
    imu_thigh_buffer[13] = data.orientation.z
    imu_thigh_buffer.flush()
    # print("Thigh Roll:{}, Pitch:{}, Yaw:{}".format(eular[0], eular[1], eular[2]))

def imu_knee_callback(data:Imu):
    t = data.header.stamp.to_sec()
    t = t - int(t/100000)*100000
    imu_knee_buffer[0] = t
    imu_knee_buffer[1] = data.linear_acceleration.x
    imu_knee_buffer[2] = data.linear_acceleration.y
    imu_knee_buffer[3] = data.linear_acceleration.z
    imu_knee_buffer[4] = data.angular_velocity.x
    imu_knee_buffer[5] = data.angular_velocity.y
    imu_knee_buffer[6] = data.angular_velocity.z
    r = R.from_quat([data.orientation.x, data.orientation.y, data.orientation.z,data.orientation.w])
    eular = r.as_euler("xyz",degrees=True)
    imu_knee_buffer[7] = eular[0]
    imu_knee_buffer[8] = eular[1]
    imu_knee_buffer[9] = eular[2]
    imu_knee_buffer[10] = data.orientation.w
    imu_knee_buffer[11] = data.orientation.x
    imu_knee_buffer[12] = data.orientation.y
    imu_knee_buffer[13] = data.orientation.z
    imu_knee_buffer.flush()
    print("Time:{},Knee Roll:{}, Pitch:{}, Yaw:{}".format(
        data.header.stamp.to_sec(),
        eular[0], eular[1], eular[2]))

def imu_ankle_callback(data:Imu):
    t = data.header.stamp.to_sec()
    t = t - int(t/100000)*100000
    imu_ankle_buffer[0] = t
    imu_ankle_buffer[1] = data.linear_acceleration.x
    imu_ankle_buffer[2] = data.linear_acceleration.y
    imu_ankle_buffer[3] = data.linear_acceleration.z
    mag_acc = np.sqrt(data.linear_acceleration.x**2+data.linear_acceleration.y**2+data.linear_acceleration.z**2)
    imu_ankle_buffer[4] = data.angular_velocity.x
    imu_ankle_buffer[5] = data.angular_velocity.y
    imu_ankle_buffer[6] = data.angular_velocity.z
    r = R.from_quat([data.orientation.x, data.orientation.y, data.orientation.z, data.orientation.w])
    eular = r.as_euler("xyz",degrees=True)
    imu_ankle_buffer[7] = eular[0]
    imu_ankle_buffer[8] = eular[1]
    imu_ankle_buffer[9] = eular[2]
    imu_ankle_buffer[10] = data.orientation.w
    imu_ankle_buffer[11] = data.orientation.x
    imu_ankle_buffer[12] = data.orientation.y
    imu_ankle_buffer[13] = data.orientation.z
    imu_ankle_buffer.flush()
    print("Time:{} Ankle Roll:{}, Pitch:{}, Yaw:{} Accel:{}".format(t, eular[0], eular[1], eular[2], mag_acc))

def pcd_imu_multicallback(Sub_Pcd:PointCloud2, Sub_Imu:Imu):
    pcd_callback(Sub_Pcd)
    imu_knee_callback(Sub_Imu)

def shut_down_bridge():
     print("shutdown time!")

if __name__ =="__main__":
    rospy.init_node("mpv_ros_bridge",anonymous=True)
    # rospy.Subscriber("imu_thigh_pub",Imu, callback=imu_thigh_callback)
    rospy.Subscriber("imu_knee_pub",Imu, callback=imu_knee_callback)
    rospy.Subscriber("imu_ankle_pub",Imu, callback=imu_ankle_callback)
    rospy.Subscriber("pcd_pub",PointCloud2, callback=pcd_callback)
    
    
    # 实现PCD和IMU的数据同步
    # subscriber_pcd = message_filters.Subscriber("pcd_pub", PointCloud2, queue_size=1)
    # subscriber_imu_knee = message_filters.Subscriber("imu_knee_pub", Imu, queue_size=1)
    # sync = message_filters.ApproximateTimeSynchronizer([subscriber_pcd,subscriber_imu_knee],queue_size=1, slop=1, allow_headerless=True)
    # sync.registerCallback(pcd_imu_multicallback)
    
    rospy.spin()