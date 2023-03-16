#include "ros/ros.h"
#include "std_msgs/String.h"
#include "serial/serial.h"
#include "lcm/lcm-cpp.hpp"
#include "serial_stm32.h"
#include "ros_ctrl/Motor.h"
static uint8_t txDataBuffer[200];
static uint8_t rxDataBuffer[200];
static uint8_t rxMsg[14];
static uint8_t rxMsgSwap[14];
static uint16_t rxMsg16[6];
static uint8_t txMsg[10];
static uint16_t txMsg16[4];
static int i,j,k;

static float k_float2int16 = 300;
static float b_float2int16 = 30000;
static float k_float2int12 = 22;
static float b_float2int12 = 2110;

MotorTypeDef motor_knee;
MotorTypeDef motor_ankle;

static uint16_t temp,temp1,temp2;




int main(int argc, char ** argv){
    setlocale(LC_ALL,"");
    ros::init(argc, argv, "serial_port");
    ros::NodeHandle n;
    serial::Serial ser;
    try{
        ser.setPort("/dev/ttyUSB0");
        ser.setBaudrate(115200);
        serial::Timeout to = serial::Timeout::simpleTimeout(50);
        ser.setTimeout(to);
        ser.open();
    }catch(serial::IOException &e){
        ROS_INFO_STREAM("Fail to Open Port\n");
        return -1;
    }
    ROS_INFO_STREAM("Success to Open Port\n");
    ros::Publisher pub1 = n.advertise<ros_ctrl::Motor>("motor_watcher1",10);
    ros::Publisher pub2 = n.advertise<ros_ctrl::Motor>("motor_watcher2",10);
    ros_ctrl::Motor m1;
    ros_ctrl::Motor m2;
    
    ros::Rate loop_rate(100);
    motor_knee.pos_desired = 0;
    motor_ankle.pos_desired = 0;
    PC_PackMessages(CMD_POSITION_CTRL);
    ser.write(txMsg,sizeof(txMsg));

    int counter = 0;
    while (ros::ok()){
        // if(ser.available()) {
            size_t byte_read = ser.read(rxDataBuffer,sizeof(rxDataBuffer));
            for(i=0;i<byte_read;i++){
                if(rxDataBuffer[i]==0xFC){
                    j = i+sizeof(rxMsg)-1;
                    if(j>=byte_read){
                        break;
                    }else{
                        if(rxDataBuffer[j]==0xFF){
                            memcpy(rxMsg,(rxDataBuffer+i),sizeof(rxMsg));
                            PC_UnpackMessages();
                            break;
                        }else{
                            i=j;
                        }
                    }
                }
            }

        // }
        // if(ser.available()){
            motor_knee.pos_desired = 90;
            motor_ankle.pos_desired = -89;
            PC_PackMessages(CMD_POSITION_CTRL);
            ser.write(txMsg,sizeof(txMsg));
            printf("Msg %d Send\n",counter);
            counter+=1;
            if(counter>100000){
                counter = 0;
            }
        // }
        UpdateWatcher(&m1,&m2);
        pub1.publish(m1);
        pub2.publish(m2);
        ros::spinOnce();
        loop_rate.sleep();
    }
    ser.close();
    return 0;

}
void PC_UnpackMessages(){
    if(rxMsg[0]==0xFC&&rxMsg[sizeof(rxMsg)-1]==0xFF){
        // memcpy(rxMsg16,rxMsg,sizeof(rxMsg16));
        msg2msg16(1);
        temp = (rxMsg16[0]>>4&0xfff);
        motor_knee.pos_actual = (float)(temp-b_float2int12)/k_float2int12;
        temp = ((rxMsg16[0]&0xf)<<8)|(rxMsg16[1]>>8&0xff);
        motor_knee.vel_actual = (float)(temp-b_float2int12)/k_float2int12;
        temp = ((rxMsg16[1]&0xff)<<4)|(rxMsg16[2]>>12&0xf);
        motor_ankle.pos_actual = (float)(temp-b_float2int12)/k_float2int12;
        temp = (rxMsg16[2]&0xfff);
        motor_ankle.vel_actual = (float)(temp-b_float2int12)/k_float2int12;
        temp = (rxMsg16[3]>>4&0xfff);
        motor_knee.cur_actual = (float)(temp-b_float2int12)/k_float2int12;
        temp = ((rxMsg16[3]&0xf)<<8)|(rxMsg16[4]>>8&0xff);
        motor_ankle.cur_actual = (float)(temp-b_float2int12)/k_float2int12;
        temp = ((rxMsg16[4]&0xff)<<4)|(rxMsg16[5]>>12&0xf);
        motor_knee.temperature = (float)(temp-b_float2int12)/k_float2int12;
        temp = (rxMsg16[5]&0xfff);
        motor_ankle.temperature = (float)(temp-b_float2int12)/k_float2int12;
        ROS_INFO("Pos_knee:%.2f,Pos_ankle:%.2f",motor_knee.pos_actual,motor_ankle.pos_actual);
        ROS_INFO("Vel_knee:%.2f,Vel_ankle:%.2f",motor_knee.vel_actual,motor_ankle.vel_actual);
    }else{}
}

