#include "serial_msg.hpp"
#include "stdio.h"
static uint16_t rxMsg16[6];
static uint16_t txMsg16[4];
static uint16_t rxMsg16Normal[8];
static uint16_t txMsg16Normal[6];
//recommend to use PackNormal and UnpackNormal
//UnpackNormal: 18byte size
//PackNormal: 15byte size
static float k_float2int16 = 300;
static float b_float2int16 = 30000;
static float k_float2int12 = 22;
static float b_float2int12 = 2110;

static uint16_t temp,temp1,temp2;

int PC_UnpackMessages(uint8_t rxMsg[], MotorTypeDef* motor_knee, MotorTypeDef* motor_ankle){
    if(rxMsg[0]==0xFC&&rxMsg[13]==0xFF){
        motor_knee->state = BusyWriting;
        motor_ankle->state = BusyWriting;
        msg2msg16(1,rxMsg,rxMsg16);
        temp = (rxMsg16[0]>>4&0xfff);
        motor_knee->pos_actual = (float)(temp-b_float2int12)/k_float2int12;
        temp = ((rxMsg16[0]&0xf)<<8)|(rxMsg16[1]>>8&0xff);
        motor_knee->vel_actual = (float)(temp-b_float2int12)/k_float2int12;
        temp = ((rxMsg16[1]&0xff)<<4)|(rxMsg16[2]>>12&0xf);
        motor_ankle->pos_actual = (float)(temp-b_float2int12)/k_float2int12;
        temp = (rxMsg16[2]&0xfff);
        motor_ankle->vel_actual = (float)(temp-b_float2int12)/k_float2int12;
        temp = (rxMsg16[3]>>4&0xfff);
        motor_knee->cur_actual = (float)(temp-b_float2int12)/k_float2int12;
        temp = ((rxMsg16[3]&0xf)<<8)|(rxMsg16[4]>>8&0xff);
        motor_ankle->cur_actual = (float)(temp-b_float2int12)/k_float2int12;
        temp = ((rxMsg16[4]&0xff)<<4)|(rxMsg16[5]>>12&0xf);
        motor_knee->temperature = (float)(temp-b_float2int12)/k_float2int12;
        temp = (rxMsg16[5]&0xfff);
        motor_ankle->temperature = (float)(temp-b_float2int12)/k_float2int12;
        motor_knee->state = ReadyReading;
        motor_ankle->state = ReadyReading;
        return 1;
    }else{
        return 0;
    }
    return 0;
}
int PC_UnpackMessagesNormal(uint8_t rxMsg[], MotorTypeDef* motor_knee, MotorTypeDef* motor_ankle){
    if(rxMsg[0]==0xFC&&rxMsg[17]==0xFF){
        motor_knee->state = BusyWriting;
        motor_ankle->state = BusyWriting;
        msg2msg16(1,rxMsg,rxMsg16Normal);
        temp = rxMsg16Normal[0];
        motor_knee->pos_actual = (float)(temp-b_float2int16)/k_float2int16;
        temp = rxMsg16Normal[1];
        motor_knee->vel_actual = (float)(temp-b_float2int16)/k_float2int16;
        temp = rxMsg16Normal[2];
        motor_ankle->pos_actual = (float)(temp-b_float2int16)/k_float2int16;
        temp = rxMsg16Normal[3];
        motor_ankle->vel_actual = (float)(temp-b_float2int16)/k_float2int16;
        temp = rxMsg16Normal[4];
        motor_knee->cur_actual = (float)(temp-b_float2int16)/k_float2int16;
        temp = rxMsg16Normal[5];
        motor_ankle->cur_actual = (float)(temp-b_float2int16)/k_float2int16;
        temp = rxMsg16Normal[6];
        motor_knee->temperature = (float)(temp-b_float2int16)/k_float2int16;
        temp = rxMsg16Normal[7];
        motor_ankle->temperature = (float)(temp-b_float2int16)/k_float2int16;
        motor_knee->state = ReadyReading;
        motor_ankle->state = ReadyReading;
        return 1;
    }else{
        return 0;
    }
    return 0;
}

