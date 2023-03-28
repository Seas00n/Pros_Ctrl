;; Auto-generated. Do not edit!


(when (boundp 'ros_ctrl::Kill)
  (if (not (find-package "ROS_CTRL"))
    (make-package "ROS_CTRL"))
  (shadow 'Kill (find-package "ROS_CTRL")))
(unless (find-package "ROS_CTRL::KILL")
  (make-package "ROS_CTRL::KILL"))
(unless (find-package "ROS_CTRL::KILLREQUEST")
  (make-package "ROS_CTRL::KILLREQUEST"))
(unless (find-package "ROS_CTRL::KILLRESPONSE")
  (make-package "ROS_CTRL::KILLRESPONSE"))

(in-package "ROS")





(defclass ros_ctrl::KillRequest
  :super ros::object
  :slots (_name ))

(defmethod ros_ctrl::KillRequest
  (:init
   (&key
    ((:name __name) "")
    )
   (send-super :init)
   (setq _name (string __name))
   self)
  (:name
   (&optional __name)
   (if __name (setq _name __name)) _name)
  (:serialization-length
   ()
   (+
    ;; string _name
    4 (length _name)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _name
       (write-long (length _name) s) (princ _name s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass ros_ctrl::KillResponse
  :super ros::object
  :slots ())

(defmethod ros_ctrl::KillResponse
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass ros_ctrl::Kill
  :super ros::object
  :slots ())

(setf (get ros_ctrl::Kill :md5sum-) "c1f3d28f1b044c871e6eff2e9fc3c667")
(setf (get ros_ctrl::Kill :datatype-) "ros_ctrl/Kill")
(setf (get ros_ctrl::Kill :request) ros_ctrl::KillRequest)
(setf (get ros_ctrl::Kill :response) ros_ctrl::KillResponse)

(defmethod ros_ctrl::KillRequest
  (:response () (instance ros_ctrl::KillResponse :init)))

(setf (get ros_ctrl::KillRequest :md5sum-) "c1f3d28f1b044c871e6eff2e9fc3c667")
(setf (get ros_ctrl::KillRequest :datatype-) "ros_ctrl/KillRequest")
(setf (get ros_ctrl::KillRequest :definition-)
      "string name
---
")

(setf (get ros_ctrl::KillResponse :md5sum-) "c1f3d28f1b044c871e6eff2e9fc3c667")
(setf (get ros_ctrl::KillResponse :datatype-) "ros_ctrl/KillResponse")
(setf (get ros_ctrl::KillResponse :definition-)
      "string name
---
")



(provide :ros_ctrl/Kill "c1f3d28f1b044c871e6eff2e9fc3c667")


