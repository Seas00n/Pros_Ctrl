#ifndef SERIAL_STM32_
#define SERIAL_STM32_
#include "stdint.h"
#include "ros_ctrl/Motor.h"
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
}MotorTypeDef;
typedef enum{
	CMD_POSITION_CTRL,
	CMD_VELOCITY_CTRL,
	CMD_TORQUE_CTRL,
	CMD_POSITION_AND_VELOCITY,
	CMD_IMPEDANCE,
	CMD_QUICK_STOP
}CMD_PACKET_ID;
void PC_UnpackMessages(void);
void PC_PackMessages(CMD_PACKET_ID id);
void UpdateWatcher(ros_ctrl::Motor* knee, ros_ctrl::Motor* ankle);
void msg2msg16(int id_8_0);
void msg162msg(int id_8_0);
#endif