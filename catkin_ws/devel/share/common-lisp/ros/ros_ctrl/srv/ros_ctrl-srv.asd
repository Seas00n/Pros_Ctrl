
(cl:in-package :asdf)

(defsystem "ros_ctrl-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Kill" :depends-on ("_package_Kill"))
    (:file "_package_Kill" :depends-on ("_package"))
  ))