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
import time
from scipy.spatial.transform import Rotation as R


open_memmap = sys.argv[1]
if open_memmap == "use_memmap":
    use_memmap = True

path_to_imu_thigh = "/home/yuxuan/Project/MPV_2024/Sensor/IM948/imu_thigh.npy"
path_to_imu_knee = "/home/yuxuan/Project/MPV_2024/Sensor/IM948/imu_knee.npy"
path_to_imu_ankle = "/home/yuxuan/Project/MPV_2024/Sensor/IM948/imu_ankle.npy"

imu_thigh_buffer = np.memmap(path_to_imu_thigh, dtype='float32', mode='r+', shape=(14,))
imu_knee_buffer = np.memmap(path_to_imu_knee, dtype='float32', mode='r+', shape=(14,))
imu_ankle_buffer = np.memmap(path_to_imu_ankle, dtype='float32', mode='r+', shape=(14,))

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
    r = R.from_quat([data.orientation.w, data.orientation.x, data.orientation.y, data.orientation.z])
    eular = r.as_euler("xyz",degrees=True)
    imu_thigh_buffer[7] = eular[0]
    imu_thigh_buffer[8] = eular[1]
    imu_thigh_buffer[9] = eular[2]
    imu_thigh_buffer[10] = data.orientation.w
    imu_thigh_buffer[11] = data.orientation.x
    imu_thigh_buffer[12] = data.orientation.y
    imu_thigh_buffer[13] = data.orientation.z
    imu_thigh_buffer.flush()

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
    


def publish_imu(imu_pub, imu_id ,imu_data):
    imu = Imu()
    imu.header.frame_id = "map"
    imu.header.stamp = rospy.Time.now()
    imu.linear_acceleration.x = imu_data[0]
    imu.linear_acceleration.y = imu_data[1]
    imu.linear_acceleration.z = imu_data[2]
    imu.angular_velocity.x = imu_data[3]
    imu.angular_velocity.y = imu_data[4]
    imu.angular_velocity.z = imu_data[5]
    imu.orientation.x = imu_data[9]
    imu.orientation.y = imu_data[10]
    imu.orientation.z = imu_data[11]
    imu.orientation.w = imu_data[12]
    if use_memmap:
        return imu
    else:
        imu_pub.publish(imu)
        return imu





if __name__ == "__main__":
    rospy.init_node("pose_publisher", anonymous=True)
    
    imu_thigh_pub = rospy.Publisher("imu_thigh_pub",Imu, queue_size = 10)
    imu_knee_pub = rospy.Publisher("imu_knee_pub",Imu, queue_size = 10)
    imu_ankle_pub = rospy.Publisher("imu_ankle_pub",Imu, queue_size = 10)

    rate = rospy.Rate(100)

    imu_thigh_bf = np.memmap("/home/yuxuan/Project/Pros_Ctrl/sensor_ws/src/pros_imu/scripts/imu_thigh.npy", dtype='float32', mode='r',
                           shape=(13,))
    
    imu_knee_bf = np.memmap("/home/yuxuan/Project/Pros_Ctrl/sensor_ws/src/pros_imu/scripts/imu_knee.npy", dtype='float32', mode='r',
                           shape=(13,))
   
    imu_ankle_bf = np.memmap("/home/yuxuan/Project/Pros_Ctrl/sensor_ws/src/pros_imu/scripts/imu_ankle.npy", dtype='float32', mode='r',
                           shape=(13,))
    
    
    
    img = np.zeros((300, 300), np.uint8)
    # 浅灰色背景
    img.fill(200)

    t0 = time.time()

    while not rospy.is_shutdown():
        try:
            # thigh:
            imu_thigh_data = np.copy(imu_thigh_bf[0:])
            imu_thigh = publish_imu(imu_thigh_pub, "imu_thigh", imu_data = imu_thigh_data)
            # knee:
            imu_knee_data = np.copy(imu_knee_bf[0:])
            imu_knee = publish_imu(imu_knee_pub, "imu_knee", imu_data = imu_knee_data)
            # ankle:
            imu_ankle_data = np.copy(imu_ankle_bf[0:])
            imu_ankle = publish_imu(imu_ankle_pub, "imu_ankle", imu_data = imu_ankle_data)

            rospy.loginfo("Thigh:x=%.2f, y=%.2f, z=%.2f;Knee:x=%.2f, y=%.2f, z=%.2f;Ankle:x=%.2f, y=%.2f, z=%.2f",
                            imu_thigh_bf[6], imu_thigh_bf[7], imu_thigh_bf[8],
                            imu_knee_bf[6], imu_knee_bf[7], imu_knee_bf[8],
                            imu_ankle_bf[6], imu_ankle_bf[7], imu_ankle_bf[8])

            if use_memmap:
                imu_thigh_callback(imu_thigh)
                imu_knee_callback(imu_knee)
                imu_ankle_callback(imu_ankle)


            cv2.imshow("Press q to stop imu", img)
            if cv2.waitKey(1) == ord('q'):
                break
        except Exception as e:
            rospy.logerr("Exception:%s", e)
            break
        time.sleep(0.005)
