// Generated by gencpp from file agvworkspace/AgvNavRequest.msg
// DO NOT EDIT!


#ifndef AGVWORKSPACE_MESSAGE_AGVNAVREQUEST_H
#define AGVWORKSPACE_MESSAGE_AGVNAVREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace agvworkspace
{
template <class ContainerAllocator>
struct AgvNavRequest_
{
  typedef AgvNavRequest_<ContainerAllocator> Type;

  AgvNavRequest_()
    : coordinate()  {
    }
  AgvNavRequest_(const ContainerAllocator& _alloc)
    : coordinate(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _coordinate_type;
  _coordinate_type coordinate;





  typedef boost::shared_ptr< ::agvworkspace::AgvNavRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::agvworkspace::AgvNavRequest_<ContainerAllocator> const> ConstPtr;

}; // struct AgvNavRequest_

typedef ::agvworkspace::AgvNavRequest_<std::allocator<void> > AgvNavRequest;

typedef boost::shared_ptr< ::agvworkspace::AgvNavRequest > AgvNavRequestPtr;
typedef boost::shared_ptr< ::agvworkspace::AgvNavRequest const> AgvNavRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::agvworkspace::AgvNavRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::agvworkspace::AgvNavRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace agvworkspace

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::agvworkspace::AgvNavRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::agvworkspace::AgvNavRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::agvworkspace::AgvNavRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::agvworkspace::AgvNavRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::agvworkspace::AgvNavRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::agvworkspace::AgvNavRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::agvworkspace::AgvNavRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "c65ef28c342c0d5eee21ae18aad1bb8d";
  }

  static const char* value(const ::agvworkspace::AgvNavRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xc65ef28c342c0d5eULL;
  static const uint64_t static_value2 = 0xee21ae18aad1bb8dULL;
};

template<class ContainerAllocator>
struct DataType< ::agvworkspace::AgvNavRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "agvworkspace/AgvNavRequest";
  }

  static const char* value(const ::agvworkspace::AgvNavRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::agvworkspace::AgvNavRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string coordinate\n\
";
  }

  static const char* value(const ::agvworkspace::AgvNavRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::agvworkspace::AgvNavRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.coordinate);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct AgvNavRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::agvworkspace::AgvNavRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::agvworkspace::AgvNavRequest_<ContainerAllocator>& v)
  {
    s << indent << "coordinate: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.coordinate);
  }
};

} // namespace message_operations
} // namespace ros

#endif // AGVWORKSPACE_MESSAGE_AGVNAVREQUEST_H