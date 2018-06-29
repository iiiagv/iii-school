
(cl:in-package :asdf)

(defsystem "agvworkspace-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "AgvNav" :depends-on ("_package_AgvNav"))
    (:file "_package_AgvNav" :depends-on ("_package"))
    (:file "WordCount" :depends-on ("_package_WordCount"))
    (:file "_package_WordCount" :depends-on ("_package"))
  ))