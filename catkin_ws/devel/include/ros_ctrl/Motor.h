// Generated by gencpp from file ros_ctrl/Motor.msg
// DO NOT EDIT!


#ifndef ROS_CTRL_MESSAGE_MOTOR_H
#define ROS_CTRL_MESSAGE_MOTOR_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace ros_ctrl
{
template <class ContainerAllocator>
struct Motor_
{
  typedef Motor_<ContainerAllocator> Type;

  Motor_()
    : pos_desired(0.0)
    , pos_actual(0.0)
    , vel_desired(0.0)
    , vel_actual(0.0)
    , cur_desired(0.0)
    , cur_actual(0.0)
    , temperature(0.0)
    , Kp(0.0)
    , Kb(0.0)
    , Angle_eq(0.0)
    , error(0.0)  {
    }
  Motor_(const ContainerAllocator& _alloc)
    : pos_desired(0.0)
    , pos_actual(0.0)
    , vel_desired(0.0)
    , vel_actual(0.0)
    , cur_desired(0.0)
    , cur_actual(0.0)
    , temperature(0.0)
    , Kp(0.0)
    , Kb(0.0)
    , Angle_eq(0.0)
    , error(0.0)  {
  (void)_alloc;
    }



   typedef double _pos_desired_type;
  _pos_desired_type pos_desired;

   typedef double _pos_actual_type;
  _pos_actual_type pos_actual;

   typedef double _vel_desired_type;
  _vel_desired_type vel_desired;

   typedef double _vel_actual_type;
  _vel_actual_type vel_actual;

   typedef double _cur_desired_type;
  _cur_desired_type cur_desired;

   typedef double _cur_actual_type;
  _cur_actual_type cur_actual;

   typedef double _temperature_type;
  _temperature_type temperature;

   typedef double _Kp_type;
  _Kp_type Kp;

   typedef double _Kb_type;
  _Kb_type Kb;

   typedef double _Angle_eq_type;
  _Angle_eq_type Angle_eq;

   typedef double _error_type;
  _error_type error;





  typedef boost::shared_ptr< ::ros_ctrl::Motor_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ros_ctrl::Motor_<ContainerAllocator> const> ConstPtr;

}; // struct Motor_

typedef ::ros_ctrl::Motor_<std::allocator<void> > Motor;

typedef boost::shared_ptr< ::ros_ctrl::Motor > MotorPtr;
typedef boost::shared_ptr< ::ros_ctrl::Motor const> MotorConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ros_ctrl::Motor_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ros_ctrl::Motor_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::ros_ctrl::Motor_<ContainerAllocator1> & lhs, const ::ros_ctrl::Motor_<ContainerAllocator2> & rhs)
{
  return lhs.pos_desired == rhs.pos_desired &&
    lhs.pos_actual == rhs.pos_actual &&
    lhs.vel_desired == rhs.vel_desired &&
    lhs.vel_actual == rhs.vel_actual &&
    lhs.cur_desired == rhs.cur_desired &&
    lhs.cur_actual == rhs.cur_actual &&
    lhs.temperature == rhs.temperature &&
    lhs.Kp == rhs.Kp &&
    lhs.Kb == rhs.Kb &&
    lhs.Angle_eq == rhs.Angle_eq &&
    lhs.error == rhs.error;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::ros_ctrl::Motor_<ContainerAllocator1> & lhs, const ::ros_ctrl::Motor_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace ros_ctrl

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::ros_ctrl::Motor_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ros_ctrl::Motor_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ros_ctrl::Motor_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ros_ctrl::Motor_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ros_ctrl::Motor_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ros_ctrl::Motor_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ros_ctrl::Motor_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d10d1cd9c18069d9a59d0d6841c64eb0";
  }

  static const char* value(const ::ros_ctrl::Motor_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd10d1cd9c18069d9ULL;
  static const uint64_t static_value2 = 0xa59d0d6841c64eb0ULL;
};

template<class ContainerAllocator>
struct DataType< ::ros_ctrl::Motor_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ros_ctrl/Motor";
  }

  static const char* value(const ::ros_ctrl::Motor_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ros_ctrl::Motor_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 pos_desired\n"
"float64 pos_actual\n"
"float64 vel_desired\n"
"float64 vel_actual\n"
"float64 cur_desired\n"
"float64 cur_actual\n"
"float64 temperature\n"
"float64 Kp\n"
"float64 Kb\n"
"float64 Angle_eq\n"
"float64 error\n"
;
  }

  static const char* value(const ::ros_ctrl::Motor_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ros_ctrl::Motor_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.pos_desired);
      stream.next(m.pos_actual);
      stream.next(m.vel_desired);
      stream.next(m.vel_actual);
      stream.next(m.cur_desired);
      stream.next(m.cur_actual);
      stream.next(m.temperature);
      stream.next(m.Kp);
      stream.next(m.Kb);
      stream.next(m.Angle_eq);
      stream.next(m.error);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Motor_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ros_ctrl::Motor_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ros_ctrl::Motor_<ContainerAllocator>& v)
  {
    s << indent << "pos_desired: ";
    Printer<double>::stream(s, indent + "  ", v.pos_desired);
    s << indent << "pos_actual: ";
    Printer<double>::stream(s, indent + "  ", v.pos_actual);
    s << indent << "vel_desired: ";
    Printer<double>::stream(s, indent + "  ", v.vel_desired);
    s << indent << "vel_actual: ";
    Printer<double>::stream(s, indent + "  ", v.vel_actual);
    s << indent << "cur_desired: ";
    Printer<double>::stream(s, indent + "  ", v.cur_desired);
    s << indent << "cur_actual: ";
    Printer<double>::stream(s, indent + "  ", v.cur_actual);
    s << indent << "temperature: ";
    Printer<double>::stream(s, indent + "  ", v.temperature);
    s << indent << "Kp: ";
    Printer<double>::stream(s, indent + "  ", v.Kp);
    s << indent << "Kb: ";
    Printer<double>::stream(s, indent + "  ", v.Kb);
    s << indent << "Angle_eq: ";
    Printer<double>::stream(s, indent + "  ", v.Angle_eq);
    s << indent << "error: ";
    Printer<double>::stream(s, indent + "  ", v.error);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROS_CTRL_MESSAGE_MOTOR_H
