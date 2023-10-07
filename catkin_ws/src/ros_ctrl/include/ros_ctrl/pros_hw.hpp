#pragma once

#include <mutex>
#include "stdint.h"
#include "ros_ctrl/Motor.h"

typedef struct
{
    uint16_t device_id;
    float pos_actual;
    float vel_actual;
    float cur_actual;
    float pos_desired;
    float vel_desired;
    float cur_desired;
    float Kp;
    float Kb;
    float Angle_eq;
    float temperature;
    uint8_t state;
    uint8_t mode;
} MotorTypeDef;
typedef enum
{
    CMD_POSITION_CTRL = 0,
    CMD_VELOCITY_CTRL = 1,
    CMD_TORQUE_CTRL = 2,
    CMD_POSITION_AND_VELOCITY = 3,
    CMD_IMPEDANCE = 4,
    CMD_QUICK_STOP = 5
} CMD_PACKET_ID;
typedef enum
{
    ReadyReading = 0,
    BusyWriting = 1
} Motor_Serial_State;



class ProsHardwareInterface final{
    public:
        MotorTypeDef motor_knee;
        MotorTypeDef motor_ankle;
        ProsHardwareInterface(void){
            motor_knee.pos_desired = 0;
            motor_ankle.pos_desired = 0;
        }
        ~ProsHardwareInterface(){}
        void msg2msg16(int id_8_0, uint8_t rxMsg[])
        {
            int id_16 = 0;
            for (id_16 = 0; id_16 < sizeof(rxMsg16Normal) / 2; id_16++)
            {
                rxMsg16Normal[id_16] = (rxMsg[id_8_0 + id_16 * 2] << 8) | (rxMsg[id_8_0 + id_16 * 2 + 1]);
            }
        }
        void msg162msg(int id_8_0, uint8_t txMsg[])
        {
            int id_16 = 0;
            for (id_16 = 0; id_16 < sizeof(txMsg16Normal) / 2; id_16++)
            {
                txMsg[id_8_0 + id_16 * 2] = (uint8_t)(txMsg16Normal[id_16] >> 8);
                txMsg[id_8_0 + id_16 * 2 + 1] = (uint8_t)(txMsg16Normal[id_16] & 0xff);
            }
        }
        int UnpackMsgNormal(uint8_t rxMsg[]){
            std::lock_guard<std::mutex> lock(latestObservationMutex_);
            if (rxMsg[0] == 0xFC && rxMsg[17] == 0xFF)
            {   
                uint16_t temp;
                motor_knee.state = BusyWriting;
                motor_ankle.state = BusyWriting;
                msg2msg16(1, rxMsg);
                temp = rxMsg16Normal[0];
                motor_knee.pos_actual = (float)(temp - b_float2int16) / k_float2int16;
                temp = rxMsg16Normal[1];
                motor_knee.vel_actual = (float)(temp - b_float2int16) / k_float2int16;
                temp = rxMsg16Normal[2];
                motor_ankle.pos_actual = (float)(temp - b_float2int16) / k_float2int16;
                temp = rxMsg16Normal[3];
                motor_ankle.vel_actual = (float)(temp - b_float2int16) / k_float2int16;
                temp = rxMsg16Normal[4];
                motor_knee.cur_actual = (float)(temp - b_float2int16) / k_float2int16;
                temp = rxMsg16Normal[5];
                motor_ankle.cur_actual = (float)(temp - b_float2int16) / k_float2int16;
                temp = rxMsg16Normal[6];
                motor_knee.temperature = (float)(temp - b_float2int16) / k_float2int16;
                temp = rxMsg16Normal[7];
                motor_ankle.temperature = (float)(temp - b_float2int16) / k_float2int16;
                motor_knee.state = ReadyReading;
                motor_ankle.state = ReadyReading;
                return 1;
            }
            else
            {
                return 0;
            }
            return 0;
        }
        void PackMessagesNormal(CMD_PACKET_ID cmd_id, uint8_t txMsg[])
        {
            std::lock_guard<std::mutex> lock(latestObservationMutex_);
            if (cmd_id == CMD_QUICK_STOP)
            {
                for (int i = 0; i < 6; i++)
                {
                    txMsg16Normal[i] = 0;
                }
                msg162msg(2, txMsg);
                txMsg[0] = 0xfc;
                txMsg[1] = (uint8_t)((cmd_id & 0xf) << 4);
                txMsg[14] = (uint8_t)(0xf);
            }
            else if (cmd_id == CMD_POSITION_CTRL)
            {
                txMsg16Normal[0] = (uint16_t)(k_float2int16 * motor_knee.pos_desired + b_float2int16);
                txMsg16Normal[1] = (uint16_t)(k_float2int16 * motor_ankle.pos_desired + b_float2int16);
                txMsg16Normal[2] = 0;
                txMsg16Normal[3] = 0;
                txMsg16Normal[5] = 0;
                txMsg16Normal[6] = 0;
                msg162msg(2, txMsg);
                txMsg[0] = 0xfc;
                txMsg[1] = (uint8_t)((cmd_id & 0xf) << 4);
                txMsg[14] = (uint8_t)(0xf);
            }
            else if (cmd_id == CMD_VELOCITY_CTRL)
            {
                txMsg16Normal[0] = (uint16_t)(k_float2int16 * motor_knee.vel_desired + b_float2int16);
                txMsg16Normal[1] = (uint16_t)(k_float2int16 * motor_ankle.vel_desired + b_float2int16);
                txMsg16Normal[2] = 0;
                txMsg16Normal[3] = 0;
                txMsg16Normal[5] = 0;
                txMsg16Normal[6] = 0;
                msg162msg(2, txMsg);
                txMsg[0] = 0xfc;
                txMsg[1] = (uint8_t)((cmd_id & 0xf) << 4);
                txMsg[14] = (uint8_t)(0xf);
            }
            else if (cmd_id == CMD_POSITION_AND_VELOCITY)
            {
                txMsg16Normal[0] = (uint16_t)(k_float2int16 * motor_knee.pos_desired + b_float2int16);
                txMsg16Normal[1] = (uint16_t)(k_float2int16 * motor_knee.vel_desired + b_float2int16);
                txMsg16Normal[2] = (uint16_t)(k_float2int16 * motor_ankle.pos_desired + b_float2int16);
                txMsg16Normal[3] = (uint16_t)(k_float2int16 * motor_ankle.vel_desired + b_float2int16);
                txMsg16Normal[5] = 0;
                txMsg16Normal[6] = 0;
                msg162msg(2, txMsg);
                txMsg[0] = 0xfc;
                txMsg[1] = (uint8_t)((cmd_id & 0xf) << 4);
                txMsg[14] = (uint8_t)(0xf);
            }
            else if (cmd_id == CMD_TORQUE_CTRL)
            {
                txMsg16Normal[0] = (uint16_t)(k_float2int16 * motor_knee.cur_desired + b_float2int16);
                txMsg16Normal[1] = (uint16_t)(k_float2int16 * motor_ankle.cur_desired + b_float2int16);
                txMsg16Normal[2] = 0;
                txMsg16Normal[3] = 0;
                txMsg16Normal[5] = 0;
                txMsg16Normal[6] = 0;
                msg162msg(2, txMsg);
                txMsg[0] = 0xfc;
                txMsg[1] = (uint8_t)((cmd_id & 0xf) << 4);
                txMsg[14] = (uint8_t)(0xf);
            }
            else if (cmd_id == CMD_IMPEDANCE)
            {
                txMsg16Normal[0] = (uint16_t)(k_float2int16 * motor_knee.Kp + b_float2int16);
                txMsg16Normal[1] = (uint16_t)(k_float2int16 * motor_knee.Kb + b_float2int16);
                txMsg16Normal[2] = (uint16_t)(k_float2int16 * motor_ankle.Kp + b_float2int16);
                txMsg16Normal[3] = (uint16_t)(k_float2int16 * motor_ankle.Kb + b_float2int16);
                txMsg16Normal[5] = (uint16_t)(k_float2int16 * motor_knee.Angle_eq + b_float2int16);
                txMsg16Normal[6] = (uint16_t)(k_float2int16 * motor_ankle.Angle_eq + b_float2int16);
                msg162msg(2, txMsg);
                txMsg[0] = 0xfc;
                txMsg[1] = (uint8_t)((cmd_id & 0xf) << 4);
                txMsg[14] = (uint8_t)(0xf);
            }
        }
        void ROSUpdateMsg(ros_ctrl::Motor *knee, ros_ctrl::Motor *ankle)
        {
            knee->pos_actual = motor_knee.pos_actual;
            knee->pos_desired = motor_knee.pos_desired;
            knee->vel_actual = motor_knee.vel_actual;
            knee->vel_desired = motor_knee.vel_desired;
            knee->cur_actual = motor_knee.cur_actual;
            knee->cur_desired = motor_knee.cur_desired;
            knee->temperature = motor_knee.temperature;
            knee->Kp = motor_knee.Kp;
            knee->Kb = motor_knee.Kb;
            knee->Angle_eq = motor_knee.Angle_eq;
            knee->error = knee->pos_actual - knee->pos_desired;

            ankle->pos_actual = motor_ankle.pos_actual;
            ankle->pos_desired = motor_ankle.pos_desired;
            ankle->vel_actual = motor_ankle.vel_actual;
            ankle->vel_desired = motor_ankle.vel_desired;
            ankle->cur_actual = motor_ankle.cur_actual;
            ankle->cur_desired = motor_ankle.cur_desired;
            ankle->temperature = motor_ankle.temperature;
            ankle->Kp = motor_ankle.Kp;
            ankle->Kb = motor_ankle.Kb;
            ankle->Angle_eq = motor_ankle.Angle_eq;
        }

    private:
        float k_float2int16 = 300;
        float b_float2int16 = 30000;
        float k_float2int12 = 22;
        float b_float2int12 = 2110;
        uint16_t rxMsg16Normal[8];
        uint16_t txMsg16Normal[6];
        mutable std::mutex latestObservationMutex_;
};