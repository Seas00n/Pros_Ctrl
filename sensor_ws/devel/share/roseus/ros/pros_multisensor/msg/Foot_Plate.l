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
  :slots (_F_area1 _x_area1 _y_area1 _F_area2 _x_area2 _y_area2 _F_area3 _x_area3 _y_area3 ))

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
  (:serialization-length
   ()
   (+
    ;; float64 _F_area1
    8
    ;; float64 _x_area1
    8
    ;; float64 _y_area1
    8
    ;; float64 _F_area2
    8
    ;; float64 _x_area2
    8
    ;; float64 _y_area2
    8
    ;; float64 _F_area3
    8
    ;; float64 _x_area3
    8
    ;; float64 _y_area3
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _F_area1
       (sys::poke _F_area1 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _x_area1
       (sys::poke _x_area1 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y_area1
       (sys::poke _y_area1 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _F_area2
       (sys::poke _F_area2 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _x_area2
       (sys::poke _x_area2 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y_area2
       (sys::poke _y_area2 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _F_area3
       (sys::poke _F_area3 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _x_area3
       (sys::poke _x_area3 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y_area3
       (sys::poke _y_area3 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _F_area1
     (setq _F_area1 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _x_area1
     (setq _x_area1 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y_area1
     (setq _y_area1 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _F_area2
     (setq _F_area2 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _x_area2
     (setq _x_area2 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y_area2
     (setq _y_area2 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _F_area3
     (setq _F_area3 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _x_area3
     (setq _x_area3 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y_area3
     (setq _y_area3 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get pros_multisensor::Foot_Plate :md5sum-) "8abe2ed9ca3a52015264ef11ea8b519b")
(setf (get pros_multisensor::Foot_Plate :datatype-) "pros_multisensor/Foot_Plate")
(setf (get pros_multisensor::Foot_Plate :definition-)
      "float64 F_area1
float64 x_area1
float64 y_area1
float64 F_area2
float64 x_area2
float64 y_area2
float64 F_area3
float64 x_area3
float64 y_area3

")



(provide :pros_multisensor/Foot_Plate "8abe2ed9ca3a52015264ef11ea8b519b")


