import rospy
from std_msgs.msg import String
import tf2_ros
from tf2_geometry_msgs import PointStamped
import gatt
import sys
import numpy as np
import cv2
from scipy import io

if __name__ == "__main__":
    rospy.init_node("listener_pose")
    buffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(buffer)
    rate = rospy.Rate(100)

    imu_thigh_buffer = np.memmap("/home/yuxuan/Project/Pros_Ctrl/sensor_ws/src/pros_imu/scripts/imu_thigh.npy", dtype='float32', mode='r',
                           shape=(12,))
    
    imu_knee_buffer = np.memmap("/home/yuxuan/Project/Pros_Ctrl/sensor_ws/src/pros_imu/scripts/imu_knee.npy", dtype='float32', mode='r',
                           shape=(12,))
   
    imu_ankle_buffer = np.memmap("/home/yuxuan/Project/Pros_Ctrl/sensor_ws/src/pros_imu/scripts/imu_ankle.npy", dtype='float32', mode='r',
                           shape=(12,))
    
    imu_buffer = np.memmap("/home/yuxuan/Project/Pros_Ctrl/sensor_ws/src/pros_imu/scripts/imu_buffer.npy", dtype='float32', mode='r+',
                           shape=(28,))
    
    data_buffer = np.zeros((20,))
    img = np.zeros((300, 300), np.uint8)
    # 浅灰色背景
    img.fill(200)
    while not rospy.is_shutdown():
        try:
            data_temp = np.zeros((28,))
            data_temp[0] = rospy.get_time()
            # thigh:
            rospy.loginfo("Thigh Angle Data:x=%.2f, y=%.2f, z=%.2f",imu_thigh_buffer[6], imu_thigh_buffer[7], imu_thigh_buffer[8])
            for i in range(9):
                data_temp[i+1] = imu_thigh_buffer[i]
            #knee
            rospy.loginfo("Knee Angle Data:x=%.2f, y=%.2f, z=%.2f",imu_knee_buffer[6], imu_knee_buffer[7], imu_knee_buffer[8])
            for i in range(9):
                data_temp[i+10] = imu_knee_buffer[i]
            #ankle
            rospy.loginfo("Ankle Angle Data:x=%.2f, y=%.2f, z=%.2f",imu_ankle_buffer[6], imu_ankle_buffer[7], imu_ankle_buffer[8])
            for i in range(9):
                data_temp[i+19] = imu_ankle_buffer[i]
            for i in range(28):
                imu_buffer[i] = data_temp[i]
            
            imu_buffer.flush()
            cv2.imshow("Press q to stop imu", img)
            if cv2.waitKey(1) == ord('q'):
                # io.savemat("/media/yuxuan/SSD/Big_Rover_Data/imu_april_tag/data.mat", {"data": data_buffer})
                break
        except Exception as e:
            rospy.logerr("Exception:%s", e)
        rate.sleep()
