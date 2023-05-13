#include "ros/ros.h"
#include "std_msgs/String.h"
#include "serial/serial.h"
#include "lcm/lcm-cpp.hpp"
#include "serial_msg.hpp"
#include "ros_ctrl/Motor.h"
#include "msg_t.hpp"
#include "msg_r.hpp"
#include "lcm_.hpp"
#include "time.h"
#include "unistd.h"
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






int main(int argc, char ** argv){
    //节点初始化
    setlocale(LC_ALL,"");
    ros::init(argc, argv, "serial_port");
    ros::NodeHandle n;
    ros::Rate loop_rate(1000);
    
    //串口初始化
    serial::Serial ser;
    try{
        ser.setPort("/dev/ttyUSB0");
        ser.setBaudrate(115200);
        serial::Timeout to = serial::Timeout::simpleTimeout(100);
        ser.setTimeout(to);
        ser.open();
    }catch(serial::IOException &e){
        ROS_INFO_STREAM("Fail to Open Port\n");
        return -1;
    }
    ROS_INFO_STREAM("Success to Open Port\n");
    volatile size_t byte_read;
    
    //LCM 通信初始化
    if(!lc_r.good()||(!lc_r.good()))
        return 1;
    mvp_t::msg_t mt;
    mvp_r::msg_r mr;

    //ROS 通信初始化
    ros::Publisher pub1 = n.advertise<ros_ctrl::Motor>("motor_watcher1",100);
    ros::Publisher pub2 = n.advertise<ros_ctrl::Motor>("motor_watcher2",100);

    //电机对象初始化
    ros_ctrl::Motor m1;
    ros_ctrl::Motor m2;
    motor_knee.pos_desired = 0;
    motor_ankle.pos_desired = 0;
    PC_PackMessages(CMD_POSITION_CTRL,txMsg,&motor_knee,&motor_ankle);
    ser.write(txMsg,sizeof(txMsg));
    
    //消息计数器
    volatile double start, end;
    volatile double total_start,total_end;
    int counter_rx = 0;
    int counter_tx = 0;

    SubscribeLCMHandler handleObject;
    lc_t.subscribe("HIGH_TO_MIDDLE",&SubscribeLCMHandler::handleMessage,&handleObject);
    total_start = clock();
    while (ros::ok()){
        lc_t.handleTimeout(10);
        ros::spinOnce();
        loop_rate.sleep();
        start = clock();
        byte_read = ser.read(rxMsg,sizeof(rxMsg));
        if(PC_UnpackMessages(rxMsg,&motor_knee,&motor_ankle)==1){
            counter_rx++;
            printf("Receive Message %d, ",counter_rx);
        }else{
            printf("Something Wrong\r\n");
        }
        end = clock();
        printf("Time cost:%f, byte_read=%d\n",(double)((end-start)/CLOCKS_PER_SEC),(int)counter_rx);

        start = clock();
        PC_PackMessages((CMD_PACKET_ID)(motor_knee.mode),txMsg,&motor_knee,&motor_ankle);
        ser.write(txMsg,sizeof(txMsg));
        printf("Send Message %d, ",counter_tx);
        end = clock();
        counter_tx+=1;
        printf("Time cost:%f, byte_send=%d\n",(double)(end-start)/CLOCKS_PER_SEC,(int)counter_tx);

        if(counter_tx>=10000){
            counter_tx = 0;
            printf("%f",double(end-start));
            break;
        }
        

        UpdateWatcher(&m1,&m2,&motor_knee,&motor_ankle);
        pub1.publish(m1);
        pub2.publish(m2);
        PublishLCM(mr);
        ROS_INFO("Pos_knee_Desired:%.2f,Pos_knee_Actual:%.2f,error:%.2f",m1.pos_desired,m1.pos_actual,
                                                                m1.pos_desired-m1.pos_actual); 
        ROS_INFO("Pos_ankle_Desired:%.2f,Pos_ankle_Actual:%.2f",motor_ankle.pos_desired,motor_ankle.pos_actual);
        
    }
    ser.close();
    return 0;

}






























