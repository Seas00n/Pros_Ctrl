;; Auto-generated. Do not edit!


(when (boundp 'pros_multisensor::Foot_Plate)
  (if (not (find-package "PROS_MULTISENSOR"))
    (make-package "PROS_MULTISENSOR"))
  (shadow 'Foot_Plate (find-package "PROS_MULTISENSOR")))
(unless (find-package "PROS_MULTISENSOR::FOOT_PLATE")
  (make-package "PROS_MULTISENSOR::FOOT_PLATE"))

(in-package "ROS")
;;//! \htmlinclude Foot_Plate.msg.html


(defclass pros_multisensor::Foot_Plate
  :super ros::object
  :slots (_F_area1 _x_area1 _y_area1 _F_area2 _x_area2 _y_area2 _F_area3 _x_area3 _y_area3 _F_net _x_net _y_net _contact ))

(defmethod pros_multisensor::Foot_Plate
  (:init
   (&key
    ((:F_area1 __F_area1) 0.0)
    ((:x_area1 __x_area1) 0.0)
    ((:y_area1 __y_area1) 0.0)
    ((:F_area2 __F_area2) 0.0)
    ((:x_area2 __x_area2) 0.0)
    ((:y_area2 __y_area2) 0.0)
    ((:F_area3 __F_area3) 0.0)
    ((:x_area3 __x_area3) 0.0)
    ((:y_area3 __y_area3) 0.0)
    ((:F_net __F_net) 0.0)
    ((:x_net __x_net) 0.0)
    ((:y_net __y_net) 0.0)
    ((:contact __contact) 0)
    )
   (send-super :init)
   (setq _F_area1 (float __F_area1))
   (setq _x_area1 (float __x_area1))
   (setq _y_area1 (float __y_area1))
   (setq _F_area2 (float __F_area2))
   (setq _x_area2 (float __x_area2))
   (setq _y_area2 (float __y_area2))
   (setq _F_area3 (float __F_area3))
   (setq _x_area3 (float __x_area3))
   (setq _y_area3 (float __y_area3))
   (setq _F_net (float __F_net))
   (setq _x_net (float __x_net))
   (setq _y_net (float __y_net))
   (setq _contact (round __contact))
   self)
  (:F_area1
   (&optional __F_area1)
   (if __F_area1 (setq _F_area1 __F_area1)) _F_area1)
  (:x_area1
   (&optional __x_area1)
   (if __x_area1 (setq _x_area1 __x_area1)) _x_area1)
  (:y_area1
   (&optional __y_area1)
   (if __y_area1 (setq _y_area1 __y_area1)) _y_area1)
  (:F_area2
   (&optional __F_area2)
   (if __F_area2 (setq _F_area2 __F_area2)) _F_area2)
  (:x_area2
   (&optional __x_area2)
   (if __x_area2 (setq _x_area2 __x_area2)) _x_area2)
  (:y_area2
   (&optional __y_area2)
   (if __y_area2 (setq _y_area2 __y_area2)) _y_area2)
  (:F_area3
   (&optional __F_area3)
   (if __F_area3 (setq _F_area3 __F_area3)) _F_area3)
  (:x_area3
   (&optional __x_area3)
   (if __x_area3 (setq _x_area3 __x_area3)) _x_area3)
  (:y_area3
   (&optional __y_area3)
   (if __y_area3 (setq _y_area3 __y_area3)) _y_area3)
  (:F_net
   (&optional __F_net)
   (if __F_net (setq _F_net __F_net)) _F_net)
  (:x_net
   (&optional __x_net)
   (if __x_net (setq _x_net __x_net)) _x_net)
  (:y_net
   (&optional __y_net)
   (if __y_net (setq _y_net __y_net)) _y_net)
  (:contact
   (&optional __contact)
   (if __contact (setq _contact __contact)) _contact)
  (:serialization-length
   ()
   (+
    ;; float32 _F_area1
    4
    ;; float32 _x_area1
    4
    ;; float32 _y_area1
    4
    ;; float32 _F_area2
    4
    ;; float32 _x_area2
    4
    ;; float32 _y_area2
    4
    ;; float32 _F_area3
    4
    ;; float32 _x_area3
    4
    ;; float32 _y_area3
    4
    ;; float32 _F_net
    4
    ;; float32 _x_net
    4
    ;; float32 _y_net
    4
    ;; int8 _contact
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _F_area1
       (sys::poke _F_area1 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _x_area1
       (sys::poke _x_area1 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _y_area1
       (sys::poke _y_area1 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _F_area2
       (sys::poke _F_area2 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _x_area2
       (sys::poke _x_area2 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _y_area2
       (sys::poke _y_area2 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _F_area3
       (sys::poke _F_area3 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _x_area3
       (sys::poke _x_area3 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _y_area3
       (sys::poke _y_area3 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _F_net
       (sys::poke _F_net (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _x_net
       (sys::poke _x_net (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _y_net
       (sys::poke _y_net (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; int8 _contact
       (write-byte _contact s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _F_area1
     (setq _F_area1 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _x_area1
     (setq _x_area1 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y_area1
     (setq _y_area1 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _F_area2
     (setq _F_area2 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _x_area2
     (setq _x_area2 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y_area2
     (setq _y_area2 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _F_area3
     (setq _F_area3 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _x_area3
     (setq _x_area3 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y_area3
     (setq _y_area3 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _F_net
     (setq _F_net (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _x_net
     (setq _x_net (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y_net
     (setq _y_net (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; int8 _contact
     (setq _contact (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _contact 127) (setq _contact (- _contact 256)))
   ;;
   self)
  )

(setf (get pros_multisensor::Foot_Plate :md5sum-) "e96a18f41c104b55b04d72c552abf512")
(setf (get pros_multisensor::Foot_Plate :datatype-) "pros_multisensor/Foot_Plate")
(setf (get pros_multisensor::Foot_Plate :definition-)
      "float32 F_area1
float32 x_area1
float32 y_area1
float32 F_area2
float32 x_area2
float32 y_area2
float32 F_area3
float32 x_area3
float32 y_area3
float32 F_net
float32 x_net
float32 y_net
int8 contact

")



(provide :pros_multisensor/Foot_Plate "e96a18f41c104b55b04d72c552abf512")