void PC_PackMessagesNormal(CMD_PACKET_ID cmd_id, uint8_t txMsg[], MotorTypeDef* motor_knee, MotorTypeDef* motor_ankle){
    if(cmd_id==CMD_QUICK_STOP){
        for(int i=0;i<6;i++){
            txMsg16Normal[i] = 0;
        }
        msg162msg(2,txMsg,txMsg16Normal);
        txMsg[0] = 0xfc;
        txMsg[1] = (uint8_t)((cmd_id&0xf)<<4);
        txMsg[14] = (uint8_t)(0xf);
    }else if(cmd_id==CMD_POSITION_CTRL){
        txMsg16Normal[0] = (uint16_t)(k_float2int16*motor_knee->pos_desired+b_float2int16);
        txMsg16Normal[1] = (uint16_t)(k_float2int16*motor_ankle->pos_desired+b_float2int16);
        txMsg16Normal[2] = 0;
        txMsg16Normal[3] = 0;
        txMsg16Normal[5] = 0;
        txMsg16Normal[6] = 0;
        msg162msg(2,txMsg,txMsg16Normal);
        txMsg[0] = 0xfc;
        txMsg[1] = (uint8_t)((cmd_id&0xf)<<4);
        txMsg[14] = (uint8_t)(0xf);
    }else if(cmd_id==CMD_VELOCITY_CTRL){
        txMsg16Normal[0] = (uint16_t)(k_float2int16*motor_knee->vel_desired+b_float2int16);
        txMsg16Normal[1] = (uint16_t)(k_float2int16*motor_ankle->vel_desired+b_float2int16);
        txMsg16Normal[2] = 0;
        txMsg16Normal[3] = 0;
        txMsg16Normal[5] = 0;
        txMsg16Normal[6] = 0;
        msg162msg(2,txMsg,txMsg16Normal);
        txMsg[0] = 0xfc;
        txMsg[1] = (uint8_t)((cmd_id&0xf)<<4);
        txMsg[14] = (uint8_t)(0xf);
    }else if(cmd_id==CMD_POSITION_AND_VELOCITY){
        txMsg16Normal[0] = (uint16_t)(k_float2int16*motor_knee->pos_desired+b_float2int16);
        txMsg16Normal[1] = (uint16_t)(k_float2int16*motor_knee->vel_desired+b_float2int16);
        txMsg16Normal[2] = (uint16_t)(k_float2int16*motor_ankle->pos_desired+b_float2int16);
        txMsg16Normal[3] = (uint16_t)(k_float2int16*motor_ankle->vel_desired+b_float2int16);
        txMsg16Normal[5] = 0;
        txMsg16Normal[6] = 0;
        msg162msg(2,txMsg,txMsg16Normal);
        txMsg[0] = 0xfc;
        txMsg[1] = (uint8_t)((cmd_id&0xf)<<4);
        txMsg[14] = (uint8_t)(0xf);
    }else if(cmd_id==CMD_TORQUE_CTRL){
        txMsg16Normal[0] = (uint16_t)(k_float2int16*motor_knee->cur_desired+b_float2int16);
        txMsg16Normal[1] = (uint16_t)(k_float2int16*motor_ankle->cur_desired+b_float2int16);
        txMsg16Normal[2] = 0;
        txMsg16Normal[3] = 0;
        txMsg16Normal[5] = 0;
        txMsg16Normal[6] = 0;
        msg162msg(2,txMsg,txMsg16Normal);
        txMsg[0] = 0xfc;
        txMsg[1] = (uint8_t)((cmd_id&0xf)<<4);
        txMsg[14] = (uint8_t)(0xf);
    }else if(cmd_id==CMD_IMPEDANCE){
        txMsg16Normal[0] = (uint16_t)(k_float2int16*motor_knee->Kp+b_float2int16);
        txMsg16Normal[1] = (uint16_t)(k_float2int16*motor_knee->Kb+b_float2int16);
        txMsg16Normal[2] = (uint16_t)(k_float2int16*motor_ankle->Kp+b_float2int16);
        txMsg16Normal[3] = (uint16_t)(k_float2int16*motor_ankle->Kb+b_float2int16);
        txMsg16Normal[5] = (uint16_t)(k_float2int16*motor_knee->Angle_eq+b_float2int16);
        txMsg16Normal[6] = (uint16_t)(k_float2int16*motor_ankle->Angle_eq+b_float2int16);
        msg162msg(2,txMsg,txMsg16Normal);
        txMsg[0] = 0xfc;
        txMsg[1] = (uint8_t)((cmd_id&0xf)<<4);
        txMsg[14] = (uint8_t)(0xf);
    }

}

