; Auto-generated. Do not edit!


(cl:in-package pros_multisensor-msg)


;//! \htmlinclude Foot_Plate.msg.html

(cl:defclass <Foot_Plate> (roslisp-msg-protocol:ros-message)
  ((F_area1
    :reader F_area1
    :initarg :F_area1
    :type cl:float
    :initform 0.0)
   (x_area1
    :reader x_area1
    :initarg :x_area1
    :type cl:float
    :initform 0.0)
   (y_area1
    :reader y_area1
    :initarg :y_area1
    :type cl:float
    :initform 0.0)
   (F_area2
    :reader F_area2
    :initarg :F_area2
    :type cl:float
    :initform 0.0)
   (x_area2
    :reader x_area2
    :initarg :x_area2
    :type cl:float
    :initform 0.0)
   (y_area2
    :reader y_area2
    :initarg :y_area2
    :type cl:float
    :initform 0.0)
   (F_area3
    :reader F_area3
    :initarg :F_area3
    :type cl:float
    :initform 0.0)
   (x_area3
    :reader x_area3
    :initarg :x_area3
    :type cl:float
    :initform 0.0)
   (y_area3
    :reader y_area3
    :initarg :y_area3
    :type cl:float
    :initform 0.0)
   (F_net
    :reader F_net
    :initarg :F_net
    :type cl:float
    :initform 0.0)
   (x_net
    :reader x_net
    :initarg :x_net
    :type cl:float
    :initform 0.0)
   (y_net
    :reader y_net
    :initarg :y_net
    :type cl:float
    :initform 0.0)
   (contact
    :reader contact
    :initarg :contact
    :type cl:fixnum
    :initform 0))
)

