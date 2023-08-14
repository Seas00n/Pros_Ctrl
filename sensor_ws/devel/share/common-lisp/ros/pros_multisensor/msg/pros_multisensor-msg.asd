
(cl:in-package :asdf)

(defsystem "pros_multisensor-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Foot_Plate" :depends-on ("_package_Foot_Plate"))
    (:file "_package_Foot_Plate" :depends-on ("_package"))
  ))