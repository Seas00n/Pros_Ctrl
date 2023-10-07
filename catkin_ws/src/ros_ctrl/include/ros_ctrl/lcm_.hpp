#pragma once
#include <memory>
#include "lcm/lcm-cpp.hpp"
#include "ros_ctrl/msg_r.hpp"
#include "ros_ctrl/msg_t.hpp"
#include "ros_ctrl/pros_hw.hpp"

class SubscribeLCMHandler
{
public:
    SubscribeLCMHandler(MotorTypeDef& mk, MotorTypeDef& ma) {
        motor_knee = &mk;
        motor_ankle = &ma;
    }
    ~SubscribeLCMHandler() {}
    void handleMessage(
        const lcm::ReceiveBuffer *rbuff,
        const std::string &chan,
        const mvp_t::msg_t *msg)
    {
        motor_knee->pos_desired = msg->knee_position_desired;
        motor_ankle->pos_desired = msg->ankle_position_desired;
        motor_knee->vel_desired = msg->knee_velocity_desired;
        motor_ankle->vel_desired = msg->ankle_velocity_desired;
        motor_knee->cur_desired = msg->knee_torque_desired;
        motor_knee->mode = msg->Mode;
        motor_ankle->mode = msg->Mode;
    }
private:
    MotorTypeDef * motor_knee;
    MotorTypeDef * motor_ankle;
};

class LCMProsInterface final{
    public:
        LCMProsInterface(ProsHardwareInterface& pros_hw){
            pros_hw_ = &(pros_hw);
            SubscribeLCMHandler handleObject = SubscribeLCMHandler(pros_hw.motor_knee, pros_hw.motor_ankle);
            lc_t.subscribe("HIGH_TO_MIDDLE",&SubscribeLCMHandler::handleMessage,&handleObject);
        }
        void PublishLCM(void)
        {
            mr.knee_position_actual = pros_hw_->motor_knee.pos_actual;
            mr.ankle_position_actual = pros_hw_->motor_ankle.pos_actual;
            mr.knee_velocity_actual = pros_hw_->motor_knee.vel_actual;
            mr.ankle_velocity_actual = pros_hw_->motor_ankle.vel_actual;
            mr.knee_torque_actual = pros_hw_->motor_knee.cur_actual;
            mr.ankle_torque_actual = pros_hw_->motor_ankle.cur_actual;
            lc_r.publish("MIDDLE_TO_HIGH", &mr);
            lc_t.handleTimeout(1);
        }
    private:
        mvp_t::msg_t mt;
        mvp_r::msg_r mr;
        lcm::LCM lc_t;
        lcm::LCM lc_r;
        ProsHardwareInterface* pros_hw_;
};
