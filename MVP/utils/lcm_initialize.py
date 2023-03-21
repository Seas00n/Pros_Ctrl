import lcm
from lcm_msg.mvp_r import msg_r
from lcm_msg.mvp_t import msg_t


def lcm_initialize():
    mt = msg_t()
    mr = msg_r()
    lc_t = lcm.LCM()
    lc_r = lcm.LCM()
    return mt, mr, lc_t, lc_r
