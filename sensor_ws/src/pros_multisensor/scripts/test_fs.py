import numpy as np
import rospy
from pros_multisensor.msg import Foot_Plate
import time
import os
import message_filters

class FS_Sub:
    def __init__(self,save_path,bag_idx) -> None:
        self.save_path = save_path
        self.bag_idx = bag_idx
        self.max_count = 10000
        self.force_list_r = []
        self.force_list_l = []
        self.file_count = 0
        self.ts = 0.012352941
        self.time = 0
        fs_sub_l = message_filters.Subscriber("fs_pub_left",Foot_Plate,queue_size=10)
        fs_sub_r = message_filters.Subscriber("fs_pub_right",Foot_Plate,queue_size=10)
        sync = message_filters.ApproximateTimeSynchronizer([fs_sub_l,fs_sub_r],queue_size=10,slop=1,allow_headerless=True)
        sync.registerCallback(self.callback)

    def callback(self,data_l:Foot_Plate,data_r:Foot_Plate):
        self.time += self.ts
        data_vec = np.array([self.time,data_l.F_area1,data_l.x_area1,data_l.y_area1,
                            data_l.F_area2,data_l.x_area2,data_l.y_area2,
                            data_l.F_area3,data_l.x_area3,data_l.y_area3,
                            data_l.F_net,data_l.x_net,data_l.y_net])
        self.force_list_l.append(data_vec)
        data_vec = np.array([self.time,data_r.F_area1,data_r.x_area1,data_r.y_area1,
                        data_r.F_area2,data_r.x_area2,data_r.y_area2,
                        data_r.F_area3,data_r.x_area3,data_r.y_area3,
                        data_r.F_net,data_r.x_net,data_r.y_net])
        self.force_list_r.append(data_vec)
        if len(self.force_list_l)==self.max_count:
            self.save_npy()
    
    def save_npy(self):
       
        print("save {} left".format(self.file_count))
        print("num {}".format(len(self.force_list_l)))
        np.save(self.save_path+"data{}/{}_l.npy".format(self.bag_idx,int(self.file_count)),
                        np.array(self.force_list_l))
        print("save {} right".format(self.file_count))
        print("num {}".format(len(self.force_list_r)))
        np.save(self.save_path+"data{}/{}_r.npy".format(self.bag_idx,int(self.file_count)),
                        np.array(self.force_list_r))
        self.file_count += 1
        self.force_list_l = []
        self.force_list_r = []

if __name__ == "__main__":
    rospy.init_node("test_fs",anonymous=True)
    save_path = "/media/yuxuan/My Passport/testFootPlate/"  
    bag_idx = 5

    clear_ = input("Clear Current Npy?[Y/n]")
    if clear_=="Y":
        file_list = os.listdir(save_path+"data{}/".format(bag_idx))
        for f in file_list:
            os.remove(save_path+"data{}/".format(bag_idx)+f)
    
    fs_sub = FS_Sub(save_path=save_path,bag_idx=bag_idx)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rate.sleep()
    fs_sub.save_npy()
    