(cl:defclass Foot_Plate (<Foot_Plate>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Foot_Plate>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Foot_Plate)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pros_multisensor-msg:<Foot_Plate> is deprecated: use pros_multisensor-msg:Foot_Plate instead.")))

(cl:ensure-generic-function 'F_area1-val :lambda-list '(m))
(cl:defmethod F_area1-val ((m <Foot_Plate>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pros_multisensor-msg:F_area1-val is deprecated.  Use pros_multisensor-msg:F_area1 instead.")
  (F_area1 m))

(cl:ensure-generic-function 'x_area1-val :lambda-list '(m))
(cl:defmethod x_area1-val ((m <Foot_Plate>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pros_multisensor-msg:x_area1-val is deprecated.  Use pros_multisensor-msg:x_area1 instead.")
  (x_area1 m))

(cl:ensure-generic-function 'y_area1-val :lambda-list '(m))
(cl:defmethod y_area1-val ((m <Foot_Plate>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pros_multisensor-msg:y_area1-val is deprecated.  Use pros_multisensor-msg:y_area1 instead.")
  (y_area1 m))

(cl:ensure-generic-function 'F_area2-val :lambda-list '(m))
(cl:defmethod F_area2-val ((m <Foot_Plate>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pros_multisensor-msg:F_area2-val is deprecated.  Use pros_multisensor-msg:F_area2 instead.")
  (F_area2 m))

(cl:ensure-generic-function 'x_area2-val :lambda-list '(m))
(cl:defmethod x_area2-val ((m <Foot_Plate>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pros_multisensor-msg:x_area2-val is deprecated.  Use pros_multisensor-msg:x_area2 instead.")
  (x_area2 m))

(cl:ensure-generic-function 'y_area2-val :lambda-list '(m))
(cl:defmethod y_area2-val ((m <Foot_Plate>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pros_multisensor-msg:y_area2-val is deprecated.  Use pros_multisensor-msg:y_area2 instead.")
  (y_area2 m))

(cl:ensure-generic-function 'F_area3-val :lambda-list '(m))
(cl:defmethod F_area3-val ((m <Foot_Plate>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pros_multisensor-msg:F_area3-val is deprecated.  Use pros_multisensor-msg:F_area3 instead.")
  (F_area3 m))

(cl:ensure-generic-function 'x_area3-val :lambda-list '(m))
(cl:defmethod x_area3-val ((m <Foot_Plate>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pros_multisensor-msg:x_area3-val is deprecated.  Use pros_multisensor-msg:x_area3 instead.")
  (x_area3 m))

(cl:ensure-generic-function 'y_area3-val :lambda-list '(m))
(cl:defmethod y_area3-val ((m <Foot_Plate>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pros_multisensor-msg:y_area3-val is deprecated.  Use pros_multisensor-msg:y_area3 instead.")
  (y_area3 m))

(cl:ensure-generic-function 'F_net-val :lambda-list '(m))
(cl:defmethod F_net-val ((m <Foot_Plate>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pros_multisensor-msg:F_net-val is deprecated.  Use pros_multisensor-msg:F_net instead.")
  (F_net m))

(cl:ensure-generic-function 'x_net-val :lambda-list '(m))
(cl:defmethod x_net-val ((m <Foot_Plate>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pros_multisensor-msg:x_net-val is deprecated.  Use pros_multisensor-msg:x_net instead.")
  (x_net m))

(cl:ensure-generic-function 'y_net-val :lambda-list '(m))
(cl:defmethod y_net-val ((m <Foot_Plate>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pros_multisensor-msg:y_net-val is deprecated.  Use pros_multisensor-msg:y_net instead.")
  (y_net m))

(cl:ensure-generic-function 'contact-val :lambda-list '(m))
(cl:defmethod contact-val ((m <Foot_Plate>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pros_multisensor-msg:contact-val is deprecated.  Use pros_multisensor-msg:contact instead.")
  (contact m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Foot_Plate>) ostream)
  "Serializes a message object of type '<Foot_Plate>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'F_area1))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'x_area1))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'y_area1))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'F_area2))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'x_area2))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'y_area2))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'F_area3))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'x_area3))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'y_area3))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'F_net))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'x_net))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'y_net))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let* ((signed (cl:slot-value msg 'contact)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Foot_Plate>) istream)
  "Deserializes a message object of type '<Foot_Plate>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'F_area1) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x_area1) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y_area1) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'F_area2) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x_area2) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y_area2) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'F_area3) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x_area3) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y_area3) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'F_net) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x_net) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y_net) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'contact) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Foot_Plate>)))
  "Returns string type for a message object of type '<Foot_Plate>"
  "pros_multisensor/Foot_Plate")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Foot_Plate)))
  "Returns string type for a message object of type 'Foot_Plate"
  "pros_multisensor/Foot_Plate")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Foot_Plate>)))
  "Returns md5sum for a message object of type '<Foot_Plate>"
  "e96a18f41c104b55b04d72c552abf512")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Foot_Plate)))
  "Returns md5sum for a message object of type 'Foot_Plate"
  "e96a18f41c104b55b04d72c552abf512")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Foot_Plate>)))
  "Returns full string definition for message of type '<Foot_Plate>"
  (cl:format cl:nil "float32 F_area1~%float32 x_area1~%float32 y_area1~%float32 F_area2~%float32 x_area2~%float32 y_area2~%float32 F_area3~%float32 x_area3~%float32 y_area3~%float32 F_net~%float32 x_net~%float32 y_net~%int8 contact~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Foot_Plate)))
  "Returns full string definition for message of type 'Foot_Plate"
  (cl:format cl:nil "float32 F_area1~%float32 x_area1~%float32 y_area1~%float32 F_area2~%float32 x_area2~%float32 y_area2~%float32 F_area3~%float32 x_area3~%float32 y_area3~%float32 F_net~%float32 x_net~%float32 y_net~%int8 contact~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Foot_Plate>))
  (cl:+ 0
     4
     4
     4
     4
     4
     4
     4
     4
     4
     4
     4
     4
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Foot_Plate>))
  "Converts a ROS message object to a list"
  (cl:list 'Foot_Plate
    (cl:cons ':F_area1 (F_area1 msg))
    (cl:cons ':x_area1 (x_area1 msg))
    (cl:cons ':y_area1 (y_area1 msg))
    (cl:cons ':F_area2 (F_area2 msg))
    (cl:cons ':x_area2 (x_area2 msg))
    (cl:cons ':y_area2 (y_area2 msg))
    (cl:cons ':F_area3 (F_area3 msg))
    (cl:cons ':x_area3 (x_area3 msg))
    (cl:cons ':y_area3 (y_area3 msg))
    (cl:cons ':F_net (F_net msg))
    (cl:cons ':x_net (x_net msg))
    (cl:cons ':y_net (y_net msg))
    (cl:cons ':contact (contact msg))
))
