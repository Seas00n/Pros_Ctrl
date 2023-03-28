import numpy as np
from lcm_msg.mvp_t import msg_t
from lcm_msg.mvp_r import msg_r

from lcm_initialize import *

total_timestep = 10000
Pi = np.pi


class Motor():
    def __init__(self):
        self.pos_desired = 0
        self.pos_actual = 0
        self.vel_desired = 0
        self.vel_actual = 0
        self.cur_desired = 0
        self.cur_actual = 0
        self.Kp = 0
        self.Kd = 0
        self.Angle_eq = 0
        self.Mode = 0
        self.State = 1


Knee = Motor()
Ankle = Motor()


def my_handler(channel, data):
    msg = msg_r.decode(data)
    Knee.pos_actual = msg.knee_position_actual
    Ankle.pos_actual = msg.ankle_position_actual
    Knee.vel_actual = msg.knee_velocity_actual
    Ankle.vel_actual = msg.ankle_velocity_actual
    Knee.cur_actual = msg.knee_torque_actual
    Ankle.cur_actual = msg.ankle_torque_actual
    print("Received message on channel \"%s\"" % channel)


if __name__ == '__main__':
    mt, mr, lc_t, lc_r = lcm_initialize()
    subscription = lc_r.subscribe("MIDDLE_TO_HIGH", my_handler)
    write_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    try:
        for i in range(total_timestep):
            mt.knee_position_desired = 50 * np.sin(i * 0.02 * Pi)
            mt.ankle_position_desired = -50 * np.sin(i * 0.02 * Pi)
            mt.knee_velocity_desired = 10 * np.cos(i * 0.02 * Pi)
            mt.ankle_velocity_desired = -10 * np.cos(i * 0.02 * Pi)
            # mt.knee_position_desired = write_array[int(np.floor(i*0.02))%10]
            lc_t.publish("HIGH_TO_MIDDLE", mt.encode())
            lc_r.handle()
    except KeyboardInterrupt:
        pass
