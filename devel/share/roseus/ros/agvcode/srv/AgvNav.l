;; Auto-generated. Do not edit!


(when (boundp 'agvcode::AgvNav)
  (if (not (find-package "AGVCODE"))
    (make-package "AGVCODE"))
  (shadow 'AgvNav (find-package "AGVCODE")))
(unless (find-package "AGVCODE::AGVNAV")
  (make-package "AGVCODE::AGVNAV"))
(unless (find-package "AGVCODE::AGVNAVREQUEST")
  (make-package "AGVCODE::AGVNAVREQUEST"))
(unless (find-package "AGVCODE::AGVNAVRESPONSE")
  (make-package "AGVCODE::AGVNAVRESPONSE"))

(in-package "ROS")





(defclass agvcode::AgvNavRequest
  :super ros::object
  :slots (_coordinate ))

(defmethod agvcode::AgvNavRequest
  (:init
   (&key
    ((:coordinate __coordinate) "")
    )
   (send-super :init)
   (setq _coordinate (string __coordinate))
   self)
  (:coordinate
   (&optional __coordinate)
   (if __coordinate (setq _coordinate __coordinate)) _coordinate)
  (:serialization-length
   ()
   (+
    ;; string _coordinate
    4 (length _coordinate)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _coordinate
       (write-long (length _coordinate) s) (princ _coordinate s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _coordinate
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _coordinate (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass agvcode::AgvNavResponse
  :super ros::object
  :slots (_status _error_msg ))

(defmethod agvcode::AgvNavResponse
  (:init
   (&key
    ((:status __status) nil)
    ((:error_msg __error_msg) "")
    )
   (send-super :init)
   (setq _status __status)
   (setq _error_msg (string __error_msg))
   self)
  (:status
   (&optional __status)
   (if __status (setq _status __status)) _status)
  (:error_msg
   (&optional __error_msg)
   (if __error_msg (setq _error_msg __error_msg)) _error_msg)
  (:serialization-length
   ()
   (+
    ;; bool _status
    1
    ;; string _error_msg
    4 (length _error_msg)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _status
       (if _status (write-byte -1 s) (write-byte 0 s))
     ;; string _error_msg
       (write-long (length _error_msg) s) (princ _error_msg s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _status
     (setq _status (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; string _error_msg
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _error_msg (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass agvcode::AgvNav
  :super ros::object
  :slots ())

(setf (get agvcode::AgvNav :md5sum-) "d314b4d308820390a64698753b2ba3b9")
(setf (get agvcode::AgvNav :datatype-) "agvcode/AgvNav")
(setf (get agvcode::AgvNav :request) agvcode::AgvNavRequest)
(setf (get agvcode::AgvNav :response) agvcode::AgvNavResponse)

(defmethod agvcode::AgvNavRequest
  (:response () (instance agvcode::AgvNavResponse :init)))

(setf (get agvcode::AgvNavRequest :md5sum-) "d314b4d308820390a64698753b2ba3b9")
(setf (get agvcode::AgvNavRequest :datatype-) "agvcode/AgvNavRequest")
(setf (get agvcode::AgvNavRequest :definition-)
      "string coordinate
---
bool status
string error_msg


")

(setf (get agvcode::AgvNavResponse :md5sum-) "d314b4d308820390a64698753b2ba3b9")
(setf (get agvcode::AgvNavResponse :datatype-) "agvcode/AgvNavResponse")
(setf (get agvcode::AgvNavResponse :definition-)
      "string coordinate
---
bool status
string error_msg


")



(provide :agvcode/AgvNav "d314b4d308820390a64698753b2ba3b9")


