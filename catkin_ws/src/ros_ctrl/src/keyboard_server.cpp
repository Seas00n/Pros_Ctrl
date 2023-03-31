#include "ros/ros.h"
#include "ros_ctrl/Kill.h"
static bool main_ok = true;
static int count_main = 0;
bool doReq(ros_ctrl::KillRequest& req,
ros_ctrl::KillResponse& res){
    main_ok = false;
    return main_ok;
}
int main(int argc, char *argv[]){
    setlocale(LC_ALL,"");
    ros::init(argc, argv, "Kill_Test");
    ros::NodeHandle nh;
    ros::ServiceServer server = nh.advertiseService("Kill",doReq);
    ros::Rate loop_rate(20);
    while(ros::ok&&count_main<1000){
        count_main +=1;
        if(!main_ok){
            return 1;
        }
        ros::spinOnce();
        loop_rate.sleep();
        ROS_INFO_STREAM("CONTINUE");
    }
    return 0;
}
