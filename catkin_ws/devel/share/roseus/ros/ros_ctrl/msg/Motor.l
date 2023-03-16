;; Auto-generated. Do not edit!


(when (boundp 'ros_ctrl::Motor)
  (if (not (find-package "ROS_CTRL"))
    (make-package "ROS_CTRL"))
  (shadow 'Motor (find-package "ROS_CTRL")))
(unless (find-package "ROS_CTRL::MOTOR")
  (make-package "ROS_CTRL::MOTOR"))

(in-package "ROS")
;;//! \htmlinclude Motor.msg.html


(defclass ros_ctrl::Motor
  :super ros::object
  :slots (_pos_desired _pos_actual _vel_desired _vel_actual _cur_desired _cur_actual _temperature _Kp _Kb _Angle_eq ))

(defmethod ros_ctrl::Motor
  (:init
   (&key
    ((:pos_desired __pos_desired) 0.0)
    ((:pos_actual __pos_actual) 0.0)
    ((:vel_desired __vel_desired) 0.0)
    ((:vel_actual __vel_actual) 0.0)
    ((:cur_desired __cur_desired) 0.0)
    ((:cur_actual __cur_actual) 0.0)
    ((:temperature __temperature) 0.0)
    ((:Kp __Kp) 0.0)
    ((:Kb __Kb) 0.0)
    ((:Angle_eq __Angle_eq) 0.0)
    )
   (send-super :init)
   (setq _pos_desired (float __pos_desired))
   (setq _pos_actual (float __pos_actual))
   (setq _vel_desired (float __vel_desired))
   (setq _vel_actual (float __vel_actual))
   (setq _cur_desired (float __cur_desired))
   (setq _cur_actual (float __cur_actual))
   (setq _temperature (float __temperature))
   (setq _Kp (float __Kp))
   (setq _Kb (float __Kb))
   (setq _Angle_eq (float __Angle_eq))
   self)
  (:pos_desired
   (&optional __pos_desired)
   (if __pos_desired (setq _pos_desired __pos_desired)) _pos_desired)
  (:pos_actual
   (&optional __pos_actual)
   (if __pos_actual (setq _pos_actual __pos_actual)) _pos_actual)
  (:vel_desired
   (&optional __vel_desired)
   (if __vel_desired (setq _vel_desired __vel_desired)) _vel_desired)
  (:vel_actual
   (&optional __vel_actual)
   (if __vel_actual (setq _vel_actual __vel_actual)) _vel_actual)
  (:cur_desired
   (&optional __cur_desired)
   (if __cur_desired (setq _cur_desired __cur_desired)) _cur_desired)
  (:cur_actual
   (&optional __cur_actual)
   (if __cur_actual (setq _cur_actual __cur_actual)) _cur_actual)
  (:temperature
   (&optional __temperature)
   (if __temperature (setq _temperature __temperature)) _temperature)
  (:Kp
   (&optional __Kp)
   (if __Kp (setq _Kp __Kp)) _Kp)
  (:Kb
   (&optional __Kb)
   (if __Kb (setq _Kb __Kb)) _Kb)
  (:Angle_eq
   (&optional __Angle_eq)
   (if __Angle_eq (setq _Angle_eq __Angle_eq)) _Angle_eq)
  (:serialization-length
   ()
   (+
    ;; float64 _pos_desired
    8
    ;; float64 _pos_actual
    8
    ;; float64 _vel_desired
    8
    ;; float64 _vel_actual
    8
    ;; float64 _cur_desired
    8
    ;; float64 _cur_actual
    8
    ;; float64 _temperature
    8
    ;; float64 _Kp
    8
    ;; float64 _Kb
    8
    ;; float64 _Angle_eq
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _pos_desired
       (sys::poke _pos_desired (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _pos_actual
       (sys::poke _pos_actual (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _vel_desired
       (sys::poke _vel_desired (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _vel_actual
       (sys::poke _vel_actual (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _cur_desired
       (sys::poke _cur_desired (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _cur_actual
       (sys::poke _cur_actual (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _temperature
       (sys::poke _temperature (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _Kp
       (sys::poke _Kp (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _Kb
       (sys::poke _Kb (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _Angle_eq
       (sys::poke _Angle_eq (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _pos_desired
     (setq _pos_desired (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _pos_actual
     (setq _pos_actual (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _vel_desired
     (setq _vel_desired (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _vel_actual
     (setq _vel_actual (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _cur_desired
     (setq _cur_desired (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _cur_actual
     (setq _cur_actual (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _temperature
     (setq _temperature (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _Kp
     (setq _Kp (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _Kb
     (setq _Kb (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _Angle_eq
     (setq _Angle_eq (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get ros_ctrl::Motor :md5sum-) "e4cbdf296cd255d692be25d05074c48d")
(setf (get ros_ctrl::Motor :datatype-) "ros_ctrl/Motor")
(setf (get ros_ctrl::Motor :definition-)
      "float64 pos_desired
float64 pos_actual
float64 vel_desired
float64 vel_actual
float64 cur_desired
float64 cur_actual
float64 temperature
float64 Kp
float64 Kb
float64 Angle_eq
")



(provide :ros_ctrl/Motor "e4cbdf296cd255d692be25d05074c48d")


