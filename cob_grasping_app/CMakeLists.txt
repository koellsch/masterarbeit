cmake_minimum_required(VERSION 2.8.3)
project(cob_grasping_app)

find_package(catkin REQUIRED COMPONENTS rospy atf_core)

#catkin_python_setup()

###################################
## catkin specific configuration ##
###################################
catkin_package(CATKIN_DEPENDS rospy)

###########
## Build ##
###########

include_directories(${catkin_INCLUDE_DIRS})

install(PROGRAMS scripts/grasping_app.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

#############
## Testing ##
#############

if(CATKIN_ENABLE_TESTING)
    find_package(rostest REQUIRED)

    message("Generate test files ...")

    set(EXECUTE_ARGUMENTS ${CMAKE_CURRENT_SOURCE_DIR}/config/test_generation_config.yaml)
    set(EXECUTE_COMMAND ${atf_core_SOURCE_DIR}/scripts/generate_tests.py ${EXECUTE_ARGUMENTS})

    execute_process(
        COMMAND ${EXECUTE_COMMAND}
        WORKING_DIRECTORY "${atf_core_SOURCE_DIR}"
    )

    file(GLOB TESTS_FILES ${atf_core_SOURCE_DIR}/test/generated/recording/*.test)
    foreach(TEST ${TESTS_FILES})
        add_rostest(${TEST})
    endforeach()

    file(GLOB TESTS_FILES ${atf_core_SOURCE_DIR}/test/generated/analysing/*.test)
    foreach(TEST ${TESTS_FILES})
        add_rostest(${TEST})
    endforeach()
endif()