void PC_PackMessages(CMD_PACKET_ID cmd_id, uint8_t txMsg[], MotorTypeDef* motor_knee, MotorTypeDef* motor_ankle){
    if(cmd_id==CMD_QUICK_STOP){
        txMsg[0] = 0xfc;
        txMsg[1] = (uint8_t)((cmd_id&0xf)<<4);
        txMsg[10] = (uint8_t)(0xf);
    }else if(cmd_id==CMD_POSITION_CTRL){
        txMsg16[0] = (uint16_t)(k_float2int16*motor_knee->pos_desired+b_float2int16);
        txMsg16[1] = (uint16_t)(k_float2int16*motor_ankle->pos_desired+b_float2int16);
        txMsg16[2] = 0;
        txMsg16[3] = 0;
        msg162msg(2,txMsg,txMsg16);
        txMsg[0] = 0xfc;
        txMsg[1] = (uint8_t)((cmd_id&0xf)<<4);
        txMsg[10] = (uint8_t)(0xf);
    }else if(cmd_id==CMD_VELOCITY_CTRL){
        txMsg16[0] = (uint16_t)(k_float2int16*motor_knee->vel_desired+b_float2int16);
        txMsg16[1] = (uint16_t)(k_float2int16*motor_ankle->vel_desired+b_float2int16);
        txMsg16[2] = 0;
        txMsg16[3] = 0;
        msg162msg(2,txMsg,txMsg16);
        txMsg[0] = 0xfc;
        txMsg[1] = (uint8_t)((cmd_id&0xf)<<4);
        txMsg[10] = (uint8_t)(0xf);
    }else if(cmd_id==CMD_POSITION_AND_VELOCITY){
        txMsg16[0] = (uint16_t)(k_float2int16*motor_knee->pos_desired+b_float2int16);
        txMsg16[1] = (uint16_t)(k_float2int16*motor_knee->vel_desired+b_float2int16);
        txMsg16[2] = (uint16_t)(k_float2int16*motor_ankle->pos_desired+b_float2int16);
        txMsg16[3] = (uint16_t)(k_float2int16*motor_ankle->vel_desired+b_float2int16);
        msg162msg(2,txMsg,txMsg16);
        txMsg[0] = 0xfc;
        txMsg[1] = (uint8_t)((cmd_id&0xf)<<4);
        txMsg[10] = (uint8_t)(0xf);
    }else if(cmd_id==CMD_TORQUE_CTRL){
        txMsg16[0] = (uint16_t)(k_float2int16*motor_knee->cur_desired+b_float2int16);
        txMsg16[1] = (uint16_t)(k_float2int16*motor_ankle->cur_desired+b_float2int16);
        txMsg16[2] = 0;
        txMsg16[3] = 0;
        msg162msg(2,txMsg,txMsg16);
        txMsg[0] = 0xfc;
        txMsg[1] = (uint8_t)((cmd_id&0xf)<<4);
        txMsg[10] = (uint8_t)(0xf);
    }else if(cmd_id==CMD_IMPEDANCE){
        temp = (uint16_t)(motor_ankle->Angle_eq*k_float2int12+b_float2int12);
        txMsg[0] = 0xfc;
        txMsg[1] = (uint8_t)(((cmd_id&0xf)<<4)|temp>>4&0xf);
        txMsg[10] = (uint8_t)(((temp&0xf)<<4)|0xf);
        temp1 = (uint16_t)(motor_knee->Kp*k_float2int12+b_float2int12);
        temp2 = (uint16_t)(motor_knee->Kb*k_float2int12+b_float2int12);
        txMsg16[0] = (uint16_t)(((temp1&0xfff)<<4)|(temp2>>8&0xf));
        temp1 =  (uint16_t)(motor_ankle->Kp*k_float2int12+b_float2int12);
        txMsg16[1] = (uint16_t)(((temp2&0xff)<<8)|(temp1>>4&0xff));
        temp2 =  (uint16_t)(motor_ankle->Kb*k_float2int12+b_float2int12);
        txMsg16[2] = (uint16_t)(((temp1&0xf)<<12)|(temp2&0xfff));
        temp1 =  (uint16_t)(motor_knee->Angle_eq*k_float2int12+b_float2int12);
        temp2 = (uint16_t)(motor_ankle->Angle_eq*k_float2int12+b_float2int12);
        txMsg16[3] =  (uint16_t)(((temp1&0xfff)<<4)|(temp2>>8&0xf));
        msg162msg(2,txMsg,txMsg16);
    }else{}
}