// void PC_UnpackMessages(){
//     if(rxMsg[0]==0xFC&&rxMsg[sizeof(rxMsg)-1]==0xFF){
//         // memcpy(rxMsg16,rxMsg,sizeof(rxMsg16));
//         msg2msg16(1);
//         temp = (rxMsg16[0]>>4&0xfff);
//         motor_knee.pos_actual = (float)(temp-b_float2int12)/k_float2int12;
//         temp = ((rxMsg16[0]&0xf)<<8)|(rxMsg16[1]>>8&0xff);
//         motor_knee.vel_actual = (float)(temp-b_float2int12)/k_float2int12;
//         temp = ((rxMsg16[1]&0xff)<<4)|(rxMsg16[2]>>12&0xf);
//         motor_ankle.pos_actual = (float)(temp-b_float2int12)/k_float2int12;
//         temp = (rxMsg16[2]&0xfff);
//         motor_ankle.vel_actual = (float)(temp-b_float2int12)/k_float2int12;
//         temp = (rxMsg16[3]>>4&0xfff);
//         motor_knee.cur_actual = (float)(temp-b_float2int12)/k_float2int12;
//         temp = ((rxMsg16[3]&0xf)<<8)|(rxMsg16[4]>>8&0xff);
//         motor_ankle.cur_actual = (float)(temp-b_float2int12)/k_float2int12;
//         temp = ((rxMsg16[4]&0xff)<<4)|(rxMsg16[5]>>12&0xf);
//         motor_knee.temperature = (float)(temp-b_float2int12)/k_float2int12;
//         temp = (rxMsg16[5]&0xfff);
//         motor_ankle.temperature = (float)(temp-b_float2int12)/k_float2int12;
//         ROS_INFO("Pos_knee:%.2f,Pos_ankle:%.2f",motor_knee.pos_actual,motor_ankle.pos_actual);
//         ROS_INFO("Vel_knee:%.2f,Vel_ankle:%.2f",motor_knee.vel_actual,motor_ankle.vel_actual);
//     }else{}
// }
// void PC_PackMessages(CMD_PACKET_ID cmd_id){
//     if(cmd_id==CMD_QUICK_STOP){
//         txMsg[0] = (uint8_t)(cmd_id&0xf<<4);
//         txMsg[9] = (uint8_t)(0xf);
//     }else if(cmd_id==CMD_POSITION_CTRL){
//         txMsg16[0] = (uint16_t)(k_float2int16*motor_knee.pos_desired+b_float2int16);
//         txMsg16[1] = (uint16_t)(k_float2int16*motor_ankle.pos_desired+b_float2int16);
//         txMsg16[2] = 0;
//         txMsg16[3] = 0;
//         // memcpy(txMsg+1,txMsg16,sizeof(txMsg16));
//         msg162msg(1);
//         txMsg[0] = (uint8_t)(cmd_id&0xf<<4);
//         txMsg[9] = (uint8_t)(0xf);
//     }else if(cmd_id==CMD_VELOCITY_CTRL){
//         txMsg16[0] = (uint16_t)(k_float2int16*motor_knee.vel_desired+b_float2int16);
//         txMsg16[1] = (uint16_t)(k_float2int16*motor_ankle.vel_desired+b_float2int16);
//         txMsg16[2] = 0;
//         txMsg16[3] = 0;
//         // memcpy(txMsg+1,txMsg16,sizeof(txMsg16));
//         msg162msg(1);
//         txMsg[0] = (uint8_t)(cmd_id&0xf<<4);
//         txMsg[9] = (uint8_t)(0xf);
//     }else if(cmd_id==CMD_POSITION_AND_VELOCITY){
//         txMsg16[0] = (uint16_t)(k_float2int16*motor_knee.pos_desired+b_float2int16);
//         txMsg16[1] = (uint16_t)(k_float2int16*motor_ankle.pos_desired+b_float2int16);
//         txMsg16[2] = (uint16_t)(k_float2int16*motor_knee.vel_desired+b_float2int16);
//         txMsg16[3] = (uint16_t)(k_float2int16*motor_ankle.vel_desired+b_float2int16);
//         // memcpy(txMsg+1,txMsg16,sizeof(txMsg16));
//         msg162msg(1);
//         txMsg[0] = (uint8_t)(cmd_id&0xf<<4);
//         txMsg[9] = (uint8_t)(0xf);
//     }else if(cmd_id==CMD_TORQUE_CTRL){
//         txMsg16[0] = (uint16_t)(k_float2int16*motor_knee.cur_desired+b_float2int16);
//         txMsg16[1] = (uint16_t)(k_float2int16*motor_ankle.cur_desired+b_float2int16);
//         txMsg16[2] = 0;
//         txMsg16[3] = 0;
//         // memcpy(txMsg+1,txMsg16,sizeof(txMsg16));
//         msg162msg(1);
//         txMsg[0] = (uint8_t)(cmd_id&0xf<<4);
//         txMsg[9] = (uint8_t)(0xf);
//     }else if(cmd_id==CMD_IMPEDANCE){
//         temp = (uint16_t)(motor_ankle.Angle_eq*k_float2int12+b_float2int12);
//         txMsg[0] = (uint8_t)(((cmd_id&0xf)<<4)|temp>>4&0xf);
//         txMsg[9] = (uint8_t)(((temp&0xf)<<4)|0xf);
//         temp1 = (uint16_t)(motor_knee.Kp*k_float2int12+b_float2int12);
//         temp2 = (uint16_t)(motor_knee.Kb*k_float2int12+b_float2int12);
//         txMsg16[0] = (uint16_t)(((temp1&0xfff)<<4)|(temp2>>8&0xf));
//         temp1 =  (uint16_t)(motor_ankle.Kp*k_float2int12+b_float2int12);
//         txMsg16[1] = (uint16_t)(((temp2&0xff)<<8)|(temp1>>4&0xff));
//         temp2 =  (uint16_t)(motor_ankle.Kb*k_float2int12+b_float2int12);
//         txMsg16[2] = (uint16_t)(((temp1&0xf)<<12)|(temp2&0xfff));
//         temp1 =  (uint16_t)(motor_knee.Angle_eq*k_float2int12+b_float2int12);
//         temp2 = (uint16_t)(motor_ankle.Angle_eq*k_float2int12+b_float2int12);
//         txMsg16[3] =  (uint16_t)(((temp1&0xfff)<<4)|(temp2>>8&0xf));
//         // memcpy(txMsg+1,txMsg16,sizeof(txMsg16));
//         msg162msg(1);
//     }else{}
// }
// void UpdateWatcher(ros_ctrl::Motor* knee, ros_ctrl::Motor* ankle){
//     knee->pos_actual = motor_knee.pos_actual;
//     knee->pos_desired = motor_knee.pos_desired;
//     knee->vel_actual = motor_knee.vel_actual;
//     knee->vel_desired = motor_knee.vel_desired;
//     knee->cur_actual = motor_knee.cur_actual;
//     knee->cur_desired = motor_knee.cur_desired;
//     knee->temperature = motor_knee.temperature;
//     knee->Kp = motor_knee.Kp;
//     knee->Kb = motor_knee.Kb;
//     knee->Angle_eq = motor_knee.Angle_eq;

