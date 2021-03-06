cmake_minimum_required(VERSION 2.8.3)
project(atf_app_template)

find_package(catkin REQUIRED COMPONENTS
  atf_core
  rospy
)

## System dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)


## Uncomment this if the package has a setup.py. This macro ensures
## modules and global scripts declared therein get installed
## See http://ros.org/doc/api/catkin/html/user_guide/setup_dot_py.html
# catkin_python_setup()

################################################
## Declare ROS messages, services and actions ##
################################################

## To declare and build messages, services or actions from within this
## package, follow these steps:
## * Let MSG_DEP_SET be the set of packages whose message types you use in
##   your messages/services/actions (e.g. std_msgs, actionlib_msgs, ...).
## * In the file package.xml:
##   * add a build_depend and a run_depend tag for each package in MSG_DEP_SET
##   * If MSG_DEP_SET isn't empty the following dependencies might have been
##     pulled in transitively but can be declared for certainty nonetheless:
##     * add a build_depend tag for "message_generation"
##     * add a run_depend tag for "message_runtime"
## * In this file (CMakeLists.txt):
##   * add "message_generation" and every package in MSG_DEP_SET to
##     find_package(catkin REQUIRED COMPONENTS ...)
##   * add "message_runtime" and every package in MSG_DEP_SET to
##     catkin_package(CATKIN_DEPENDS ...)
##   * uncomment the add_*_files sections below as needed
##     and list every .msg/.srv/.action file to be processed
##   * uncomment the generate_messages entry below
##   * add every package in MSG_DEP_SET to generate_messages(DEPENDENCIES ...)

## Generate messages in the 'msg' folder
# add_message_files(
#   FILES
#   Message1.msg
#   Message2.msg
# )

## Generate services in the 'srv' folder
# add_service_files(
#   FILES
#   Service1.srv
#   Service2.srv
# )

## Generate actions in the 'action' folder
# add_action_files(
#   FILES
#   Action1.action
#   Action2.action
# )

## Generate added messages and services with any dependencies listed here
# generate_messages(
#   DEPENDENCIES
#   std_msgs  # Or other packages containing msgs
# )

###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## INCLUDE_DIRS: uncomment this if you package contains header files
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES atf_app_template
   CATKIN_DEPENDS rospy
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(${catkin_INCLUDE_DIRS})

## Declare a cpp library
# add_library(atf_app_template
#   src/${PROJECT_NAME}/atf_app_template.cpp
# )

## Declare a cpp executable
# add_executable(atf_app_template_node src/atf_app_template_node.cpp)

## Add cmake target dependencies of the executable/library
## as an example, message headers may need to be generated before nodes
# add_dependencies(atf_app_template_node atf_app_template_generate_messages_cpp)

## Specify libraries to link a library or executable target against
# target_link_libraries(atf_app_template_node
#   ${catkin_LIBRARIES}
# )

#############
## Install ##
#############

# all install targets should use catkin DESTINATION variables
# See http://ros.org/doc/api/catkin/html/adv_user_guide/variables.html

## Mark executable scripts (Python etc.) for installation
## in contrast to setup.py, you can choose the destination

install(PROGRAMS scripts/atf_app.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

## Mark executables and/or libraries for installation
# install(TARGETS atf_app_template atf_app_template_node
#   ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#   LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#   RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

## Mark cpp header files for installation
# install(DIRECTORY include/${PROJECT_NAME}/
#   DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
#   FILES_MATCHING PATTERN "*.h"
#   PATTERN ".svn" EXCLUDE
# )

## Mark other files for installation (e.g. launch and bag files, etc.)
# install(FILES
#   # myfile1
#   # myfile2
#   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
# )

#############
## Testing ##
#############

if(CATKIN_ENABLE_TESTING)
    find_package(rostest REQUIRED)

    SET(PKGNAME ${PROJECT_NAME} CACHE STRING "The name of the package you want to generate the test files. If you do not set this variable all test files are generated.")
    # SET(MAKETESTS "all" CACHE STRING "Choose which sort of tests you want to run (record, analyse, all). Default is 'all'.")

    if(${PKGNAME} STREQUAL ${PROJECT_NAME})

        message(STATUS "Generate test files ...")

        set(OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/Testing/tests_generated/)
        set(GENERATION_CONFIG ${CMAKE_CURRENT_SOURCE_DIR}/config/test_generation_config.yaml)

        set(EXECUTE_ARGUMENTS ${GENERATION_CONFIG} ${OUTPUT_DIRECTORY})
        set(EXECUTE_COMMAND ${atf_core_SOURCE_DIR}/scripts/generate_tests.py ${EXECUTE_ARGUMENTS})

        execute_process(
            COMMAND ${EXECUTE_COMMAND}
            WORKING_DIRECTORY ${atf_core_SOURCE_DIR}
        )

        file(GLOB TESTS_FILES ${OUTPUT_DIRECTORY}recording/*.test)
        foreach(TEST ${TESTS_FILES})
            add_rostest(${TEST}
                WORKING_DIRECTORY
                    ${CMAKE_CURRENT_SOURCE_DIR}
                PACKAGE
                    ${PROJECT_NAME}
                PKGDIR
                    ${CMAKE_CURRENT_SOURCE_DIR}
            )

            string(REPLACE "/" ";" LIST ${TEST})
            list(GET LIST -1 TEST_NAME)

            add_rostest(${OUTPUT_DIRECTORY}analysing/${TEST_NAME}
                WORKING_DIRECTORY
                    ${CMAKE_CURRENT_SOURCE_DIR}
                PACKAGE
                    ${PROJECT_NAME}
                PKGDIR
                    ${CMAKE_CURRENT_SOURCE_DIR}
            )
        endforeach()
    endif()
endif()
