;; Auto-generated. Do not edit!


(when (boundp 'agvcode::WordCount)
  (if (not (find-package "AGVCODE"))
    (make-package "AGVCODE"))
  (shadow 'WordCount (find-package "AGVCODE")))
(unless (find-package "AGVCODE::WORDCOUNT")
  (make-package "AGVCODE::WORDCOUNT"))
(unless (find-package "AGVCODE::WORDCOUNTREQUEST")
  (make-package "AGVCODE::WORDCOUNTREQUEST"))
(unless (find-package "AGVCODE::WORDCOUNTRESPONSE")
  (make-package "AGVCODE::WORDCOUNTRESPONSE"))

(in-package "ROS")





(defclass agvcode::WordCountRequest
  :super ros::object
  :slots (_words ))

(defmethod agvcode::WordCountRequest
  (:init
   (&key
    ((:words __words) 0.0)
    )
   (send-super :init)
   (setq _words (float __words))
   self)
  (:words
   (&optional __words)
   (if __words (setq _words __words)) _words)
  (:serialization-length
   ()
   (+
    ;; float32 _words
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _words
       (sys::poke _words (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _words
     (setq _words (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass agvcode::WordCountResponse
  :super ros::object
  :slots (_count ))

(defmethod agvcode::WordCountResponse
  (:init
   (&key
    ((:count __count) 0)
    )
   (send-super :init)
   (setq _count (round __count))
   self)
  (:count
   (&optional __count)
   (if __count (setq _count __count)) _count)
  (:serialization-length
   ()
   (+
    ;; uint32 _count
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint32 _count
       (write-long _count s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint32 _count
     (setq _count (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass agvcode::WordCount
  :super ros::object
  :slots ())

(setf (get agvcode::WordCount :md5sum-) "a9a24dbc1cac26f2f8c73d77906b969c")
(setf (get agvcode::WordCount :datatype-) "agvcode/WordCount")
(setf (get agvcode::WordCount :request) agvcode::WordCountRequest)
(setf (get agvcode::WordCount :response) agvcode::WordCountResponse)

(defmethod agvcode::WordCountRequest
  (:response () (instance agvcode::WordCountResponse :init)))

(setf (get agvcode::WordCountRequest :md5sum-) "a9a24dbc1cac26f2f8c73d77906b969c")
(setf (get agvcode::WordCountRequest :datatype-) "agvcode/WordCountRequest")
(setf (get agvcode::WordCountRequest :definition-)
      "float32 words
---
uint32 count

")

(setf (get agvcode::WordCountResponse :md5sum-) "a9a24dbc1cac26f2f8c73d77906b969c")
(setf (get agvcode::WordCountResponse :datatype-) "agvcode/WordCountResponse")
(setf (get agvcode::WordCountResponse :definition-)
      "float32 words
---
uint32 count

")



(provide :agvcode/WordCount "a9a24dbc1cac26f2f8c73d77906b969c")