void PC_PackMessages(CMD_PACKET_ID cmd_id){
    if(cmd_id==CMD_QUICK_STOP){
        txMsg[0] = (uint8_t)(cmd_id&0xf<<4);
        txMsg[9] = (uint8_t)(0xf);
    }else if(cmd_id==CMD_POSITION_CTRL){
        txMsg16[0] = (uint16_t)(k_float2int16*motor_knee.pos_desired+b_float2int16);
        txMsg16[1] = (uint16_t)(k_float2int16*motor_ankle.pos_desired+b_float2int16);
        txMsg16[2] = 0;
        txMsg16[3] = 0;
        // memcpy(txMsg+1,txMsg16,sizeof(txMsg16));
        msg162msg(1);
        txMsg[0] = (uint8_t)(cmd_id&0xf<<4);
        txMsg[9] = (uint8_t)(0xf);
    }else if(cmd_id==CMD_VELOCITY_CTRL){
        txMsg16[0] = (uint16_t)(k_float2int16*motor_knee.vel_desired+b_float2int16);
        txMsg16[1] = (uint16_t)(k_float2int16*motor_ankle.vel_desired+b_float2int16);
        txMsg16[2] = 0;
        txMsg16[3] = 0;
        // memcpy(txMsg+1,txMsg16,sizeof(txMsg16));
        msg162msg(1);
        txMsg[0] = (uint8_t)(cmd_id&0xf<<4);
        txMsg[9] = (uint8_t)(0xf);
    }else if(cmd_id==CMD_POSITION_AND_VELOCITY){
        txMsg16[0] = (uint16_t)(k_float2int16*motor_knee.pos_desired+b_float2int16);
        txMsg16[1] = (uint16_t)(k_float2int16*motor_ankle.pos_desired+b_float2int16);
        txMsg16[2] = (uint16_t)(k_float2int16*motor_knee.vel_desired+b_float2int16);
        txMsg16[3] = (uint16_t)(k_float2int16*motor_ankle.vel_desired+b_float2int16);
        // memcpy(txMsg+1,txMsg16,sizeof(txMsg16));
        msg162msg(1);
        txMsg[0] = (uint8_t)(cmd_id&0xf<<4);
        txMsg[9] = (uint8_t)(0xf);
    }else if(cmd_id==CMD_TORQUE_CTRL){
        txMsg16[0] = (uint16_t)(k_float2int16*motor_knee.cur_desired+b_float2int16);
        txMsg16[1] = (uint16_t)(k_float2int16*motor_ankle.cur_desired+b_float2int16);
        txMsg16[2] = 0;
        txMsg16[3] = 0;
        // memcpy(txMsg+1,txMsg16,sizeof(txMsg16));
        msg162msg(1);
        txMsg[0] = (uint8_t)(cmd_id&0xf<<4);
        txMsg[9] = (uint8_t)(0xf);
    }else if(cmd_id==CMD_IMPEDANCE){
        temp = (uint16_t)(motor_ankle.Angle_eq*k_float2int12+b_float2int12);
        txMsg[0] = (uint8_t)(((cmd_id&0xf)<<4)|temp>>4&0xf);
        txMsg[9] = (uint8_t)(((temp&0xf)<<4)|0xf);
        temp1 = (uint16_t)(motor_knee.Kp*k_float2int12+b_float2int12);
        temp2 = (uint16_t)(motor_knee.Kb*k_float2int12+b_float2int12);
        txMsg16[0] = (uint16_t)(((temp1&0xfff)<<4)|(temp2>>8&0xf));
        temp1 =  (uint16_t)(motor_ankle.Kp*k_float2int12+b_float2int12);
        txMsg16[1] = (uint16_t)(((temp2&0xff)<<8)|(temp1>>4&0xff));
        temp2 =  (uint16_t)(motor_ankle.Kb*k_float2int12+b_float2int12);
        txMsg16[2] = (uint16_t)(((temp1&0xf)<<12)|(temp2&0xfff));
        temp1 =  (uint16_t)(motor_knee.Angle_eq*k_float2int12+b_float2int12);
        temp2 = (uint16_t)(motor_ankle.Angle_eq*k_float2int12+b_float2int12);
        txMsg16[3] =  (uint16_t)(((temp1&0xfff)<<4)|(temp2>>8&0xf));
        // memcpy(txMsg+1,txMsg16,sizeof(txMsg16));
        msg162msg(1);
    }else{}
}

void UpdateWatcher(ros_ctrl::Motor* knee, ros_ctrl::Motor* ankle){
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
void msg2msg16(int id_8_0){
    int id_16=0;
    for(id_16=0;id_16<sizeof(rxMsg16)/2;id_16++){
        rxMsg16[id_16] = (rxMsg[id_8_0+id_16*2]<<8)|(rxMsg[id_8_0+id_16*2+1]);
    }
}
void msg162msg(int id_8_0){
    int id_16 = 0;
    for(id_16=0;id_16<sizeof(txMsg16)/2;id_16++){
        txMsg[id_8_0+id_16*2] = (uint8_t)(txMsg16[id_16]>>8);
        txMsg[id_8_0+id_16*2+1] = (uint8_t)(txMsg16[id_16]&0xff);
    }
}