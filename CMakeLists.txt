cmake_minimum_required(VERSION 2.8.12)
project(RestApiCppRestSDKConan)

add_definitions("-std=c++11")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

ADD_LIBRARY(hello hello.cpp)
ADD_EXECUTABLE(greet main.cpp)
TARGET_LINK_LIBRARIES(greet hello)