//     ankle->pos_actual = motor_ankle.pos_actual;
//     ankle->pos_desired = motor_ankle.pos_desired;
//     ankle->vel_actual = motor_ankle.vel_actual;
//     ankle->vel_desired = motor_ankle.vel_desired;
//     ankle->cur_actual = motor_ankle.cur_actual;
//     ankle->cur_desired = motor_ankle.cur_desired;
//     ankle->temperature = motor_ankle.temperature;
//     ankle->Kp = motor_ankle.Kp;
//     ankle->Kb = motor_ankle.Kb;
//     ankle->Angle_eq = motor_ankle.Angle_eq;
// }
// void msg2msg16(int id_8_0){
//     int id_16=0;
//     for(id_16=0;id_16<sizeof(rxMsg16)/2;id_16++){
//         rxMsg16[id_16] = (rxMsg[id_8_0+id_16*2]<<8)|(rxMsg[id_8_0+id_16*2+1]);
//     }
// }
// void msg162msg(int id_8_0){
//     int id_16 = 0;
//     for(id_16=0;id_16<sizeof(txMsg16)/2;id_16++){
//         txMsg[id_8_0+id_16*2] = (uint8_t)(txMsg16[id_16]>>8);
//         txMsg[id_8_0+id_16*2+1] = (uint8_t)(txMsg16[id_16]&0xff);
//     }
// }


