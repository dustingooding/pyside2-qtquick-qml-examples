cmake_minimum_required(VERSION 2.8.3)
project(now)

find_package(catkin REQUIRED)

catkin_package()

catkin_python_setup()

install(DIRECTORY resources
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

set(doxy_sources
    ${PROJECT_SOURCE_DIR}/src
    ${PROJECT_SOURCE_DIR}/scripts
)
catkin_doxygen(${PROJECT_NAME}_docs "${doxy_sources}")