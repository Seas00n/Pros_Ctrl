#include <mutex>
#include <thread>
#include "ros/ros.h"
#include "serial/Serial.hpp"
#include "ros_ctrl/pros_hw.hpp"
#include "ros_ctrl/lcm_.hpp"
static bool main_ok = true;
static bool stm32_ok = true;

static uint8_t rxMsg[18];
static uint8_t txMsg[15];


void thread_stm32rx(Serial& ser, ProsHardwareInterface& pros_hw){
    volatile size_t byte_read;
    while (ros::ok()&&(stm32_ok)){
        byte_read = ser.read(rxMsg, sizeof(rxMsg), 100);
        pros_hw.UnpackMsgNormal(rxMsg);
    }
}

int main(int argc, char** argv){
    ros::init(argc, argv, "main_control");
    ros::NodeHandle n;
    ros::Rate loop_rate(1000);
    ROS_INFO_STREAM("节点初始完成");
    
    Serial ser;
    if (ser.open("/dev/ttyUSB0", 115200, 8, Serial::PARITY_NONE, 1) != Serial::OK)
    {
        ROS_ERROR("无法开启串口\n");
        return -1;
    }
    ROS_INFO_STREAM("串口开启成功\n");
    
    ros::Publisher pub1 = n.advertise<ros_ctrl::Motor>("motor_watcher1", 100);
    ros::Publisher pub2 = n.advertise<ros_ctrl::Motor>("motor_watcher2", 100);
    ros_ctrl::Motor knee_message_ros;
    ros_ctrl::Motor ankle_message_ros;

    ProsHardwareInterface pros_hw;
    LCMProsInterface lcm = LCMProsInterface(std::ref(pros_hw));
    pros_hw.PackMessagesNormal(CMD_POSITION_CTRL, txMsg);
    ser.write(txMsg, sizeof(txMsg));
    std::thread stm32_rx(thread_stm32rx, std::ref(ser), std::ref(pros_hw));

    while ((ros::ok()&&(main_ok))){
        ros::spinOnce();
        loop_rate.sleep();
        pros_hw.PackMessagesNormal(CMD_VELOCITY_CTRL, txMsg);
        ser.write(txMsg, sizeof(txMsg));
        pros_hw.ROSUpdateMsg(&knee_message_ros,&ankle_message_ros);
        pub1.publish(knee_message_ros);
        pub2.publish(ankle_message_ros);
        lcm.PublishLCM();
    }
    // ROS_INFO("Total Send Message %d", counter_tx);
    // ROS_INFO("Total_Receive_Message %d", counter_rx);
    ros::shutdown();
    stm32_rx.join();
    return 0;
}