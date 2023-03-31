#include "ros/ros.h"
#include "std_msgs/String.h"
#include "serial_msg.hpp"
#include "time.h"

#include "boost/thread.hpp"

#include "lcm/lcm-cpp.hpp"
#include "msg_t.hpp"
#include "msg_r.hpp"
#include "lcm_.hpp"


#include "ros_ctrl/Motor.h"
#include "ros_ctrl/Kill.h"

#include "Serial.hpp"

static uint8_t txDataBuffer[200];
static uint8_t rxDataBuffer[14*5];
static uint8_t rxMsg[14];
static uint8_t txMsg[11];

static float k_float2int16 = 300;
static float b_float2int16 = 30000;
static float k_float2int12 = 22;
static float b_float2int12 = 2110;

MotorTypeDef motor_knee;
MotorTypeDef motor_ankle;

static uint16_t temp_16,temp1_16,temp2_16;
static uint8_t temp_8;

static uint32_t count;

lcm::LCM lc_t;
lcm::LCM lc_r;
mvp_t::msg_t lcm_mt;
mvp_r::msg_r lcm_mr;


static bool main_ok = true;
static bool stm32_ok = true;

boost::shared_mutex mutex;
boost::condition_variable_any cond; 

static int counter_stm32 = 0;
static int counter_main = 0;
static int counter_rx = 0;
static int counter_tx = 0;

void PublishLCM(mvp_r::msg_r mr){
    mr.knee_position_actual = motor_knee.pos_actual;
    mr.ankle_position_actual = motor_ankle.pos_actual;
    mr.knee_velocity_actual = motor_knee.vel_actual;
    mr.ankle_velocity_actual = motor_ankle.vel_actual;
    mr.knee_torque_actual = motor_knee.cur_actual;
    mr.ankle_torque_actual = motor_ankle.cur_actual;
    lc_r.publish("MIDDLE_TO_HIGH",&mr);
}

class SubscribeLCMHandler{
    public:
        SubscribeLCMHandler(){}
        ~SubscribeLCMHandler(){}
        void handleMessage(
            const lcm::ReceiveBuffer* rbuff,
            const std::string& chan,
            const mvp_t::msg_t* msg
        ){
            motor_knee.pos_desired = msg->knee_position_desired;
            motor_ankle.pos_desired = msg->ankle_position_desired;
            motor_knee.vel_desired = msg->knee_velocity_desired;
            motor_ankle.vel_desired = msg->ankle_velocity_desired;
            motor_knee.cur_desired = msg->knee_torque_desired;
            motor_knee.mode = msg->Mode;
            motor_ankle.mode = msg->Mode;
        }
};

bool KillCallback(ros_ctrl::KillRequest& req, ros_ctrl::KillResponse&){
    ROS_INFO_STREAM("退出控制");
    main_ok = false;
    stm32_ok = false;
    return true;
}



// void thread_stm32rx(serial::Serial& ser){
void thread_stm32rx(Serial& ser){
    volatile size_t byte_read;
    while(ros::ok()&&(stm32_ok)&&counter_stm32<10000){
        byte_read = ser.read(rxMsg,sizeof(rxMsg),100);
        //boost::unique_lock<boost::shared_mutex> lock(mutex);
        if(PC_UnpackMessages(rxMsg,&motor_knee,&motor_ankle)){
            ROS_INFO_STREAM("消息接收成功");
            counter_rx +=1;
        }else{
            ROS_ERROR("Receive Message Wrong");
        }
        counter_stm32 +=1;
        // cond.notify_all();
        // cond.wait(mutex);
        
    }
    return;
}


int main(int argc, char ** argv){
    setlocale(LC_ALL,"");
    ros::init(argc,argv,"main_control");
    ros::NodeHandle n;
    ros::Rate loop_rate(100);
    ROS_INFO_STREAM("节点初始完成");
    ros::ServiceServer server = n.advertiseService("Kill",KillCallback);
    ROS_INFO_STREAM("按q终止");
    
    Serial ser;
    if(ser.open("/dev/ttyUSB1",115200,8,Serial::PARITY_NONE,1)!=Serial::OK)
    {
        ROS_ERROR("无法开启串口\n");
        return -1;
    }
    ROS_INFO_STREAM("串口开启成功\n");

    if(!lc_r.good()||(!lc_r.good()))
        return 1;
    SubscribeLCMHandler handleObject;
    lc_t.subscribe("HIGH_TO_MIDDLE",&SubscribeLCMHandler::handleMessage,&handleObject);

    ros::Publisher pub1 = n.advertise<ros_ctrl::Motor>("motor_watcher1",100);
    ros::Publisher pub2 = n.advertise<ros_ctrl::Motor>("motor_watcher2",100);

    ros_ctrl::Motor knee_message_ros;
    ros_ctrl::Motor ankle_message_ros;

    motor_knee.pos_desired = 0;
    motor_ankle.pos_actual = 0;

    PC_PackMessages(CMD_POSITION_CTRL,txMsg,&motor_knee,&motor_ankle);
    ser.write(txMsg,sizeof(txMsg));

    

    boost::thread stm32_rx(thread_stm32rx,std::ref(ser));
    while(ros::ok()&&(main_ok)&&(counter_main<10000)){
        lc_t.handleTimeout(10);
        ros::spinOnce();
        loop_rate.sleep();
        boost::shared_lock<boost::shared_mutex> lock(mutex);
        // cond.wait(mutex);
        if(motor_knee.state==ReadyReading&&motor_ankle.state==ReadyReading)
            PC_PackMessages(CMD_POSITION_CTRL,txMsg,&motor_knee,&motor_ankle);
        // cond.notify_all();
        ser.write(txMsg,sizeof(txMsg));
        ROS_INFO_STREAM("消息发送成功");
        counter_tx += 1;
        UpdateWatcher(&knee_message_ros,&ankle_message_ros,
            &motor_knee, &motor_ankle);
        pub1.publish(knee_message_ros);
        pub2.publish(ankle_message_ros);
        PublishLCM(lcm_mr);

        ROS_INFO("Knee:P_des = %.3f,P_act = %.3f",
                knee_message_ros.pos_desired,knee_message_ros.pos_actual);
        ROS_INFO("Ankle:P_des = %.3f,P_act = %.3f",
                ankle_message_ros.pos_desired,ankle_message_ros.pos_actual);
        counter_main+=1;
    }
    ROS_INFO("Total Send Message %d",counter_tx);
    ROS_INFO("Total_Receive_Message %d",counter_rx);
    ros::shutdown();
    stm32_rx.join();

    return 0;
}