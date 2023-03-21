lcm-gen -p msg_t.lcm
lcm-gen -p msg_r.lcm
lcm-gen -x msg_t.lcm
lcm-gen -x msg_r.lcm
sudo cp ./mvp_r/msg_r.hpp /home/yuxuan/Project/Pros_Ctrl/catkin_ws/src/ros_ctrl/include/ros_ctrl/msg_r.hpp
sudo cp ./mvp_t/msg_t.hpp /home/yuxuan/Project/Pros_Ctrl/catkin_ws/src/ros_ctrl/include/ros_ctrl/msg_t.hpp
