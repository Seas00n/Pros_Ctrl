#ifndef SERIAL_STM32_
#define SERIAL_STM32_
#include "stdint.h"
#include "ros_ctrl/Motor.h"
#define UNPACK_OK 1
typedef struct{
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
}MotorTypeDef;
typedef enum{
	CMD_POSITION_CTRL=0,
	CMD_VELOCITY_CTRL=1,
	CMD_TORQUE_CTRL=2,
	CMD_POSITION_AND_VELOCITY=3,
	CMD_IMPEDANCE=4,
	CMD_QUICK_STOP=5
}CMD_PACKET_ID;
typedef enum{
	ReadyReading=0,
	BusyWriting=1
}Serial_State;
int PC_UnpackMessages(uint8_t rxMsg[],MotorTypeDef* knee, MotorTypeDef* ankle);
void PC_PackMessages(CMD_PACKET_ID id, uint8_t txMsg[], MotorTypeDef* knee,MotorTypeDef* ankle);
void UpdateWatcher(ros_ctrl::Motor* msg_knee, ros_ctrl::Motor* msg_ankle, MotorTypeDef* knee, MotorTypeDef* ankle);
void msg2msg16(int id_8_0,uint8_t rxMsg[]);
void msg162msg(int id_8_0,uint8_t rxMsg[]);
#endif