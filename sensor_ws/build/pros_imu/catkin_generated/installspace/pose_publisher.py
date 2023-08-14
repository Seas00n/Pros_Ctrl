import rospy
from std_msgs.msg import String
import tf2_ros
from tf2_geometry_msgs import PointStamped
import gatt
import sys
import numpy as np
import cv2
from scipy import io
from sensor_msgs.msg import Imu



open_memmap = sys.argv[1]
if open_memmap == "use_memmap":
    use_memmap = True

def publish_imu(imu_pub, imu_id ,imu_data):
    imu = Imu()
    imu.header.frame_id = imu_id
    imu.header.stamp = rospy.Time.now()
    imu.orientation.x = imu_data[9]
    imu.orientation.y = imu_data[10]
    imu.orientation.z = imu_data[11]
    imu.orientation.w = imu_data[12]
    imu.linear_acceleration.x = imu_data[0]
    imu.linear_acceleration.y = imu_data[1]
    imu.linear_acceleration.z = imu_data[2]
    imu.angular_velocity.x = imu_data[3]
    imu.angular_velocity.y = imu_data[4]
    imu.angular_velocity.z = imu_data[5]
    imu_pub.publish(imu)
    


if __name__ == "__main__":
    rospy.init_node("pose_publisher", anonymous=True)
    
    imu_thigh_pub = rospy.Publisher("imu_thigh_pub",Imu, queue_size = 10)
    imu_knee_pub = rospy.Publisher("imu_knee_pub",Imu, queue_size = 10)
    imu_ankle_pub = rospy.Publisher("imu_ankle_pub",Imu, queue_size = 10)




    rate = rospy.Rate(100)

    imu_thigh_buffer = np.memmap("/home/yuxuan/Project/Pros_Ctrl/sensor_ws/src/pros_imu/scripts/imu_thigh.npy", dtype='float32', mode='r',
                           shape=(13,))
    
    imu_knee_buffer = np.memmap("/home/yuxuan/Project/Pros_Ctrl/sensor_ws/src/pros_imu/scripts/imu_knee.npy", dtype='float32', mode='r',
                           shape=(13,))
   
    imu_ankle_buffer = np.memmap("/home/yuxuan/Project/Pros_Ctrl/sensor_ws/src/pros_imu/scripts/imu_ankle.npy", dtype='float32', mode='r',
                           shape=(13,))
    
    imu_buffer = np.memmap("/home/yuxuan/Project/Pros_Ctrl/sensor_ws/src/buffer/imu_buffer.npy", dtype='float32', mode='r+',
                            shape=(28,))
    
    img = np.zeros((300, 300), np.uint8)
    # 浅灰色背景
    img.fill(200)






    while not rospy.is_shutdown():
        try:
            # thigh:
            rospy.loginfo("Thigh Angle Data:x=%.2f, y=%.2f, z=%.2f",imu_thigh_buffer[6], imu_thigh_buffer[7], imu_thigh_buffer[8])
            imu_thigh_data = np.copy(imu_thigh_buffer[0:])
            publish_imu(imu_thigh_pub, "imu_thigh", imu_data = imu_thigh_data)
            # knee:
            rospy.loginfo("Knee Angle Data:x=%.2f, y=%.2f, z=%.2f",imu_knee_buffer[6], imu_knee_buffer[7], imu_thigh_buffer[8])
            imu_knee_data = np.copy(imu_knee_buffer[0:])
            publish_imu(imu_knee_pub, "imu_knee", imu_data = imu_knee_data)
            # ankle:
            rospy.loginfo("Ankle Angle Data:x=%.2f, y=%.2f, z=%.2f",imu_ankle_buffer[6], imu_ankle_buffer[7], imu_thigh_buffer[8])
            imu_ankle_data = np.copy(imu_ankle_buffer[0:])
            publish_imu(imu_ankle_pub, "imu_ankle", imu_data = imu_ankle_data)
            if use_memmap:
                imu_buffer[0] = rospy.Time.now()
                imu_buffer[1:10] = imu_thigh_data[0:9]
                imu_buffer[10:19] = imu_knee_data[0:9]
                imu_buffer[19:28] = imu_ankle_data[0:9]
                imu_buffer.flush()
            cv2.imshow("Press q to stop imu", img)
            if cv2.waitKey(1) == ord('q'):
                break
        except Exception as e:
            rospy.logerr("Exception:%s", e)
        rate.sleep()
