cmake_minimum_required(VERSION 2.8.3)
project(atf_test)

find_package(catkin REQUIRED COMPONENTS
    rospy
    atf_core
)

#catkin_python_setup()

###################################
## catkin specific configuration ##
###################################

catkin_package(CATKIN_DEPENDS
    rospy
)

###########
## Build ##
###########

include_directories(
  ${catkin_INCLUDE_DIRS}
)

#############
## Install ##
#############

install(PROGRAMS scripts/publish_tf.py
        DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

#############
## Testing ##
#############

if(CATKIN_ENABLE_TESTING)
    find_package(rostest REQUIRED)

    message("Generate test files ...")

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
