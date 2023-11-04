#!/usr/bin/python3
import sys
sys.path.append("/home/yuxuan/Project/Pros_Ctrl/sensor_ws/src/pros_pcd/scripts/")
print(sys.path)

import argparse
import roypy  # local installation
import time
import queue
from sample_camera_info import print_camera_info
from roypy_sample_utils import CameraOpener, add_camera_opener_options, select_use_case
from roypy_platform_utils import PlatformHelper
import matplotlib.pyplot as plt

import numpy as np
import open3d as o3d
from scipy.spatial.transform import Rotation as R

import rospy
from std_msgs.msg import Header
from sensor_msgs.msg import Image, PointCloud2, Imu
import sensor_msgs.point_cloud2 as pcl2 



count = 0

down_sample_rate = 20
if down_sample_rate % 2 == 1:
    num_points = int(38528/down_sample_rate)+1
    if num_points > 38528:
        num_points = 38528
else:
    num_points = int(38528/down_sample_rate)


        
def publish_pcd(pcd_pub, pcd):
    global count
    header = Header()
    header.stamp = rospy.Time.now()
    header.frame_id = "oak_right_camera_optical_frame"
    pcd = pcd[0:-1:down_sample_rate,:]
    R_camera = R.from_euler('xyz',[0,0,90],degrees=True).as_matrix()
    R_calib = R.from_euler('xyz',[0,0,0],degrees=True).as_matrix()
    pcd = np.matmul(R_camera@R_calib,pcd.T).T
    pcd_pub.publish(pcl2.create_cloud_xyz32(header, pcd))
    rospy.loginfo("PCD_Data size[%d x 3]",np.shape(pcd[:,0])[0])



class MyListener(roypy.IDepthDataListener):
    def __init__(self, q):
        super(MyListener, self).__init__()
        self.queue = q
        self.figSetup = False
        self.firstTime = True

    def onNewData(self, data):
        pc = data.npoints ()
        
        #only select the three columns we're interested in
        px = pc[:,:,0]
        py = pc[:,:,1]
        pz = pc[:,:,2]
        stack1 = np.stack([px,py,pz], axis=-1)
        stack2 = stack1.reshape(-1, 3)
        
        self.queue.put(stack2)

    def paint (self, data):
        """Called in the main thread, with data containing one of the items that was added to the
        queue in onNewData.
        """
        depth = data[:,2].reshape((172,224))
        if not self.figSetup:
            self.fig = plt.figure(1)
            self.im = plt.imshow(depth)
            plt.show(block=False)
            plt.draw()
            self.figSetup = True
        else:
            self.im.set_data(depth)
            self.fig.canvas.draw()




def main ():
    rospy.init_node("hps_pcd", anonymous=True)
    pcd_pub = rospy.Publisher("pcd_pub",PointCloud2, queue_size=10)


    platformhelper = PlatformHelper()
    parser = argparse.ArgumentParser (usage = __doc__)
    add_camera_opener_options (parser)
    parser.add_argument ("--seconds", type=int, default=600, help="duration to capture data")
    options = parser.parse_args()
    opener = CameraOpener (options)
    cam = opener.open_camera ()

    print_camera_info (cam)
    print("isConnected", cam.isConnected())
    print("getFrameRate", cam.getFrameRate())

    # curUseCase = select_use_case(cam)
    use_cases = cam.getUseCases()
    curUseCase = use_cases[3]

    try:
        # retrieve the interface that is available for recordings
        replay = cam.asReplay()
        print ("Using a recording")
        print ("Framecount : ", replay.frameCount())
        print ("File version : ", replay.getFileVersion())
    except SystemError:
        print ("Using a live camera")
    
    # we will use this queue to synchronize the callback with the main
    # thread, as drawing should happen in the main thread
    q = queue.Queue()
    l = MyListener(q)
    cam.registerDataListener(l)

    print ("Setting use case : " + curUseCase)
    cam.setUseCase(curUseCase)

    cam.startCapture()
    # create a loop that will run for a time (default 15 seconds)
    # process_event_queue (q, l, options.seconds)
    t_end = time.time() + options.seconds

    rate = rospy.Rate(10)
    while not rospy.is_shutdown() and time.time() < t_end:
        try:
            # try to retrieve an item from the queue.
            # this will block until an item can be retrieved
            # or the timeout of 1 second is hit
            if len(q.queue) == 0:
                item = q.get(True, 1)
            else:
                for i in range (0, len (q.queue)):
                    item = q.get(True, 1)
        except queue.Empty:
            # this will be thrown when the timeout is hit
            break
        else:
            # l.paint(item)
            publish_pcd(pcd_pub=pcd_pub, pcd=item)
            rate.sleep()
    cam.stopCapture()

if (__name__ == "__main__"):
    main()
