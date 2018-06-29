; Auto-generated. Do not edit!


(cl:in-package agvcode-srv)


;//! \htmlinclude WordCount-request.msg.html

(cl:defclass <WordCount-request> (roslisp-msg-protocol:ros-message)
  ((words
    :reader words
    :initarg :words
    :type cl:float
    :initform 0.0))
)

(cl:defclass WordCount-request (<WordCount-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <WordCount-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'WordCount-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name agvcode-srv:<WordCount-request> is deprecated: use agvcode-srv:WordCount-request instead.")))

(cl:ensure-generic-function 'words-val :lambda-list '(m))
(cl:defmethod words-val ((m <WordCount-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader agvcode-srv:words-val is deprecated.  Use agvcode-srv:words instead.")
  (words m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <WordCount-request>) ostream)
  "Serializes a message object of type '<WordCount-request>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'words))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <WordCount-request>) istream)
  "Deserializes a message object of type '<WordCount-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'words) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<WordCount-request>)))
  "Returns string type for a service object of type '<WordCount-request>"
  "agvcode/WordCountRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'WordCount-request)))
  "Returns string type for a service object of type 'WordCount-request"
  "agvcode/WordCountRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<WordCount-request>)))
  "Returns md5sum for a message object of type '<WordCount-request>"
  "a9a24dbc1cac26f2f8c73d77906b969c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'WordCount-request)))
  "Returns md5sum for a message object of type 'WordCount-request"
  "a9a24dbc1cac26f2f8c73d77906b969c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<WordCount-request>)))
  "Returns full string definition for message of type '<WordCount-request>"
  (cl:format cl:nil "float32 words~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'WordCount-request)))
  "Returns full string definition for message of type 'WordCount-request"
  (cl:format cl:nil "float32 words~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <WordCount-request>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <WordCount-request>))
  "Converts a ROS message object to a list"
  (cl:list 'WordCount-request
    (cl:cons ':words (words msg))
))
;//! \htmlinclude WordCount-response.msg.html

(cl:defclass <WordCount-response> (roslisp-msg-protocol:ros-message)
  ((count
    :reader count
    :initarg :count
    :type cl:integer
    :initform 0))
)

(cl:defclass WordCount-response (<WordCount-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <WordCount-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'WordCount-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name agvcode-srv:<WordCount-response> is deprecated: use agvcode-srv:WordCount-response instead.")))

(cl:ensure-generic-function 'count-val :lambda-list '(m))
(cl:defmethod count-val ((m <WordCount-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader agvcode-srv:count-val is deprecated.  Use agvcode-srv:count instead.")
  (count m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <WordCount-response>) ostream)
  "Serializes a message object of type '<WordCount-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'count)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'count)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'count)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'count)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <WordCount-response>) istream)
  "Deserializes a message object of type '<WordCount-response>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'count)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'count)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'count)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'count)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<WordCount-response>)))
  "Returns string type for a service object of type '<WordCount-response>"
  "agvcode/WordCountResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'WordCount-response)))
  "Returns string type for a service object of type 'WordCount-response"
  "agvcode/WordCountResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<WordCount-response>)))
  "Returns md5sum for a message object of type '<WordCount-response>"
  "a9a24dbc1cac26f2f8c73d77906b969c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'WordCount-response)))
  "Returns md5sum for a message object of type 'WordCount-response"
  "a9a24dbc1cac26f2f8c73d77906b969c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<WordCount-response>)))
  "Returns full string definition for message of type '<WordCount-response>"
  (cl:format cl:nil "uint32 count~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'WordCount-response)))
  "Returns full string definition for message of type 'WordCount-response"
  (cl:format cl:nil "uint32 count~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <WordCount-response>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <WordCount-response>))
  "Converts a ROS message object to a list"
  (cl:list 'WordCount-response
    (cl:cons ':count (count msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'WordCount)))
  'WordCount-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'WordCount)))
  'WordCount-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'WordCount)))
  "Returns string type for a service object of type '<WordCount>"
  "agvcode/WordCount")