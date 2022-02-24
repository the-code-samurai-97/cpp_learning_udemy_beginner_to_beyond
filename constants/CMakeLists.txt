cmake_minimum_required(VERSION 3.16)
project(constants)

add_executable(${PROJECT_NAME} src/constants.cpp)

include_directories(${PROJECT_NAME} /usr/local/include/yaml-cpp)
# add_dependencies(${PROJECT_NAME} yaml-cpp)
target_link_libraries(${PROJECT_NAME} /usr/local/lib/libyaml-cpp.so.0.7)

