#include "ros/ros.h"
#include "std_msgs/String.h"
#include "boost/thread.hpp"
#include "serial/serial.h"
#include "lcm/lcm-cpp.hpp"
#include "serial_msg.hpp"
#include "ringBuffer.hpp"
#include "ros_ctrl/Motor.h"
#include "msg_t.hpp"
#include "msg_r.hpp"
#include "lcm_.hpp"
#include "time.h"
#include "unistd.h"

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

static ringBuffer_t ringBuffer; 



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


void thread_stm32rx(void){
    
}


int main(int argc, char ** argv){
    printf("Hello,World/n");
    
    return 0;
}