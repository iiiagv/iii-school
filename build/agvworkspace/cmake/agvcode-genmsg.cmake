# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "agvcode: 0 messages, 2 services")

set(MSG_I_FLAGS "-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(agvcode_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/root/iii-school/src/agvworkspace/srv/WordCount.srv" NAME_WE)
add_custom_target(_agvcode_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "agvcode" "/root/iii-school/src/agvworkspace/srv/WordCount.srv" ""
)

get_filename_component(_filename "/root/iii-school/src/agvworkspace/srv/AgvNav.srv" NAME_WE)
add_custom_target(_agvcode_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "agvcode" "/root/iii-school/src/agvworkspace/srv/AgvNav.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(agvcode
  "/root/iii-school/src/agvworkspace/srv/WordCount.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/agvcode
)
_generate_srv_cpp(agvcode
  "/root/iii-school/src/agvworkspace/srv/AgvNav.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/agvcode
)

### Generating Module File
_generate_module_cpp(agvcode
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/agvcode
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(agvcode_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(agvcode_generate_messages agvcode_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/root/iii-school/src/agvworkspace/srv/WordCount.srv" NAME_WE)
add_dependencies(agvcode_generate_messages_cpp _agvcode_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/iii-school/src/agvworkspace/srv/AgvNav.srv" NAME_WE)
add_dependencies(agvcode_generate_messages_cpp _agvcode_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(agvcode_gencpp)
add_dependencies(agvcode_gencpp agvcode_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS agvcode_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages

### Generating Services
_generate_srv_eus(agvcode
  "/root/iii-school/src/agvworkspace/srv/WordCount.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/agvcode
)
_generate_srv_eus(agvcode
  "/root/iii-school/src/agvworkspace/srv/AgvNav.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/agvcode
)

### Generating Module File
_generate_module_eus(agvcode
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/agvcode
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(agvcode_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(agvcode_generate_messages agvcode_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/root/iii-school/src/agvworkspace/srv/WordCount.srv" NAME_WE)
add_dependencies(agvcode_generate_messages_eus _agvcode_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/iii-school/src/agvworkspace/srv/AgvNav.srv" NAME_WE)
add_dependencies(agvcode_generate_messages_eus _agvcode_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(agvcode_geneus)
add_dependencies(agvcode_geneus agvcode_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS agvcode_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(agvcode
  "/root/iii-school/src/agvworkspace/srv/WordCount.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/agvcode
)
_generate_srv_lisp(agvcode
  "/root/iii-school/src/agvworkspace/srv/AgvNav.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/agvcode
)

### Generating Module File
_generate_module_lisp(agvcode
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/agvcode
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(agvcode_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(agvcode_generate_messages agvcode_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/root/iii-school/src/agvworkspace/srv/WordCount.srv" NAME_WE)
add_dependencies(agvcode_generate_messages_lisp _agvcode_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/iii-school/src/agvworkspace/srv/AgvNav.srv" NAME_WE)
add_dependencies(agvcode_generate_messages_lisp _agvcode_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(agvcode_genlisp)
add_dependencies(agvcode_genlisp agvcode_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS agvcode_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages

### Generating Services
_generate_srv_nodejs(agvcode
  "/root/iii-school/src/agvworkspace/srv/WordCount.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/agvcode
)
_generate_srv_nodejs(agvcode
  "/root/iii-school/src/agvworkspace/srv/AgvNav.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/agvcode
)

### Generating Module File
_generate_module_nodejs(agvcode
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/agvcode
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(agvcode_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(agvcode_generate_messages agvcode_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/root/iii-school/src/agvworkspace/srv/WordCount.srv" NAME_WE)
add_dependencies(agvcode_generate_messages_nodejs _agvcode_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/iii-school/src/agvworkspace/srv/AgvNav.srv" NAME_WE)
add_dependencies(agvcode_generate_messages_nodejs _agvcode_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(agvcode_gennodejs)
add_dependencies(agvcode_gennodejs agvcode_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS agvcode_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(agvcode
  "/root/iii-school/src/agvworkspace/srv/WordCount.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/agvcode
)
_generate_srv_py(agvcode
  "/root/iii-school/src/agvworkspace/srv/AgvNav.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/agvcode
)

### Generating Module File
_generate_module_py(agvcode
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/agvcode
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(agvcode_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(agvcode_generate_messages agvcode_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/root/iii-school/src/agvworkspace/srv/WordCount.srv" NAME_WE)
add_dependencies(agvcode_generate_messages_py _agvcode_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/iii-school/src/agvworkspace/srv/AgvNav.srv" NAME_WE)
add_dependencies(agvcode_generate_messages_py _agvcode_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(agvcode_genpy)
add_dependencies(agvcode_genpy agvcode_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS agvcode_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/agvcode)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/agvcode
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(agvcode_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/agvcode)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/agvcode
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(agvcode_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/agvcode)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/agvcode
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(agvcode_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/agvcode)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/agvcode
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(agvcode_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/agvcode)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/agvcode\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/agvcode
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(agvcode_generate_messages_py std_msgs_generate_messages_py)
endif()
