;; Auto-generated. Do not edit!


(when (boundp 'agvworkspace::WordCount)
  (if (not (find-package "AGVWORKSPACE"))
    (make-package "AGVWORKSPACE"))
  (shadow 'WordCount (find-package "AGVWORKSPACE")))
(unless (find-package "AGVWORKSPACE::WORDCOUNT")
  (make-package "AGVWORKSPACE::WORDCOUNT"))
(unless (find-package "AGVWORKSPACE::WORDCOUNTREQUEST")
  (make-package "AGVWORKSPACE::WORDCOUNTREQUEST"))
(unless (find-package "AGVWORKSPACE::WORDCOUNTRESPONSE")
  (make-package "AGVWORKSPACE::WORDCOUNTRESPONSE"))

(in-package "ROS")





(defclass agvworkspace::WordCountRequest
  :super ros::object
  :slots (_words ))

(defmethod agvworkspace::WordCountRequest
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

(defclass agvworkspace::WordCountResponse
  :super ros::object
  :slots (_count ))

(defmethod agvworkspace::WordCountResponse
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

(defclass agvworkspace::WordCount
  :super ros::object
  :slots ())

(setf (get agvworkspace::WordCount :md5sum-) "a9a24dbc1cac26f2f8c73d77906b969c")
(setf (get agvworkspace::WordCount :datatype-) "agvworkspace/WordCount")
(setf (get agvworkspace::WordCount :request) agvworkspace::WordCountRequest)
(setf (get agvworkspace::WordCount :response) agvworkspace::WordCountResponse)

(defmethod agvworkspace::WordCountRequest
  (:response () (instance agvworkspace::WordCountResponse :init)))

(setf (get agvworkspace::WordCountRequest :md5sum-) "a9a24dbc1cac26f2f8c73d77906b969c")
(setf (get agvworkspace::WordCountRequest :datatype-) "agvworkspace/WordCountRequest")
(setf (get agvworkspace::WordCountRequest :definition-)
      "float32 words
---
uint32 count

")

(setf (get agvworkspace::WordCountResponse :md5sum-) "a9a24dbc1cac26f2f8c73d77906b969c")
(setf (get agvworkspace::WordCountResponse :datatype-) "agvworkspace/WordCountResponse")
(setf (get agvworkspace::WordCountResponse :definition-)
      "float32 words
---
uint32 count

")



(provide :agvworkspace/WordCount "a9a24dbc1cac26f2f8c73d77906b969c")


