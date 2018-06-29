; Auto-generated. Do not edit!


(cl:in-package agvcode-srv)


;//! \htmlinclude AgvNav-request.msg.html

(cl:defclass <AgvNav-request> (roslisp-msg-protocol:ros-message)
  ((coordinate
    :reader coordinate
    :initarg :coordinate
    :type cl:string
    :initform ""))
)

(cl:defclass AgvNav-request (<AgvNav-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AgvNav-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AgvNav-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name agvcode-srv:<AgvNav-request> is deprecated: use agvcode-srv:AgvNav-request instead.")))

(cl:ensure-generic-function 'coordinate-val :lambda-list '(m))
(cl:defmethod coordinate-val ((m <AgvNav-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader agvcode-srv:coordinate-val is deprecated.  Use agvcode-srv:coordinate instead.")
  (coordinate m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AgvNav-request>) ostream)
  "Serializes a message object of type '<AgvNav-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'coordinate))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'coordinate))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AgvNav-request>) istream)
  "Deserializes a message object of type '<AgvNav-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'coordinate) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'coordinate) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AgvNav-request>)))
  "Returns string type for a service object of type '<AgvNav-request>"
  "agvcode/AgvNavRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AgvNav-request)))
  "Returns string type for a service object of type 'AgvNav-request"
  "agvcode/AgvNavRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AgvNav-request>)))
  "Returns md5sum for a message object of type '<AgvNav-request>"
  "d314b4d308820390a64698753b2ba3b9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AgvNav-request)))
  "Returns md5sum for a message object of type 'AgvNav-request"
  "d314b4d308820390a64698753b2ba3b9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AgvNav-request>)))
  "Returns full string definition for message of type '<AgvNav-request>"
  (cl:format cl:nil "string coordinate~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AgvNav-request)))
  "Returns full string definition for message of type 'AgvNav-request"
  (cl:format cl:nil "string coordinate~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AgvNav-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'coordinate))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AgvNav-request>))
  "Converts a ROS message object to a list"
  (cl:list 'AgvNav-request
    (cl:cons ':coordinate (coordinate msg))
))
;//! \htmlinclude AgvNav-response.msg.html

(cl:defclass <AgvNav-response> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type cl:boolean
    :initform cl:nil)
   (error_msg
    :reader error_msg
    :initarg :error_msg
    :type cl:string
    :initform ""))
)

(cl:defclass AgvNav-response (<AgvNav-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AgvNav-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AgvNav-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name agvcode-srv:<AgvNav-response> is deprecated: use agvcode-srv:AgvNav-response instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <AgvNav-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader agvcode-srv:status-val is deprecated.  Use agvcode-srv:status instead.")
  (status m))

(cl:ensure-generic-function 'error_msg-val :lambda-list '(m))
(cl:defmethod error_msg-val ((m <AgvNav-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader agvcode-srv:error_msg-val is deprecated.  Use agvcode-srv:error_msg instead.")
  (error_msg m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AgvNav-response>) ostream)
  "Serializes a message object of type '<AgvNav-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'status) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'error_msg))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'error_msg))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AgvNav-response>) istream)
  "Deserializes a message object of type '<AgvNav-response>"
    (cl:setf (cl:slot-value msg 'status) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'error_msg) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'error_msg) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AgvNav-response>)))
  "Returns string type for a service object of type '<AgvNav-response>"
  "agvcode/AgvNavResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AgvNav-response)))
  "Returns string type for a service object of type 'AgvNav-response"
  "agvcode/AgvNavResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AgvNav-response>)))
  "Returns md5sum for a message object of type '<AgvNav-response>"
  "d314b4d308820390a64698753b2ba3b9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AgvNav-response)))
  "Returns md5sum for a message object of type 'AgvNav-response"
  "d314b4d308820390a64698753b2ba3b9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AgvNav-response>)))
  "Returns full string definition for message of type '<AgvNav-response>"
  (cl:format cl:nil "bool status~%string error_msg~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AgvNav-response)))
  "Returns full string definition for message of type 'AgvNav-response"
  (cl:format cl:nil "bool status~%string error_msg~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AgvNav-response>))
  (cl:+ 0
     1
     4 (cl:length (cl:slot-value msg 'error_msg))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AgvNav-response>))
  "Converts a ROS message object to a list"
  (cl:list 'AgvNav-response
    (cl:cons ':status (status msg))
    (cl:cons ':error_msg (error_msg msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'AgvNav)))
  'AgvNav-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'AgvNav)))
  'AgvNav-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AgvNav)))
  "Returns string type for a service object of type '<AgvNav>"
  "agvcode/AgvNav")