void msg2msg16(int id_8_0,uint8_t rxMsg[],uint16_t rx16[]){
    int id_16=0;
    for(id_16=0;id_16<sizeof(rxMsg16)/2;id_16++){
        rxMsg16[id_16] = (rxMsg[id_8_0+id_16*2]<<8)|(rxMsg[id_8_0+id_16*2+1]);
    }
}
void msg162msg(int id_8_0,uint8_t txMsg[],uint16_t tx16[]){
    int id_16 = 0;
    for(id_16=0;id_16<sizeof(txMsg16)/2;id_16++){
        txMsg[id_8_0+id_16*2] = (uint8_t)(txMsg16[id_16]>>8);
        txMsg[id_8_0+id_16*2+1] = (uint8_t)(txMsg16[id_16]&0xff);
    }
}
void UpdateWatcher(ros_ctrl::Motor* knee, ros_ctrl::Motor* ankle,
                    MotorTypeDef* motor_knee, MotorTypeDef* motor_ankle){
    knee->pos_actual = motor_knee->pos_actual;
    knee->pos_desired = motor_knee->pos_desired;
    // uint16_t temp = (uint16_t)(k_float2int16*motor_knee->pos_desired+b_float2int16);
    // uint8_t temp0 = (uint8_t)(temp>>8);
    // uint8_t temp1 = (uint8_t)(temp&0xff);
    // temp = (uint16_t)(temp0<<8|temp1);
    // float temp2 = (float)((temp-b_float2int16)/k_float2int16);
    // uint16_t temp3 = (uint16_t)(temp2*k_float2int12+b_float2int12);
    // temp3 = ((temp3&0xfff)<<4|(0>>8&0xf));
    // temp0 = (uint8_t)(temp3>>8);
    // temp1 = (uint8_t)(temp3&0xff);
    // temp3 = (temp0<<8)|(temp1);
    // temp = (temp3>>4&0xfff);
    // knee->pos_actual = (float)(temp-b_float2int12)/k_float2int12;
    knee->vel_actual = motor_knee->vel_actual;
    knee->vel_desired = motor_knee->vel_desired;
    knee->cur_actual = motor_knee->cur_actual;
    knee->cur_desired = motor_knee->cur_desired;
    knee->temperature = motor_knee->temperature;
    knee->Kp = motor_knee->Kp;
    knee->Kb = motor_knee->Kb;
    knee->Angle_eq = motor_knee->Angle_eq;
    knee->error = knee->pos_actual-knee->pos_desired;

    ankle->pos_actual = motor_ankle->pos_actual;
    ankle->pos_desired = motor_ankle->pos_desired;
    ankle->vel_actual = motor_ankle->vel_actual;
    ankle->vel_desired = motor_ankle->vel_desired;
    ankle->cur_actual = motor_ankle->cur_actual;
    ankle->cur_desired = motor_ankle->cur_desired;
    ankle->temperature = motor_ankle->temperature;
    ankle->Kp = motor_ankle->Kp;
    ankle->Kb = motor_ankle->Kb;
    ankle->Angle_eq = motor_ankle->Angle_eq;
}